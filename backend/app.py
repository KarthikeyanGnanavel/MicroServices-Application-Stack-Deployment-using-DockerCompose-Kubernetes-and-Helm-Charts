from flask import Flask, request, jsonify
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb://mongo:27017/')
db = client['user_db']
users_collection = db['users']

# Create a unique index on the 'email' field to prevent duplicate entries
users_collection.create_index('email', unique=True)


@app.route('/')
def home():
    return "Backend container is up and running!"


# User registration
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    try:
        # Try inserting the new user; will raise DuplicateKeyError if email already exists
        users_collection.insert_one({
            'username': data['username'],
            'email': data['email'],
            'password': data['password'],  # NOTE: Add password encryption in production
            'gender': data['gender']
        })
        return jsonify({'message': 'User created successfully'}), 201

    except DuplicateKeyError:
        # Handle duplicate email error by sending a conflict response with the duplicate email
        return jsonify({'message': f'User with email {data["email"]} already exists. Please log in.'}), 409


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
