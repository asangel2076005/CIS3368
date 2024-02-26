import flask
from flask import jsonify, request
from sql_helper import create_connection, execute_read_query, execute_query
import creds
import parser


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
    @app.route("/api/inventory/<int:index>", methods=["GET"])
    def retrieve_item(index):
        sql = "SELECT * FROM inventory;"
        users = execute_read_query(connection, sql)

        for user in users:
            if user["id"] == index:
                return jsonify(user)
        return "Invalid ID"

    @app.route('/api/inventory/<int:user_id>', methods=['PUT'])
    def update_inventory(user_id):
        data = request.get_json()

        if not data:
            return "No data provided"

        sets = []

        if "brand" in data.keys():
            brand = data["brand"]
            sets.append({"brand": brand})

        if "model" in data.keys():
            model = data["model"]
            sets.append({"model": model})

        if "load_rating" in data.keys():
            load_rating = data["load_rating"]
            sets.append({"load_rating": load_rating})

        if "speed_rating" in data.keys():
            speed_rating = data["speed_rating"]
            sets.append({"speed_rating": speed_rating})

        if "inv_type" in data.keys():
            inv_type = data["inv_type"]
            sets.append({"inv_type": inv_type})

        if "stock" in data.keys():
            stock = data["stock"]
            sets.append({"stock": stock})

        for item in sets:
            for key, value in item.items():
                if isinstance(value, int):
                    update_sql = f"UPDATE inventory SET {key} = {value} WHERE id = {user_id};"
                else:
                    update_sql = f"UPDATE inventory SET {key} = '{value}' WHERE id = {user_id};"
                execute_query(connection, update_sql)

        return "Success"


    app.run()
