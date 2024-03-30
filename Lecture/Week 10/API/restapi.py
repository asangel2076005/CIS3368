import flask
from flask import jsonify
from flask import request
from sql import create_connection
from sql import execute_read_query

#setting up an application name
app = flask.Flask(__name__) #sets up the application
app.config["DEBUG"] = True #allow to show errors in browser

cars = [
    {'id': 0,
     'make': 'Jeep',
     'model': 'Grand Cherokee',
     'year': '2000',
     'color': 'black'},
    {'id': 1,
     'make': 'Ford',
     'model': 'Mustang',
     'year': '1970',
     'color': 'white'},
    {'id': 2,
     'make': 'Dodge',
     'model': 'Challenger',
     'year': '2020',
     'color': 'red'}
]

@app.route('/', methods=['GET']) # default url without any routing as GET request
def home():
    return "<h1> WELCOME TO OUR FIRST API! </h1>"

@app.route('/api/car/all', methods=['GET']) #endpoint to get all the cars: http://127.0.0.1:5000/api/car/all
def api_all():
    return jsonify(cars)

@app.route('/api/car', methods=['GET']) #endppoint to get a single car by id: http://127.0.0.1:5000/api/car?id=1
def api_id():
    if 'id' in request.args: #only if an id is provided as an argument, proceed
        id = int(request.args['id'])
    else:
        return 'ERROR: No ID provided!'
    
    results = [] #resulting car(s) to return
    for car in cars: 
        if car['id'] == id:
            results.append(car)
    return jsonify(results)

@app.route('/api/car', methods=['POST']) # add car as POST: http://127.0.0.1:5000/api/car
def add_example():          
    request_data = request.get_json()   
    newid = request_data['id']   
    newmake = request_data['make']
    newmodel = request_data['model']
    newyear = request_data['year']
    newcolor = request_data['color']                       

    cars.append({'id': newid, 'make': newmake, 'model': newmodel, 'year': newyear, 'color': newcolor})
    return 'Add request auccessful'

@app.route('/api/car', methods=['DELETE']) # delete car
def delete_example():       
    request_data = request.get_json()  
    idToDelete = request_data['id']                       
    for i in range(len(cars) - 1, -1, -1): #start, stop, step size
        if cars[i]['id'] == idToDelete:
            del(cars[i])

    return "delete request successful"

@app.route('/api/users', methods=['GET']) #API to get a user from the db table in AWS by id as a JSON response: http://127.0.0.1:5000/api/users?id=1
def api_users_id():
    if 'id' in request.args: #only if an id is provided as an argument, proceed
        id = int(request.args['id'])
    else:
        return 'ERROR: No ID provided!'

    conn = create_connection('test1.cvnfv4bycwvt.us-east-2.rds.amazonaws.com', 'admin', 'admin111', 'test1db')
    sql = "SELECT * FROM users"
    users = execute_read_query(conn, sql)
    results = []

    for user in users:
        if user['id'] == id:
            results.append(user)
    return jsonify(results)

app.run()

# API on AWS Lambda: https://cwrvx8v6xj.execute-api.us-east-2.amazonaws.com/default/apitest

# JSON parser: https://jsonformatter.org/json-parser