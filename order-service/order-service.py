from flask import Flask, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)

dummy_orders = {
    '1': {'product': 'Laptop', 'quantity': 2},
    '2': {'product': 'Phone', 'quantity': 1}
}

@app.route('/api/order/<user_id>', methods=['GET'])
def get_order(user_id):
    order = dummy_orders.get(user_id)
    if order:
        return jsonify(order)
    return jsonify({'error': 'Order not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)