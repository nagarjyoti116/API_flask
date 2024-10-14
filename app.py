from flask import Flask, request, jsonify
from threading import Lock

app = Flask(__name__)
product_details = [{
        "name" :'a',
        "para1": 'a1',
        "para2": 'a2',
        "para3": 'a3',
        "para4": 'a4'
        },{
        "name" :'b',
        "para1": 'b1',
        "para2": 'b2',
        "para3": 'b3',
        "para4": 'b4'
        }]
lock = Lock()

@app.route('/')
def index():
    return "Welcome to product management!\n \nPlease use following options:\nadd: to add data to product list\nretrieve: to retrieve data\nupdate: to update data in product list\n delete: to delete data"

@app.route('/add', methods=['POST'])
def add():
    try:
        selected_product = [product for product in product_details if product["name"] == request.json['name']]

        if len(selected_product) > 0:
            return jsonify({"error": "Product with this name already exits"}), 500
        
        new_prod = {
        "name" :request.json['name'],
        "para1":request.json['para1'],
        "para2":request.json['para2'],
        "para3":request.json['para3'],
        "para4":request.json['para4']
        }
        with lock:
            product_details.append(new_prod)
    
        return jsonify({"message": "Product added successfully"}), 201
    
    except KeyError as e:
        return jsonify({"error": f"Missing key: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": "An error occurred while adding the product", "details": str(e)}), 500


@app.route('/retrieve', methods=['GET'])
def retrieve():
    try:
        para = request.data.decode('utf-8')
        products = []
        msg = ""
        with lock:
            if para == '':
                products = [product for product in product_details]  
                msg = "All products retrieved."
            else:
                for name in para.split(","):
                    name = name.strip()
                    selected_product = [product for product in product_details if product["name"] == name]
                    if selected_product:
                        selected_product = selected_product[0]
                        products.append(selected_product)
                        msg+= f"{name} is found. "
                    else:
                        msg+=  f"{name} is not found. "    

        return jsonify({"products": products, "message": msg}), 200
    
    except Exception as e:
        return jsonify({"error": "An error occurred while retrieving products", "details": str(e)}), 500
    

@app.route('/update', methods=['PUT'])
def update():
    try:
        name = request.json["name"]
        with lock:
            selected_product = [product for product in product_details if product["name"] == name]

            if selected_product:
                selected_product = selected_product[0]
                for key, value in request.json.items():
                    selected_product[key] = value
                return jsonify({"message": f"Updated product '{name}' successfully"}), 200
            else:
                return jsonify({"error": "No matching product found"}), 404

    except KeyError as e:
        return jsonify({"error": f"Missing key: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": "An error occurred while updating the product", "details": str(e)}), 500

@app.route('/delete', methods=['DELETE'])
def delete():
    try:
        names = request.data.decode('utf-8').split(",")
        msg = ""
        with lock:
            if names:
                for name in names:
                    name = name.strip()
                    selected_product = [product for product in product_details if product["name"] == name]
                    if selected_product:
                        selected_product = selected_product[0]
                        product_details.remove(selected_product)
                        msg+= f"{name} deleted\n"
                    else:
                        msg+= f"{name} not found\n"
            else:
                return jsonify({"error": "Please provide some values"}), 400
        return jsonify({"message": msg.strip()}), 200
    
    except Exception as e:
        return jsonify({"error": "An error occurred while deleting products", "details": str(e)}), 500


if __name__ == '__main__':
    app.run(port = 3030)