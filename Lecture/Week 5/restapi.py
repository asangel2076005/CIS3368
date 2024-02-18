import flask
from flask import jsonify, request
from sql_helper import create_connection, execute_read_query
import creds


if __name__ == "__main__":
    # setting up an application name
    app = flask.Flask(__name__)  # sets up the application
    app.config["DEBUG"] = True  # allow to show errors in browser

    cars = [
        {
            "id": 0,
            "make": "jeep",
            "model": "cherokee",
            "year": "2000",
            "color": "black"
        },
        {
            "id": 1,
            "make": "ford",
            "model": "mustang",
            "year": "1970",
            "color": "white"
        },
        {
            "id": 2,
            "make": "dodge",
            "model": "challenger",
            "year": "2020",
            "color": "read"
        }
    ]





    @app.route('/', methods=['GET'])  # default url without any routing
    def home():
        return "WELCOME TO OUR FIRST API"

    @app.route('/api/car/all', methods=['GET'])  # get all the cars
    def api_all():
        # return cars list object into a JSON object because we can't be sure the client knows Python Lists
        return jsonify(cars)

    # http://127.0.0.1:5000/api/car?id=1
    @app.route('/api/car', methods=['GET'])  # get a single car by id
    def api_id():
        if "id" in request.args:  # only if an id is provided, proceed
            id = int(request.args['id'])
        else:
            return "ERROR: no ID provided"

        results = []  # resulting car(s) to return
        for car in cars:
            if car["id"] == id:
                results.append(car)

        return jsonify(results)

    @app.route('/api/car', methods=['POST'])  # add a car
    def add_example():
        request_data = request.get_json()  # requests data on a stack. Gets a JSON object
        new_id = request_data['id']
        new_name = request_data['make']
        new_model = request_data['model']
        new_year = request_data['year']
        new_color = request_data['color']

        cars.append({
            'id': new_id,
            'make': new_name,
            'model': new_model,
            'new_year': new_year,
            'color': new_color
        })

        return "Add request successful!"

    @app.route("/api/car", methods=["DELETE"])  # delete a car
    def delete_example():
        request_data = request.get_json()
        id_to_delete = request_data["id"]

        # we start at the end to the start of the list
        # because if we remove an item from a list, the next item to iterate will be ignored
        # when deleting, always iterate beginning from the last item
        for i in range(len(cars) - 1, -1, -1):  # start, stop, step size
            if cars[i]['id'] == id_to_delete:
                del(cars[i])
        return "delete request successful"

    @app.route("/api/car", methods=["PUT"])  # api to update an entity instance
    def api_update_user():
        pass
        # figure this one out later

    # This area deals with my database
    my_creds = creds.Creds()
    connection = create_connection(my_creds.connection_string,
                                   my_creds.user_name,
                                   my_creds.password,
                                   my_creds.database_name)
    sql = "SELECT * FROM users"
    users = execute_read_query(connection, sql)

    @app.route("/api/users/all", methods=["GET"])  # api to get users from the db table in AWS by id in JSON response
    def api_users_id():
        return jsonify(users)

    # http://127.0.0.1:5000/api/users?id=1
    @app.route('/api/users', methods=['GET'])  # get a single car by id
    def api_id_user():
        if "id" in request.args:  # only if an id is provided, proceed
            id = int(request.args['id'])
        else:
            return "ERROR: no ID provided"

        results = []  # resulting car(s) to return
        for user in users:
            if user["id"] == id:
                results.append(user)

        return jsonify(results)

    app.run()
