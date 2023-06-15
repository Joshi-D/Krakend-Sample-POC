from flask import Flask, request, jsonify
import jwt

app = Flask(__name__)
app.config['SECRET_KEY'] = '192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'


def validate_email_and_password(email, password):
    return True


@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.form
        if not data:
            return {
                "message": "Please provide user details",
                "data": None,
                "error": "Bad request"
            }, 400
        # validate input
        is_validated = validate_email_and_password(data.get('username'),
                                                   data.get('password'))
        if is_validated is not True:
            return dict(message='Invalid data', data=None,
                        error=is_validated), 400
    except Exception as e:
        return {
            "message": "Something went wrong!",
            "error": str(e),
            "data": None
        }, 500


@app.route('/token', methods=['GET', 'POST'])
def token():
    response = {
        "access_token": {
            "aud": "https://your.krakend.io",
            "iss": "http://127.0.0.1:5004",
            "sub": "1234567890qwertyuio",
            "jti": "mnb23vcsrt756yuiomnbvcx98ertyuiop",
            "roles": ["user", "admin"],
            "exp": 1735689600
        },
        "refresh_token": {
            "aud": "https://your.krakend.io",
            "iss": "http://127.0.0.1:5004",
            "sub": "1234567890qwertyuio",
            "jti": "mnb23vcsrt756yuiomn12876bvcx98ertyuiop",
            "exp": 1735689600
        },
        "exp": 1735689600
    }
    return response


@app.route('/user-profile', methods=['GET'])
def user_profile():
    print("Welcome")
    print("Request object", request.__dict__)
    # if request.headers.get('Authorization') is None:
    #     return {
    #         "message": "Please provide valid JWT token",
    #         "data": None,
    #         "error": "Bad request"
    #     }, 400

    # else:
    try:
        access_token = request.headers.get('Authorization')
        print(request.headers.get('Access-Token'))
        decoded_token_payload = jwt.decode(access_token, options={"verify_signature": False})
        return jsonify(decoded_token_payload), 200
    except Exception as e:
        # import pdb;pdb.set_trace()
        return jsonify({"msg": str(e)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)
