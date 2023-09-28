import sqlite3

# https://www.w3schools.com/sql/sql_delete.asp

# Define the delete query
deleteQuery = 'DELETE FROM words WHERE word = "nova_palavra"'

fileName = "Palavras_PT-BR"
dbFileName = f'{fileName}.db'

try:
    # Establish a connection to the SQLite database
    connection = sqlite3.connect(dbFileName)
    cursor = connection.cursor()

    # Execute the SQL query to delete records from the 'words' table based on the criterion
    cursor.execute(deleteQuery)

    # Check how many records were affected (deleted)
    deleted_count = cursor.rowcount

    if deleted_count > 0:
        # If records were deleted, commit the transaction and print a success message
        connection.commit()
        print(f"Total records deleted: {deleted_count}.\nQuery: {deleteQuery}")
    else:
        print(f"No records were found.\nQuery: {deleteQuery}")

    # Close the connection to the database
    connection.close()

except sqlite3.Error as e:
    # Handle SQLite-specific errors
    print(f"SQLite Error: {e}")
except Exception as e:
    # Handle other general exceptions
    print(f"An error occurred: {e}")
