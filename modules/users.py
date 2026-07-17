from flask import Blueprint, jsonify

users_bp = Blueprint('users', __name__)

# Static demo users
USERS = [
    {
        "id": 1,
        "name": "Anil Kumar",
        "email": "anil@example.com",
        "role": "Admin"
    },
    {
        "id": 2,
        "name": "Srinivasan K",
        "email": "srinivasan@example.com",
        "role": "Developer"
    }
]

@users_bp.route('/users', methods=['GET'])
def get_users():
    return jsonify({
        'status': 'OK',
        'count': len(USERS),
        'users': USERS
    }), 200
