from logs.create_logger import create_logger

logger = create_logger()

def table_data_info(table_data, table_name):
    try:
        # Remove duplicates from the DataFrame
        table_data = table_data.drop_duplicates()

        # Count null or empty strings in each column
        null_or_empty_counts = (table_data.isnull() | (table_data == '')).sum()
        logger.info(f"{'-' * 30} Table Info: {table_name} {'-' * 30}")
        # Display the count of null or empty values
        logger.info(f"Count of null or empty values in each column: {table_name}")
        logger.info(null_or_empty_counts.to_string())  # Convert Series to string for logging

        # Total number of null or empty values in the entire DataFrame
        total_null_or_empty = null_or_empty_counts.sum()
        logger.info(f"Total null or empty values in the DataFrame: {total_null_or_empty}")

        # Get data types of each column
        column_dtypes = table_data.dtypes
        logger.info("Data types of each column:")
        logger.info(column_dtypes.to_string())  # Convert Series to string for logging

        # Get total number of rows in the DataFrame
        total_rows = len(table_data)
        logger.info(f"Total number of rows in the DataFrame: {total_rows}")

    except Exception as e:
        logger.error(f"An error occurred while processing the DataFrame: {e}")
