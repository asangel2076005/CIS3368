import flask
from flask import jsonify, request
from sql_helper import create_connection, execute_read_query, execute_query
import creds


if __name__ == "__main__":
    # setting up an application name
    app = flask.Flask(__name__)  # sets up the application
    app.config["DEBUG"] = True  # allow to show errors in browser

    # Retrieve inventory entity set from database
    my_creds = creds.Creds()
    connection = create_connection(my_creds.connection_string,
                                   my_creds.user_name,
                                   my_creds.password,
                                   my_creds.database_name)

    # Default URL without any routing
    @app.route('/', methods=["GET"])
    def home():
        return "<h1><center>Welcome to Inventory API</center></h1>"

    # Retrieve all Inventory objects from database
    @app.route("/api/inventory", methods=["GET"])
    def retrieve_inventory():
        sql = "SELECT * FROM inventory;"
        users = execute_read_query(connection, sql)
        # for user in users:   #  Print actual current rows of the table in terminal for integrity
        #    print(user)
        return jsonify(users)

    # Retrieve all objects from database one by one
    @app.route("/api/inventory/<index>", methods=["GET"])
    def retrieve_item(index):
        sql = "SELECT * FROM inventory;"
        users = execute_read_query(connection, sql)

        for user in users:
            if user["id"] == int(index):
                return jsonify(user)
        return "Invalid ID"

    app.run()
