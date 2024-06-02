from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/books')
def books():
    books = [
        {'title': 'Kubernetes in Action', 'author': 'Marko Luksa', 'price': 40},
        {'title': 'Kubernetes Book', 'author': 'Nigel Poulton', 'price': 35},
        {'title': 'Kubernetes Up & Running', 'author': 'Brendan Burns & Joe Beda', 'price': 45}
    ]
    return render_template('books.html', books=books)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
