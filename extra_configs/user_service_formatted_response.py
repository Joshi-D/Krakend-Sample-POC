from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/users', methods=['GET'])
def get_users():
    users = [
        {'id': 1, 'name': 'John', 'email_address': 'john@example.com'},
        {'id': 2, 'name': 'Jane', 'email_address': 'jane@example.com'}]
    return jsonify(users)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
