from pymongo import MongoClient

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save(self):
        client = MongoClient('mongodb://localhost:27017/')
        db = client['myapp']
        users = db['users']
        users.insert_one({
            'username': self.username,
            'password': self.password
        })

    @staticmethod
    def find(username):
        client = MongoClient('mongodb://localhost:27017/')
        db = client['myapp']
        users = db['users']
        return users.find_one({'username': username})
