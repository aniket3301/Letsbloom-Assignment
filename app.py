from flask import Flask, make_response, jsonify, request
import dataset

app = Flask(__name__)
db = dataset.connect('sqlite:///api.db')
books_db = db['books']

def retrieve(book_id):  
    return books_db.find_one(book_id=book_id)

def retrieve_all():
    books = []
    for book in books_db:
        books.append(book)
    return books

@app.route('/api/books', methods=['GET', 'POST'])
def api_books():
    if request.method == 'GET':
        return make_response(jsonify(retrieve_all()), 200)
    elif request.method == 'POST':
        content = request.json
        book_id = content['book_id']
        books_db.insert(content)
        return make_response(jsonify(retrieve(book_id)), 201)  

@app.route('/api/books/<book_id>', methods=['GET', 'PUT', 'DELETE'])
def api_each_book(book_id):
    if request.method == "GET":
        book_obj = retrieve(book_id)
        if book_obj:
            return make_response(jsonify(book_obj), 200)
        else:
            return make_response(jsonify(book_obj), 404)
    elif request.method == "PUT":  
        content = request.json
        books_db.update(content, ['book_id'])
        book_obj = retrieve(book_id)
        return make_response(jsonify(book_obj), 200)
    elif request.method == "DELETE":
        books_db.delete(id=book_id)
        return make_response(jsonify({}), 204)

if __name__ == '__main__':
    app.run(debug=True)