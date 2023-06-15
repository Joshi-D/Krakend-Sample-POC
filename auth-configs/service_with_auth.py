# Flask microservice with authentication
from flask import Flask, request, abort, jsonify
import jwt

app = Flask(__name__)


@app.route('/users')
def get_users():
    auth_header = request.headers.get('Authorization')

    # Verify authentication header
    if not auth_header or not validate_token(auth_header):
        abort(401)  # Unauthorized

    # Logic to retrieve and return users
    users = [
        {'id': 1, 'name': 'John', 'email_address': 'john@example.com'},
        {'id': 2, 'name': 'Jane', 'email_address': 'jane@example.com'}]
    return jsonify(users)


def validate_token(token):
    try:
        # Replace 'SECRET_KEY' with your actual secret key used for signing
        # the tokens
        decoded_token = jwt.decode(token, options={"verify_signature": False})
        # Additional validation logic can be added here
        return True
    except jwt.exceptions.InvalidTokenError:
        return False


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)