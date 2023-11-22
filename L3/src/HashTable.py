class HashTable:
    def __init__(self, capacity):
        self.size = 0
        self.capacity = capacity
        self.hashtable = ["0"] * capacity

    def get_size(self):
        return self.size

    def resize_table(self):
        new_capacity = 2 * self.capacity
        new_hashtable = ["0"] * new_capacity
        for value in self.hashtable:
            if value != "0":
                hash_key = self.get_hash_key(new_hashtable, value)
                new_hashtable[hash_key] = value
        self.capacity = new_capacity
        self.hashtable = new_hashtable

    def get_position(self, key):
        ascii_sum = sum(ord(char) for char in key)
        hash_value = ascii_sum % self.capacity
        while self.hashtable[hash_value] != key:
            hash_value += 1
            if hash_value >= self.capacity:
                hash_value = 0
        return hash_value

    def get_hash_key(self, hashtable, key):
        ascii_sum = sum(ord(char) for char in key)
        hash_value = ascii_sum % self.capacity
        while hashtable[hash_value] != "0":
            hash_value += 1
            if hash_value >= self.capacity:
                hash_value = 0
        return hash_value

    def add(self, value):
        if self.size == self.capacity:
            self.resize_table()
        hash_key = self.get_hash_key(self.hashtable, value)
        self.size += 1
        self.hashtable[hash_key] = value

    def remove(self, value):
        hash_key = self.get_position(value)
        self.hashtable[hash_key] = "0"
        self.size -= 1

    def __str__(self):
        result = []
        for index, key in enumerate(self.hashtable):
            if key != "0":
                result.append(f"[{key}:{index}]")
        return "\n".join(result)
