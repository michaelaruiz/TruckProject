# Michaela Ruiz #001323526
import package


# creates hashtable - which can access objects just with a key
# the hashtable handles collisions through chaining
# the hashtable uses a list of lists because python does not traditionally support arrays
class HashTable:

    def __init__(self):
        self.size = 40
        self.hashmap = [[] for _ in range(self.size)]
        # print(self.hashmap)
    # space time complexity O(1)
    # creates constructor

    def hashing_func(self, key):
        hashed_key = hash(key) % self.size
        return hashed_key
    # creates the hash key
    # O(1)

    def insert(self, key, value):
        hash_key = self.hashing_func(key)
        key_exists = False
        bucket = self.hashmap[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if not key_exists:
            bucket.append((key, value))
    # O(N)
    # inserts the key(pid) and value into the hashtable
    # insert handles collision through chaining
    # without collisions, time complexity is O(1)

    def get(self, key):
        hash_key = self.hashing_func(key)
        bucket = self.hashmap[hash_key]
        for kv in bucket:
            k, v = kv
            if key == k:
                return v
        return None
    # O(N)
    # retrieves the value using the key

    def remove(self, key):
        hash_key = key

        if self.hashmap[hash_key] is None:
            return False
        for i in range(len(self.hashmap[hash_key])):
            if self.hashmap[hash_key][i][0] == key:
                self.hashmap[hash_key].pop(i)
                return True
    # space time complexity is O(N)
    # removes and returns the value from the hashtable

    def get_all_keys(self):
        result = []
        for bucket in self.hashmap:
            for item in bucket:
                result.append(item[0])
        return result
    # O(N^2)
    # retrieves all the keys

    # def update_status(self, key, value):
    #     key_value = self.hashing_func(key)
    #     if self.hashmap[key_value] is not None:
    #         for v in self.hashmap[key_value]:
    #             if v[0] == key:
    #                 v[8] = value
    #             return value
    #     else:
    #         print('error updating key')

    def print(self):
        print('package')
        for p in self.hashmap:
            if p is not None:
                print(str(p))
