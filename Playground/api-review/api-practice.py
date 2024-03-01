import flask
from flask import jsonify, request
from sql_helper import create_connection, execute_read_query, execute_query
import creds


if __name__ == "__main__":
    # setting up an application name
    app = flask.Flask(__name__)  # sets up the application
    app.config["DEBUG"] = True  # allow to show errors in browser

    my_creds = creds.Creds()
    connection = create_connection(my_creds.connection_string,
                                   my_creds.user_name,
                                   my_creds.password,
                                   my_creds.database_name)

    @app.route("/api/login", methods=["GET"])
    def login():
        username = request.headers["username"]
        password = request.headers["password"]

        if username == "my_username" and password == "my_password":
            return "Login Success"

        return "Login Failed"

    @app.route("/", methods=["GET"])
    def welcome():
        return "Welcome to School Database"

    # Retrieve all student data
    @app.route("/api/student", methods=["GET"])
    def retrieve_student():
        sql = "SELECT * FROM STUDENT;"
        student = execute_read_query(connection, sql)
        return jsonify(student)

    # http://127.0.0.1:5000/api/student/1 or /2
    # Retrieve a single instance of student
    @app.route("/api/student/<int:student_id>", methods=["GET"])
    def retrieve_student_id(student_id):
        sql = "SELECT * FROM STUDENT"
        student = execute_read_query(connection, sql)

        for entity_instance in student:
            if entity_instance["STUDENT_ID"] == student_id:
                return jsonify(entity_instance)
        return "Invalid ID"

    # Add a student
    @app.route("/api/student", methods=["POST"])
    def add_student():
        request_data = request.get_json()

        # If no keys and values are provided in the body in POSTMAN
        if not request_data:
            return "No student data added"

        # If you include STUDENT_ID in the body
        if "STUDENT_ID" in request_data.keys():
            return "Cannot enter a student ID"

        allowed_keys = ["STUDENT_FNAME", "STUDENT_LNAME", "STUDENT_GPA", "MAJOR_CODE"]
        retrieved_keys = [key for key in request_data.keys()]

        # If you put a key other than what's in allowed_keys such as JOB_CODE OR EMPLOYEE_CODE, then an error will show
        for key in retrieved_keys:
            if key not in allowed_keys:
                return "Invalid column"

        # Since every columns (keys) are NOT NULL (WE NEED THEM), if one is missing from allowed_keys, error is shown
        # Postman will also tell you which columns (keys) you're missing
        if len(retrieved_keys) != len(allowed_keys):
            missing_keys = []
            for key in allowed_keys:
                if key not in retrieved_keys:
                    missing_keys.append(key)
            if len(missing_keys) > 1:
                return f"Error: Insufficient data. make sure {', '.join(missing_keys)} are included"
            else:
                return f"Error: Insufficient data. make sure {' '.join(missing_keys)} is included"

        # Retrieve the IDs of MAJOR
        sql = "SELECT * FROM MAJOR;"
        major = execute_read_query(connection, sql)
        major_codes = []
        for code in major:
            major_codes.append(str(code["MAJOR_CODE"]))

        # Putting a major_code outside of what the database has will lead to errors
        if str(request_data["MAJOR_CODE"]) not in major_codes:
            return f"Invalid Major Code.\n" \
                   f"Choose between {', '.join(major_codes)}"

        # Error if student GPA is less than 0 or greater than 4
        if (request_data["STUDENT_GPA"] < 0) or (request_data["STUDENT_GPA"] > 4):
            return "GPA must be between 0 and 4"

        # If student's GPA is less than the required GPA of the major, error will show; otherwise, insertion into
        # database is successful
        for major_instance in major:
            if major_instance["MAJOR_CODE"] == request_data["MAJOR_CODE"]:
                if request_data["STUDENT_GPA"] < major_instance["REQUIRED_GPA"]:
                    return "Cannot enroll student in major. Student must meet the major's gpa requirement"
                else:
                    sql = f"INSERT INTO STUDENT (STUDENT_FNAME, STUDENT_LNAME, STUDENT_GPA, MAJOR_CODE) " \
                          f"VALUES ('{request_data['STUDENT_FNAME']}', '{request_data['STUDENT_LNAME']}', {request_data['STUDENT_GPA']}, {request_data['MAJOR_CODE']});"
                    execute_query(connection, sql)
                    return "Update Success"

    # http://127.0.0.1:5000/api/student/1 or /2
    # Update a student's information
    @app.route("/api/student/<int:student_id>", methods=["PUT"])
    def update_student_id(student_id):
        request_data = request.get_json()

        # Check if the student exists
        sql = f"SELECT * FROM STUDENT WHERE STUDENT_ID = {student_id};"
        # Check will return ONE dictionary INSIDE a list
        # If you want to access the values inside the dictionary,
        # you must enter check[0]["STUDENT_ID"] to retrieve the number
        check = execute_read_query(connection, sql)
        if not check:
            return "Student does not exist"

        # If STUDENT_ID is part of the body in POSTMAN, error will occur
        if "STUDENT_ID" in request_data.keys():
            return "Cannot modify student ID"

        allowed_keys = ["STUDENT_FNAME", "STUDENT_LNAME", "STUDENT_GPA", "MAJOR_CODE"]
        retrieved_keys = [key for key in request_data.keys()]

        # If you put a key other than what's in allowed_keys such as JOB_CODE OR EMPLOYEE_CODE, then an error will show
        for key in retrieved_keys:
            if key not in allowed_keys:
                return "Invalid column"

        # This will store whatever data keys (or columns) will be changed
        sets = []

        # Retrieves MAJOR table's information for manipulating STUDENT GPA and MAJOR CODE
        sql = "SELECT * FROM MAJOR;"
        major = execute_read_query(connection, sql)

        if "STUDENT_FNAME" in request_data.keys():
            first_name = request_data["STUDENT_FNAME"]
            sets.append({"STUDENT_FNAME": first_name})

        if "STUDENT_LNAME" in request_data.keys():
            last_name = request_data["STUDENT_LNAME"]
            sets.append({"STUDENT_LNAME": last_name})

        if "STUDENT_GPA" in request_data.keys():
            gpa = request_data["STUDENT_GPA"]

            if (gpa < 0) or (gpa > 4):
                return "GPA must be between 0 and 4"

            sets.append({"STUDENT_GPA": gpa})

        if "MAJOR_CODE" in request_data.keys():
            student_major_code = request_data["MAJOR_CODE"]

            major_codes = []
            for code in major:
                major_codes.append(str(code["MAJOR_CODE"]))

            # Putting a major_code outside of what the database has will lead to errors
            if str(student_major_code) not in major_codes:
                return f"Invalid Major Code.\n" \
                       f"Choose between {', '.join(major_codes)}"

            # If you also provide the STUDENT_GPA while updating MAJOR_CODE, then this new value will be used
            # Otherwise, existing STUDENT_GPA in the database will be used instead
            if "STUDENT_GPA" in request_data.keys():
                gpa = request_data["STUDENT_GPA"]
            else:
                gpa = check[0]['STUDENT_GPA']

            # If student's GPA is less than the required GPA of the major, error will show; otherwise,
            # allow the update to happen
            for major_instance in major:
                if major_instance["MAJOR_CODE"] == student_major_code:
                    if gpa < major_instance["REQUIRED_GPA"]:
                        return "Cannot enroll student in major. Student must meet the major's gpa requirement"
                    else:
                        sets.append({"MAJOR_CODE": student_major_code})

        # Updates each item appended in the sets list
        for item in sets:
            for key, value in item.items():
                if isinstance(value, int):
                    update_sql = f"UPDATE STUDENT SET {key} = {value} WHERE STUDENT_ID = {student_id};"
                elif isinstance(value, float):
                    update_sql = f"UPDATE STUDENT SET {key} = {value} WHERE STUDENT_ID = {student_id};"
                else:
                    update_sql = f"UPDATE STUDENT SET {key} = '{value}' WHERE STUDENT_ID = {student_id};"
                execute_query(connection, update_sql)
        return "Update Success"

    # http://127.0.0.1:5000/api/student/1 or /2
    # Delete a student based on their ID
    @app.route("/api/student/<int:student_id>", methods=["DELETE"])
    def delete_student_id(student_id):
        # Check if the student exists
        sql = f"SELECT * FROM STUDENT WHERE STUDENT_ID = {student_id};"
        check = execute_read_query(connection, sql)
        if not check:
            return "Student does not exist"

        sql = f"DELETE FROM STUDENT WHERE STUDENT_ID = {student_id}"
        execute_query(connection, sql)
        return f"Student deletion success"

    # Retrieve all major data
    @app.route("/api/major", methods=["GET"])
    def retrieve_major():
        sql = "SELECT * FROM MAJOR;"
        major = execute_read_query(connection, sql)
        return jsonify(major)

    # Retrieve a major instance
    @app.route("/api/major/<int:major_code>", methods=["GET"])
    def retrieve_major_id(major_code):
        # This is another way of retrieving an instance of a table
        sql = f"SELECT * FROM MAJOR WHERE MAJOR_CODE = {major_code};"
        major = execute_read_query(connection, sql)

        # major variable will be empty, therefore no read from SQL meaning the major does not exist
        if len(major) <= 0:
            return "Invalid major ID"

        return jsonify(major[0])

    # Add a major
    @app.route("/api/major", methods=["POST"])
    def add_major():
        request_data = request.get_json()

        # If no keys and values are provided in the body in POSTMAN
        if not request_data:
            return "No student data added"

        # If you include STUDENT_ID in the body
        if "MAJOR_CODE" in request_data.keys():
            return "Cannot enter a major code"

        allowed_keys = ["MAJOR_NAME", "REQUIRED_GPA"]
        retrieved_keys = [key for key in request_data.keys()]

        # If you put a key other than what's in allowed_keys such as JOB_CODE OR EMPLOYEE_CODE, then an error will show
        for key in retrieved_keys:
            if key not in allowed_keys:
                return "Invalid column(s)"

        # Since every columns (keys) are NOT NULL (WE NEED THEM), if one is missing from allowed_keys, error is shown
        # Postman will also tell you which columns (keys) you're missing
        if len(retrieved_keys) != len(allowed_keys):
            missing_keys = []
            for key in allowed_keys:
                if key not in retrieved_keys:
                    missing_keys.append(key)
            if len(missing_keys) > 1:
                return f"Error: Insufficient data. make sure {', '.join(missing_keys)} are included"
            else:
                return f"Error: Insufficient data. make sure {' '.join(missing_keys)} is included"

        # Error if major GPA is less than 0 or greater than 4
        if (request_data["REQUIRED_GPA"] < 0) or (request_data["REQUIRED_GPA"] > 4):
            return "GPA must be between 0 and 4"

        sql = f"INSERT INTO MAJOR (MAJOR_NAME, REQUIRED_GPA)" \
              f"VALUES ('{request_data['MAJOR_NAME']}', {request_data['REQUIRED_GPA']});"
        execute_query(connection, sql)
        return "Insertion Success"

    # Update a major by code
    @app.route("/api/major/<int:major_code>", methods=["PUT"])
    def update_major_code(major_code):
        request_data = request.get_json()

        # This is another way of retrieving an instance of a table
        sql = f"SELECT * FROM MAJOR WHERE MAJOR_CODE = {major_code};"
        major = execute_read_query(connection, sql)

        # major variable will be empty, therefore no read from SQL meaning the major does not exist
        if len(major) <= 0:
            return "Invalid major ID"

        if "MAJOR_CODE" in request_data.keys():
            return "Cannot modify major code"

        allowed_keys = ["MAJOR_NAME", "REQUIRED_GPA"]
        retrieved_keys = [key for key in request_data.keys()]

        # If you put a key other than what's in allowed_keys such as JOB_CODE OR EMPLOYEE_CODE, then an error will show
        for key in retrieved_keys:
            if key not in allowed_keys:
                return "Invalid column"

        sets = []

        if "MAJOR_NAME" in request_data.keys():
            major_name = request_data["STUDENT_FNAME"]
            sets.append({"MAJOR_NAME": major_name})

        if "REQUIRED_GPA" in request_data.keys():
            required_gpa = request_data["REQUIRED_GPA"]

            if (required_gpa < 0) or (required_gpa > 4):
                return "GPA must be between 0 and 4"

            sets.append({"REQUIRED_GPA": required_gpa})

        # Updates each item appended in the sets list
        for item in sets:
            for key, value in item.items():
                if isinstance(value, float):
                    update_sql = f"UPDATE MAJOR SET {key} = {value} WHERE MAJOR_CODE = {major_code};"
                else:
                    update_sql = f"UPDATE MAJOR SET {key} = '{value}' WHERE MAJOR_CODE = {major_code};"
                execute_query(connection, update_sql)

        return "Update Success"

    # Delete a major_code based on its code
    @app.route("/api/major/<int:major_code>", methods=["DELETE"])
    def delete_major_code(major_code):
        # Check if the student exists
        sql = f"SELECT * FROM MAJOR WHERE MAJOR_CODE = {major_code};"
        check = execute_read_query(connection, sql)
        if not check:
            return "Major does not exist"

        sql = f"DELETE FROM MAJOR WHERE MAJOR_CODE = {major_code}"
        execute_query(connection, sql)
        return f"Major deletion success"

    app.run()
