import sqlite3

# https://www.w3schools.com/sql/sql_like.asp
# https://www.w3schools.com/sql/sql_count.asp

# Define the select query
selectQuery = 'SELECT COUNT(*) FROM words'

dbFileName = "../Palavras_PT-BR.db"

try:
    # Establish a connection to the SQLite database
    connection = sqlite3.connect(dbFileName)
    cursor = connection.cursor()

    cursor.execute(selectQuery)

    # Fetch the results of the query
    results = cursor.fetchall()

    if results:
        print("Select result:")
        for result in results:
            print(result[0])
    else:
        print("SELECT: Nothing found")

    # Close the connection to the database
    connection.close()

except sqlite3.Error as e:
    # Handle SQLite-specific errors
    print(f"SQLite Error: {e}")
except Exception as e:
    # Handle other general exceptions
    print(f"An error occurred: {e}")
