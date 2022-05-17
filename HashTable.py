class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.value = [None] * self.size

    def add_value(self, key, data):
        hash_value = self.hashfunction(key, len(self.slots))

        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.value[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.value[hash_value] = data  # replace
            else:
                next_slot = self.rehash(hash_value, len(self.slots))
                while self.slots[next_slot] is not None and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot, len(self.slots))

                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.value[next_slot] = data
                else:
                    self.value[next_slot] = data  # replace

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def get_value(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.value[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def remove(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = f'key: {self.slots[position]}, value: {self.value[position]} delete'
                self.slots[position] = None
                self.value[position] = None
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get_value(key)

    def __setitem__(self, key, value):
        self.add_value(key, value)


HashTable = HashTable()
HashTable[54] = "cat"
HashTable[26] = "dog"
HashTable[93] = "lion"
HashTable[17] = "tiger"
HashTable[77] = "bird"
HashTable[31] = "cow"
HashTable[44] = "goat"
HashTable[55] = "pig"
HashTable[20] = "chicken"
print(HashTable.slots)
print(HashTable.value)

print(HashTable[20])

HashTable[20] = 'duck'
print(HashTable.slots)
print(HashTable.value)
print(HashTable[20])
print(HashTable[99])

print(HashTable.remove(20))
print(HashTable.slots)
print(HashTable.value)
