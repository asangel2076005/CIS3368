import flask
from flask import jsonify, request, make_response
from sql_helper import create_connection, execute_read_query
import creds
import hashlib
import datetime
import time


if __name__ == "__main__":

    # Setting up an application name
    app = flask.Flask(__name__)  # sets up the application
    app.config["DEBUG"] = True  # allow to show errors in browser

    # password 'password' hashed
    master_password = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"
    master_username = 'username'
    valid_tokens = {
        "100",
        "200",
        "300",
        "400"
    }  # Pretend this is a database token we got from database

    # Basic http authentication, prompts username and password:
    @app.route("/authenticatedroute", methods=["GET"])
    def auth_example():
        if request.authorization:
            encoded = request.authorization.password.encode()  # Unicode coding
            hashed_result = hashlib.sha256(encoded)  # Hashing
            # Make a call to the DB and retrieve hashed value for that user

            if request.authorization.username == master_username and hashed_result.hexdigest() == master_password:
                return "<h1>We are allowed to be here</h1>"

        return make_response("Could not verify!", 401, {"WWW-Authenticate": 'Basic realm="Login Required"'})

    # Token submission as part of the url, similar to how personal SMS codes are used
    # 127.0.0.1:5000/api/token/100 or 127.0.0.1/api/token/1 for example
    @app.route("/api/token/<token>", methods=["GET"])  # <> is a placeholder
    def auth_token(token):  # Parameter needs to match the value in the placeholder
        for valid_token in valid_tokens:
            if token == valid_token:  # Check if token is valid
                # we need to discard tokens after it is used, before we reach the return statement
                return "<h1> token is valid </h1>"
        return "Invalid access token"

    # Token submission that has expiration date
    # Examples:
    # valid til Jan 1 2030: 1893456000
    # valid til Jan 1 2022: 1640995200

    # We can create time tokens easily with:
    # date = datetime.datetime(2022, 1, 1)  # Expiration date of the token
    # date_in_seconds = date.timestamp()  # Time in seconds since jan 1 1970

    # 127.0.0.1:5000/api/timetoken/1893456000 or /1640995200
    @app.route("/api/timetoken/<timetoken>", methods=["GET"])
    def auth_timetoken(timetoken):
        if float(timetoken) > time.time():  # check if token is valid right now, time.time() means right now
            return "<h1> time token is valid </h1>"
        return "token expired"

    # valid encrypted token: 7573824000
    # invalid encrypted token: 6563980800
    # Encryption with bitshift <<2 and >>2 to shift bits by 2 locations

    # 127.0.0.1:5000/api/timetokenencrypted/7573824000 or /6563980800
    @app.route("/api/timetokenencrypted/<timetoken>", methods=["GET"])
    def auth_ecrypted_timetoken(timetoken):
        encryptedtimetoken = int(timetoken)
        decryptedtimetoken = encryptedtimetoken >> 2

        if decryptedtimetoken > time.time():  # check if the token we have is valid
            return "<h1> ecrypted time token is valid </h1>"
        return "time token invalid"

    authorized_users = [
        {
            # Default user
            "username": "username",
            "password": "password",  # Should be a hash password, not plain text. only used for example
            "role": "default",
            "token": "0",
            "admin_info": None
        },
        {
            # Admin user
            "username": "otto",
            "password": "admin",
            "role": "admin",
            "token": "1234567890",
            "admin_info": "super secret admin info"
        }
    ]

    # Route to authenticate with username and password against a dataset
    # Needed for final project
    @app.route("/api/usernamepw", methods=["GET"])
    def usernamepw_example():
        username = request.headers["username"]  # Get header parameter
        pw = request.headers["password"]

        for authorized_user in authorized_users:  # Loop over users and find authorized user
            if authorized_user["username"] == username and authorized_user["password"] == pw:
                session_token = authorized_user["token"]
                admin_info = authorized_user["admin_info"]
                return_info = []
                return_info.append(authorized_user["role"])
                return_info.append(session_token)
                return_info.append(admin_info)

                return jsonify(return_info)

        # In postman, use GET and then go to headers section
        return "Security Error"

    app.run()
