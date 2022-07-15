from pymongo import MongoClient
import pymongo

# connect to mongodb
client = MongoClient('localhost', 27017)

# create database(test) and collection(books)
db = client.test
books = db.books

# create a document and find it
book = {
    "title": "monodb 入門",
    "price": 100,
}

books.insert_one(book)

print(books.find_one({"title": "monodb 入門",}))


# create multiple documents and find them

book_list = [
    {"isbn": "978-4873117386", "title": "入門 Python 3", "price": 4070},
    {"isbn": "978-4297111113", "title": "Python実践入門", "price": 3278},
    {"isbn": "978-4048930611", "title": "エキスパートPythonプログラミング改訂2版", "price": 3960},
]

books.insert_many(book_list)
print("document count:", books.count_documents({}))
print([book for book in books.find({}, sort = [("price", pymongo.DESCENDING)])])

# delete all
# books.delete_many({})
# print("document count:", books.count_documents({}))