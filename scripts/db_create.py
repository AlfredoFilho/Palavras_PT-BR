import pysqlite3 as sqlite3

dbFileName = "../Palavras_PT-BR2.db"
txtFileName = "../Palavras_PT-BR.txt"

try:
    # Establish a connection to the SQLite database
    connection = sqlite3.connect(dbFileName)
    cursor = connection.cursor()

    # Create the 'words' table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS words (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT
        )
    ''')

    # Read words from the text file and insert them into the database
    with open(txtFileName, 'r') as file:
        for line in file:
            word = line.strip()
            if word:  # Ensure the word is not empty
                cursor.execute('INSERT INTO words (word) VALUES (?)', (word,))

    # Commit the changes and close the database connection
    connection.commit()
    print("Words successfully inserted into the SQLite database!")

except sqlite3.Error as e:
    # Handle SQLite-specific errors
    print(f"SQLite Error: {e}")
except Exception as e:
    # Handle other general exceptions
    print(f"An error occurred: {e}")
finally:
    # Ensure the connection is closed
    if connection:
        connection.close()
