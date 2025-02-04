from flask import Flask, jsonify
import os

app = Flask(__name__)

# Sample product data
products = [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Smartphone", "price": 499.99}
]

@app.route('/', methods=['GET'])
def root():
    return jsonify({
        "service": "Product Service",
        "version": "1.0",
        "endpoints": [
            "/products",
            "/health"
        ]
    })

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))