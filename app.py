from flask import Flask, jsonify, request
from http import HTTPStatus  # includes different http statuses
from book_store import books


app = Flask(__name__)


@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({'data': books})  # converts list of books to json format


@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()

    title = data.get('book_title')
    author = data.get('book_author')
    publisher = data.get('publisher')
    description = data.get('description')

    book = {
        "id": len(books)+1,  # remember we start counting from zero
        "title": title,
        "author": author,
        'publisher': publisher,
        'description': description
    }

    books.append(book)

    return jsonify(books), HTTPStatus.CREATED


@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)

    if not book:
        return jsonify({'message': "book not found"}), HTTPStatus.NOT_FOUND

    data = request.get_json()
    book.update(
        {
            'title': data.get('book_title'),
            'author': data.get('book_author'),
            'publisher': data.get('publisher'),
            'description': data.get('description'),
        }
    )

    return jsonify(book)


@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next(
        (book for book in books if book['id'] == book_id),
         None)#enables us get the next book in our mock data else return None

    if book:
        return jsonify(book)
    return jsonify({"message": "Book not found "}), HTTPStatus.NOT_FOUND


if __name__ == '__main__': #stats up the flask server
    app.run()
