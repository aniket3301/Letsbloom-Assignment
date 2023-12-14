# Library Management System
RESTful API for managing a library system. The API interacts with a SQLite database and performs the following CRUD operations:
1. Retrieves all books.
   
   &emsp; a.&ensp;Endpoint: ``` GET /api/books ```
3. Adds a new book to the library. 

   &emsp; a.&ensp;Endpoint: ``` POST /api/books ```
   
   &emsp; b.&ensp;Request body: JSON object containing the book details.
   
   &emsp; c.&ensp; Example:
   ```
   {
    "author": "Aniket",
    "book_id": "1",
    "name": "Ad Astra Per Aspera"
   }
   ```
5. Updates book details for a book inputted by the user. 

   &emsp; a.&ensp;Endpoint: ``` PUT /api/books/{id} ```
   
   &emsp; b.&ensp;Request body: JSON object containing the updated book details.
   
   &emsp; c.&ensp; Example:
   
   ```
   {
    "author": "Aniket Joshi",
    "book_id": "1",
    "name": "Ad Astra Per Aspera"
   }
   ```


## Running the code locally on your system
Clone the repo: 
```
git clone https://github.com/aniket3301/Library-Management-System.git
```

Install the required dependencies: 
```
pip install -r requirements.txt
```

To spin-up the server, try one of the following commands in the root directory of the project: 

* ```python app.py```
* ```python -3 app.py```
* ```py app.py```
* ```py -3 app.py```

The requests can be made using an API testing tool such as Postman.
