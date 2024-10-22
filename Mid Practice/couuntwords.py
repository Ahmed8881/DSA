class KeyNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class MyHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        hash_value = 0
        for char in key:
            hash_value += ord(char)
        return hash_value % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if not self.table[index]:
            self.table[index] = []
        for node in self.table[index]:
            if node.key == key:
                node.value += 1  # Increment the value if key already exists
                return
        self.table[index].append(KeyNode(key, value))

    def search(self, key):
        index = self.hash_function(key)
        if self.table[index]:
            for node in self.table[index]:
                if node.key == key:
                    return node.value
        return None

    def display(self):
        for i in range(self.size):
            if self.table[i]:
                for node in self.table[i]:
                    print(f"{node.key}: {node.value}")

# Word counting program
def count_words(filename):
    hash_table = MyHashTable(128)
    with open(filename, 'r') as file:
        for line in file:
            word = line.strip()  # Assuming one word per line
            if hash_table.search(word):
                hash_table.insert(word, hash_table.search(word) + 1)
            else:
                hash_table.insert(word, 1)

    hash_table.display()

# Example usage: Create a file "words.txt" with words and run the program
# count_words('words.txt')
