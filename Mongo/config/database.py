from pymongo import MongoClient

cliente = MongoClient("mongodb+srv://robertaju05:<juju4522>@cluster0.zmjdxzt.mongodb.net/robertaju05?retryWrites=true&w=majority")

db = cliente.todo_application

collection_name = db["todos_app"]
