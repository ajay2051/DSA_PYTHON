# Dictionaries in Python uses hash table
# Chaining and linear probing are two techniques of collision handling.

stock_prices = []
with open("stock_prices.csv", "r") as f:
    for line in f:
        tokens = line.split(",")
        day = tokens[0]
        price = tokens[1]
        stock_prices.append([day, price])
print(stock_prices)
for element in stock_prices:
    if element[0] == "march 9":
        print(element[1])

stock_prices = {}
with open("stock_prices.csv", "r") as f:
    for line in f:
        tokens = line.split(",")
        day = tokens[0]
        price = tokens[1]
        stock_prices[day] = price
print(stock_prices)


class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):  # key = "march 6"
        total = 0
        for char in key:
            total += ord(char)  # ord returns the ascii value
        return total % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)  # h returns index of key
        found = False
        for index, hash_element in enumerate(self.arr[h]):  # self.arr[h] = [("march 9", 310), ("march 17", 240)]
            if len(hash_element) == 2 and hash_element[0] == key:
                # if conditions check in (key, value) value needs to be updated. Value needs to be updated in case where
                # for example ("march 9", 310) is already there and new march 9 needs to be updated with new value
                self.arr[h][index] = (key, value)  # (key, value) creates new (key,
                # value) because (key, value) is tuple and tuple is immutable.
                found = True
        if not found:
            self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for kv in self.arr[h]:  # ("march 9", 9) march 9 is key, 9 is value. kv means key value
            if kv[0] == key:
                return kv[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, kv in enumerate(self.arr[h]):
            if kv[0] == key:
                del self.arr[h][index]  # deletes specific index (key, value)


a = HashTable()
print(a.get_hash("ajay"))
