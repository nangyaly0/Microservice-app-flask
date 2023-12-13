from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import requests

app = Flask(__name__)

user_service_url = 'http://user-service:5001/api/user/'
order_service_url = 'http://order-service:5002/api/order/'

@app.route('/api/user/<user_id>', methods=['GET'])
def get_user_order(user_id):
    order_response = requests.get(f'{order_service_url}{user_id}')
    user_response = requests.get(f'{user_service_url}{user_id}')

    if order_response.status_code == 200 and user_response.status_code == 200:
        return jsonify({
            'user': user_response.json(),
            'order': order_response.json()
        })

    return jsonify({'error': 'User or Order not found'}), 404


@app.route('/api/order/<user_id>', methods=['GET'])
def get_order(user_id):
    order_response = requests.get(f'{order_service_url}{user_id}')
    if order_response.status_code == 200:
        return jsonify(order_response.json())
    return jsonify({'error': 'Order not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

