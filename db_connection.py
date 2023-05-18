from mongoengine import connect, Document, StringField, IntField
import json

class Books(Document):
    book_id = IntField(required=True,unique=True)
    author = StringField(required=True,max_length=30)
    language = StringField(required=True,max_length=20)
    title = StringField(required=True,max_length=50)

def set_db_to_default_content():

    Books.drop_collection()

    books_list = [
        {
            "id":0,
            "author":"Chinua Achebe",
            "language":"English",
            "title":"Things Fall Apart"
        },
        {   
            "id":1,
            "author":"Hans Christian Andersen",
            "language":"Danish",
            "title":"Fairy tales",
        },
        {
            "id":2,
            "author":"Samuel Beckett",
            "language":"French,English",
            "title":"Molloy,Malone Dies,The Unnamable,the trilogy",
        },
        {
            "id":3,
            "author":"Giovanni Boccaccio",
            "language":"Italian",
            "title":"The Decameron",
        },
        {
            "id":4,
            "author":"George Orwell",
            "language":"English",
            "title":"1984",
        },
        {
            "id":5,
            "author":"Emily Bront",
            "language":"English",
            "title":"Wuthering Heights",
        },
        {
            "id":6,
            "author":"Jorge Luis Borges",
            "language":"Spanish",
            "title":"Ficciones",
        }
    ]

    for b in books_list:
        book = Books()
        book.book_id = b["id"]
        book.author = b["author"]
        book.language = b["language"]
        book.title = b["title"]
        book.save()

def print_db_books_collection():
    books_collection = Books.objects()
    parsed_books_collection = json.loads(books_collection.to_json())

    for book in parsed_books_collection:
        print(json.dumps(book, indent=4), "\n")

if __name__ == "__main__":
    #connect(db="books_api",host="127.0.0.1", port=27017) # Especificando host y puerto
    connect(db="books_api") # Usando simplemente los parametros por default de mongoengine (localhost y puerto 27017)
