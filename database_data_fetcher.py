import pymysql
from environment import *

def database_data_fetcher(QUERY):
    connection = pymysql.connect(host=Host, user=User, password=PassWord, database=DataBase)
    # Create a cursor object
    cursor = connection.cursor()
    # SQL query to show all tables
    query = QUERY
    # Execute the query to fetch all tables
    cursor.execute(query)
    df  = cursor.fetchall()
    return df