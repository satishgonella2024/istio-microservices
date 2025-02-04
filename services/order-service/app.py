from flask import Flask, jsonify, request
import requests
import os
import redis

app = Flask(__name__)

# Redis connection
redis_client = redis.Redis(
    host=os.environ.get('REDIS_HOST', 'redis'),
    port=int(os.environ.get('REDIS_PORT', 6379)),
    decode_responses=True
)

@app.route('/', methods=['GET'])
def root():
    return jsonify({
        "service": "Order Service",
        "version": "2.0",  # Changed version
        "endpoints": [
            "/orders (GET, POST)",
            "/health"
        ]
    })

@app.route('/orders', methods=['POST'])
def create_order():
    order_data = request.get_json()
    
    if not order_data or 'product_id' not in order_data or 'quantity' not in order_data:
        return jsonify({"error": "Missing required fields"}), 400
    
    try:
        # Verify product exists
        product_response = requests.get(f"{PRODUCT_SERVICE_URL}/products")
        products = product_response.json()
        
        product_exists = any(p['id'] == order_data['product_id'] for p in products)
        if not product_exists:
            return jsonify({"error": "Product not found"}), 404
        
        # Get the next order ID
        next_id = redis_client.incr('order_id_counter')
        
        order = {
            "id": next_id,
            "product_id": order_data['product_id'],
            "quantity": order_data['quantity'],
            "status": "created",
            "version": "v2"  # Added version tag
        }
        
        # Store the order in Redis
        redis_client.hset(f"order:{next_id}", mapping=order)
        redis_client.rpush('orders', next_id)
        
        return jsonify(order), 201
    
    except requests.RequestException as e:
        return jsonify({"error": "Failed to verify product", "details": str(e)}), 503
    except redis.RedisError as e:
        return jsonify({"error": "Database error", "details": str(e)}), 503

@app.route('/orders', methods=['GET'])
def get_orders():
    try:
        # Get all order IDs
        order_ids = redis_client.lrange('orders', 0, -1)
        orders = []
        
        for order_id in order_ids:
            order = redis_client.hgetall(f"order:{order_id}")
            if order:
                order['id'] = int(order['id'])
                order['product_id'] = int(order['product_id'])
                order['quantity'] = int(order['quantity'])
                orders.append(order)
        
        return jsonify({
            "orders": orders,
            "version": "v2"
        })
    
    except redis.RedisError as e:
        return jsonify({"error": "Database error", "details": str(e)}), 503

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "version": "v2"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5002)))