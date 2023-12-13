from flask import Flask, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)

dummy_users = {
    '1': {'name': 'Ali Khan', 'email': 'ali@example.com'},
    '2': {'name': 'Jane Doe', 'email': 'jane@example.com'}
}

@app.route('/api/user/<user_id>', methods=['GET'])
def get_user(user_id):
    user = dummy_users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
