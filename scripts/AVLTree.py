class NodeAVL:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # Initially, node height is 1.

class AVLTree:
    def __init__(self):
        self.root = None

    def _height(self, node):
        if node is None:
            return 0
        return node.height

    def _update_height(self, node):
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _balance_factor(self, node):
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _rotate_right(self, y):
        x = y.left
        T2 = x.right

        # Perform a right rotation
        x.right = y
        y.left = T2

        # Update heights after rotation
        self._update_height(y)
        self._update_height(x)

        return x

    def _rotate_left(self, x):
        y = x.right
        T2 = y.left

        # Perform a left rotation
        y.left = x
        x.right = T2

        # Update heights after rotation
        self._update_height(x)
        self._update_height(y)

        return y

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if node is None:
            return NodeAVL(key)

        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        else:
            node.right = self._insert_recursive(node.right, key)

        # Update the height of the current node
        self._update_height(node)

        # Calculate balance factor to check for rotations
        balance = self._balance_factor(node)

        # Rotation cases to balance the tree
        if balance > 1:
            if key < node.left.key:
                return self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)

        if balance < -1:
            if key > node.right.key:
                return self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

        return node

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node

        if key < node.key:
            return self._search_recursive(node.left, key)

        return self._search_recursive(node.right, key)

    # def in_order(self):
    #     elements = []
    #     self._in_order_recursive(self.root, elements)
    #     return elements

    # def _in_order_recursive(self, node, elements):
    #     if node:
    #         self._in_order_recursive(node.left, elements)
    #         elements.append(node.key)
    #         self._in_order_recursive(node.right, elements)