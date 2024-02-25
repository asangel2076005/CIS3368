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

    # Add new tire to the inventory
    @app.route("/api/inventory", methods=["POST"])
    def add_inventory():
        request_data = request.get_json()
        brand = request_data["brand"]
        model = request_data["model"]
        load_rating = request_data["load_rating"]
        speed_rating = request_data["speed_rating"]
        inv_type = request_data["inv_type"]
        stock = request_data["stock"]

        # Adds the new tire to my database
        update_sql = f"INSERT INTO inventory(brand, model, load_rating, speed_rating, inv_type, stock)" \
                     f"VALUES ('{brand}','{model}', {load_rating}, '{speed_rating}', '{inv_type}', {stock});"
        execute_query(connection, update_sql)

        return "Successfully added a tire"

    # Update a tire in inventory
    @app.route("/api/inventory", methods=["PUT"])
    def update_inventory():
        request_data = request.get_json()
        user_id = request_data["id"]
        stock = request_data["stock"]

        update_sql = f"UPDATE inventory SET stock = {stock} WHERE id = {user_id};"
        execute_query(connection, update_sql)

        return "Update Success"

    # Delete an item from inventory
    @app.route("/api/inventory", methods=["DELETE"])
    def delete_inventory():
        sql = "SELECT * FROM inventory;"
        users = execute_read_query(connection, sql)
        request_data = request.get_json()
        user_id = request_data["id"]

        # we start at the end to the start of the list
        # because if we remove an item from a list, the next item to iterate will be ignored
        # when deleting, always iterate beginning from the last item
        for i in range(len(users) - 1, -1, -1):  # start, stop, step size
            if users[i]['id'] == user_id:
                del (users[i])

        delete_sql = f"DELETE FROM inventory WHERE id = {user_id}"
        execute_query(connection, delete_sql)

        return "Delete request successful"

    app.run()
