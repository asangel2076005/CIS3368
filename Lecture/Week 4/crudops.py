import mysql.connector
import creds
from mysql.connector import Error
from sql import create_connection
from sql import execute_query
from sql import execut_read_query

# Create a connection to MySQL database
my_creds = creds.Creds()
print(my_creds)