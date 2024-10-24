from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb://mongo:27017/')
db = client['user_db']
users_collection = db['users']


@app.route('/')
def home():
    return "Backend container is up and running!"


# User registration
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    if users_collection.find_one({'email': data['email']}):
        return jsonify({'message': 'User already exists'}), 409
    users_collection.insert_one({
        'username': data['username'],
        'email': data['email'],
        'password': data['password'],  # NOTE: Add password encryption in production
        'gender': data['gender']
    })
    return jsonify({'message': 'User created successfully'}), 201


# User login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = users_collection.find_one({'email': data['email'], 'password': data['password']})
    if user:
        return jsonify({'username': user['username']}), 200
    return jsonify({'message': 'Invalid credentials'}), 401


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
