from AVLTree import AVLTree

# Create an AVL tree
tree = AVLTree()

# Open and read the words file
with open("../Palavras_PT-BR.txt", "r") as file:
    for line in file:
        word = line.strip()
        tree.insert(word)
        print(f"{word} inserted into AVL")

try:
    print("\nPress Ctrl + C to exit")
    while True:

        word = input("Enter a word to search: ")
        result = tree.search(word)

        if result:
            print(f"{word} found in the AVL tree.\n")
        else:
            print(f"{word} not found in the AVL tree.\n")
except KeyboardInterrupt:
    print("\nExiting the program. Bye!")