orderservice(project1simeon).py 

from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# Connect to MongoDB (Docker service name)
client = MongoClient('mongodb://mongo:27017/')
db = client['ecommerce']
orders_collection = db['orders']

@app.route('/orders', methods=['GET'])
def get_orders_by_user():
    user_id = request.args.get('user_id')
    user_orders = list(orders_collection.find({"user_id": user_id}))
    for order in user_orders:
        order['_id'] = str(order['_id'])
    return jsonify(user_orders)

def seed_sample_orders():
    if orders_collection.count_documents({}) == 0:
        orders_collection.insert_many([
            {"order_id": "101", "user_id": "1", "product_id": "1001"},
            {"order_id": "102", "user_id": "1", "product_id": "1002"},
            {"order_id": "103", "user_id": "2", "product_id": "1003"}
        ])

if __name__ == '__main__':
    seed_sample_orders()
    app.run(host='0.0.0.0', port=5001)
