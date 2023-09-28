import sqlite3

# Define a new word to be inserted into the database
newWord = "nova_palavra"

fileName = "Palavras_PT-BR"
dbFileName = f'{fileName}.db'

try:
    # Establish a connection to the SQLite database
    connection = sqlite3.connect(dbFileName)
    cursor = connection.cursor()

    # newWord to lowercase
    newWord = newWord.lower()

    # Check if the word already exists in the 'words' table
    cursor.execute('SELECT word FROM words WHERE word = ?', (newWord,))
    existing_word = cursor.fetchone()

    if existing_word is None:
        # If the word doesn't exist, insert it into the 'words' table
        cursor.execute('INSERT INTO words (word) VALUES (?)', (newWord,))
        connection.commit()
        print(f"Word '{newWord}' successfully inserted into the SQLite database!")
    else:
        # If the word already exists, print a message
        print(f"Word '{newWord}' already exists in the SQLite database.")

    # Close the database connection
    connection.close()

except sqlite3.Error as e:
    # Handle SQLite-specific errors
    print(f"SQLite Error: {e}")
except Exception as e:
    # Handle other general exceptions
    print(f"An error occurred: {e}")
