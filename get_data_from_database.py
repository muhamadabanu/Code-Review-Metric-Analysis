import pymysql
import pandas as pd
from logs.create_logger import create_logger
from .sql_queries import *

logger = create_logger()

def get_data_from_database(DataBase_SchemaQuery, host, user, password, database):
    try:
        # Establish the database connection
        connection = pymysql.connect(host=host, user=user, password=password, database=database)
        # Create a cursor object
        cursor = connection.cursor()
        # SQL query to show all tables
        query = DataBase_SchemaQuery
        # Execute the query to fetch all tables
        cursor.execute(query)
        tables = cursor.fetchall()
        # Remove duplicates if any
        tables = list(set(tables))
        # Dictionary to hold DataFrames, where the key is the table name
        table_dataframes = {}
        # Loop through each table and create a DataFrame
        for table in tables:
            table_name = table[0]  # Extract the table name from the tuple
            logger.info(f"Fetching data for table: {table_name}")
            # SQL query to select all data from the current table
            select_query = f"{Select_Query} {table_name}"
            # Fetch data into a pandas DataFrame
            df = pd.read_sql(select_query, connection)
            # Store the DataFrame in the dictionary with the table name as the key
            table_dataframes[table_name] = df
        # Close the cursor and connection
        cursor.close()
        connection.close()
        return table_dataframes
    except Exception as e:
        logger.error(f"An error occurred while fetching data from the database: {e}")
        return None  # Optionally return None or an empty dictionary
