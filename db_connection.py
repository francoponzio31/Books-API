from mongoengine import Document, StringField, IntField


class Books(Document):
    meta = {"collection": "users"}
    book_id = IntField(required=True,unique=True)
    author = StringField(required=True,max_length=30)
    language = StringField(required=True,max_length=20)
    title = StringField(required=True,max_length=50)

def init_books_collection():

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
