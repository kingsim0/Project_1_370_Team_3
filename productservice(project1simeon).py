productservice(project1simeon).py

from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# MongoDB connection uses service name 'mongo' (defined in docker-compose)
client = MongoClient('mongodb://mongo:27017/')
db = client['ecommerce']
products_collection = db['products']

@app.route('/products/<product_id>', methods=['GET'])
def get_product(product_id):
    product = products_collection.find_one({"id": product_id})
    if product:
        product['_id'] = str(product['_id'])  # Convert ObjectId for JSON
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

def seed_sample_products():
    if products_collection.count_documents({}) == 0:
        products_collection.insert_many([
            {"id": "1001", "name": "Laptop", "price": 1200},
            {"id": "1002", "name": "Smartphone", "price": 800},
            {"id": "1003", "name": "Tablet", "price": 600}
        ])

if __name__ == '__main__':
    seed_sample_products()
    app.run(host='0.0.0.0', port=5002)
