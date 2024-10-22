class KeyNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class MyHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.keys_occupied = 0

    def hash_function(self, key):
        hash_value = 0
        for char in key:
            hash_value += ord(char)
        return hash_value % self.size

    def insert(self, key, value):
        if self.keys_occupied > self.size // 2:  # If more than half full, rehash
            self.rehash()

        index = self.hash_function(key)
        if not self.table[index]:
            self.table[index] = []
        for node in self.table[index]:
            if node.key == key:
                node.value += 1
                return
        self.table[index].append(KeyNode(key, value))
        self.keys_occupied += 1

    def search(self, key):
        index = self.hash_function(key)
        if self.table[index]:
            for node in self.table[index]:
                if node.key == key:
                    return node.value
        return None

    def rehash(self):
        print("Rehashing...")
        old_table = self.table
        self.size *= 2  # Double the size of the table
        self.table = [None] * self.size
        self.keys_occupied = 0

        for bucket in old_table:
            if bucket:
                for node in bucket:
                    self.insert(node.key, node.value)

    def display(self):
        for i in range(self.size):
            if self.table[i]:
                for node in self.table[i]:
                    print(f"{node.key}: {node.value}")

# Example usage
hash_table = MyHashTable(4)
hash_table.insert("Movie Title", 5)
hash_table.insert("Movie Title 2", 3)
hash_table.insert("Movie Title 3", 1)
hash_table.insert("Movie Title 4", 2)
hash_table.insert("Movie Title 5", 4)

hash_table.display()
