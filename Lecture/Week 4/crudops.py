import mysql.connector
from mysql.connector import Error
import creds
from sql_helper import create_connection
from sql_helper import execute_query
from sql_helper import execute_read_query

# Create a connection to MySQL database
my_creds = creds.Creds()

connection = create_connection(my_creds.connection_string,
                               my_creds.user_name,
                               my_creds.password,
                               my_creds.database_name)

# Create a new entry and add it to the table
query = "INSERT INTO users (firstname, lastname) VALUES ('Thomas', 'Edison')"
# execute_query(connection, query) # Commented so to not do it again

# Select all users
select_users = "SELECT * FROM users"
users = execute_read_query(connection, select_users)

for user in users:
    print(f"{user['firstname']} has the last name: {user['lastname']}")

# Add a table for invoices
create_invoice_table = """
CREATE TABLE IF NOT EXISTS invoices(
    id INT AUTO_INCREMENT,
    amount INT,
    description VARCHAR(255) NOT NULL,
    user_id INTEGER UNSIGNED NOT NULL,
    FOREIGN KEY fk_user_id(user_id) REFERENCES users(id),
    PRIMARY KEY (id)  
)   
"""
execute_query(connection, create_invoice_table)

# Add an invoice record to the invoice table
invoice_from_user = 1
invoice_amount = 50
invoice_description = "Harry Potter Books"

# Make sure that strings have quotes in them within the query
query = f"INSERT INTO invoices (amount, description, user_id) " \
        f"VALUES ({invoice_amount}, '{invoice_description}', {invoice_from_user})"

# execute_query(connection, query)  # Commented to not make anymore additions of the same entity

# Update Invoice Record
new_amount = 30
update_invoice_query = f"""
UPDATE invoices 
SET amount = {new_amount}
WHERE id = {invoice_from_user}
"""
# execute_query(connection, update_invoice_query)  # Commented to not do again since its reflected in db

# Delete Invoice Record from Invoice Table
# Most of the time, you want records to be inactive instead of deleted
invoice_to_delete = 1
delete_statement = f"DELETE FROM invoices WHERE id = {invoice_to_delete}"
# execute_query(connection, delete_statement)  # Commented for same reasons

#Delete invoice table
delete_table_statement = "DROP TABLE invoice"
execute_query(connection, delete_table_statement)
