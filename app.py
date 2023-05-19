from flask import Flask, request, jsonify
from mongoengine import connect
import json
from db_connection import Books, init_books_collection
import os
from dotenv import load_dotenv


app = Flask(__name__)
connect(host="mongodb://books-api-db-1/books_api")
init_books_collection() #? Seteo contenido de libros por default en la db


@app.route("/")
def index():
    return "App running..."


@app.route("/books", methods=["GET","POST"])
def books():

    books_collection = Books.objects() #? Traigo los documentos que estan almacenados en la colección

    if request.method == "GET":      
        if len(books_collection) > 0:
            parsed_books_collection = json.loads(books_collection.to_json()) #? Parseo la colección primero a json con el metodo to_json (devuelve el objeto como un string), y luego parseo ese string a una lista de diccionarios
            return jsonify(parsed_books_collection)
        else:
            return jsonify({"message": "Nothing Found"}), 404

    if request.method == "POST":
        book = Books()
        book.book_id = list(books_collection)[-1].book_id + 1
        book.author = request.form["author"]
        book.language = request.form["language"]
        book.title = request.form["title"]
        book.save()
        books_collection = Books.objects()
        parsed_books_collection = json.loads(books_collection.to_json())

        return jsonify(parsed_books_collection), 201


@app.route("/book/<int:id>",methods=["GET","PUT","DELETE"])
def single_book(id):

    books_collection = Books.objects() #? Traigo los documentos que estan almacenados en la colección

    if request.method == "GET":
        for book in books_collection:
            if book.book_id == id:
                parsed_book = json.loads(book.to_json())
                return jsonify(parsed_book)

        return jsonify({"message": "Book not found"}), 404

    if request.method == "PUT":
        for book in books_collection:
            if book.book_id == id:
                book.author = request.form.get("author") or book.author
                book.language = request.form.get("language") or book.language
                book.title = request.form.get("title") or book.title
                book.save()
                parsed_book = json.loads(book.to_json())
                return jsonify(parsed_book)

        return jsonify({"message": "Book not found"}), 404

    if request.method == "DELETE":
        for book in books_collection:
            if book.book_id == id:
                book.delete()
                books_collection = Books.objects()
                parsed_books_collection = json.loads(books_collection.to_json())
                return jsonify(parsed_books_collection)

        return jsonify({"message": "Book not found"}), 404


if __name__ == "__main__":
    load_dotenv()
    app.run(debug=True, host="0.0.0.0", port=os.getenv("FLASK_APP_PORT"))
