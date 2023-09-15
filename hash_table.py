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

    def get_hash(self, key):
        total = 0
        for char in key:
            total += ord(char)  # ord returns the ascii value
        return total % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)  # h returns index of key
        found = False
        for index, elemnt in enumerate(self.arr[h]):
            if len(elemnt) == 2 and elemnt[0] == key:
                self.arr[h][index] = (key, value)
                found = True
        if not found:
            self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for kv in self.arr[h]:
            if kv[0] == key:
                return kv[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, kv in enumerate(self.arr[h]):
            if kv[0] == key:
                del self.arr[h]


a = HashTable()
print(a.get_hash("ajay"))
