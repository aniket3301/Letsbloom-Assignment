# Letsbloom-Assignment
RESTful API for managing a library system. The API interacts with a SQLite database and performs the following CRUD operations:
1. Retrieves all books. (Endpoint: ``` GET /api/books ```) 
2. Adds a new book to the library. (Endpoint: ``` POST /api/books ```)
3. Updates book details for a book inputted by the user. (Endpoint: ```PUT /api/books/{id}```)

The request body for the POST and PUT requests should be JSON objects with "author", "book_id" and "name" keys. 


## Running the code locally on your system:
Clone the repo: ```git clone https://github.com/aniket3301/Letsbloom-Assignment.git```

Install the required dependencies: ```pip install -r requirements.txt```

To spin-up the server, try one of the following commands in the root directory of the project: 

* ```python app.py```
* ```python -3 app.py```
* ```py app.py```
* ```py -3 app.py```

The requests can be made using an API testing tool such as Postman.
