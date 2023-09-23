import sqlite3

fileName = "Palavras_PT-BR"
dbFileName = f'{fileName}.db'
txtFileName = f'{fileName}.txt'

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
    for line in open(txtFileName):
        
        word = line.strip()
        cursor.execute('INSERT INTO words (word) VALUES (?)', (word,))

    # Commit the changes and close the database connection
    connection.commit()
    connection.close()

    print("Words successfully inserted into the SQLite database!")

except sqlite3.Error as e:
    # Handle SQLite-specific errors
    print(f"SQLite Error: {e}")
except Exception as e:
    # Handle other general exceptions
    print(f"An error occurred: {e}")
