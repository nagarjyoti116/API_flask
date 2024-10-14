# Product Management API

This project provides a RESTful API built with Flask to manage a collection of product information. It supports operations for adding, retrieving, updating, and deleting product records. The API is designed to be simple and easy to use for managing product data.

## Features

* Add new products to the inventory
* Retrieve product information
* Update existing product details
* Delete products from the inventory

## Requirements

* Python 3.x
* Flask

## Installation

1. Clone the repository:
```
```

2. Install the required packages:

```
pip install Flask
```
3. Run the application:
```
python app.py
```
The API will be available at http://127.0.0.1:3030/

## API Endpoints

1. Index Route

 /

Returns a welcome message and instructions on how to use the API.

2. Add Product

/add

Add a new product to the inventory.

* Request Body:
```
{
  "name": "product_name",
  "para1": "value1",
  "para2": "value2",
  "para3": "value3",
  "para4": "value4"
}
```
* Responses:
    * 201 Created: Product added successfully.
    * 500 Internal Server Error: Product with this name already exists or missing fields.

3. Retrieve Products:

/retrieve

Retrieve products based on their names.

* Request Body: Comma-separated list of product names.
* Responses:
    * 200 OK: Returns the list of retrieved products and a message.
    * 500 Internal Server Error: An error occurred while retrieving products.

4. Update Product

/update

Update an existing product's details.

* Request Body:
```
{
  "name": "product_name",
  "para1": "new_value1",
  "para2": "new_value2",
  "para3": "new_value3",
  "para4": "new_value4"
}
```
* Responses:
    * 200 OK: Product updated successfully.
    * 404 Not Found: No matching product found.
    * 400 Bad Request: Missing fields in request.

5. Delete Product

/delete

Delete products from the inventory.

* Request Body: Comma-separated list of product names to delete.
* Responses:
    * 200 OK: Returns a message indicating which products were deleted.
    * 400 Bad Request: Please provide some values.
    * 500 Internal Server Error: An error occurred while deleting products.