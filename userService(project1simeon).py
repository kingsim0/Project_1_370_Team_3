userService(project1simeon).py
from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# MongoDB connection using Docker service name
client = MongoClient('mongodb://mongo:27017/')
db = client['ecommerce']
users_collection = db['users']

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users_collection.find_one({"id": user_id})
    if user:
        user['_id'] = str(user['_id'])  # Convert ObjectId for JSON serialization
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

def seed_sample_users():
    if users_collection.count_documents({}) == 0:
        users_collection.insert_many([
            {"id": "1", "name": "Alice"},
            {"id": "2", "name": "Bob"}
        ])

if __name__ == '__main__':
    seed_sample_users()
    app.run(host='0.0.0.0', port=5000)
