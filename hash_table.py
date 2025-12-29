class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, key):
        return sum(ord(char) for char in key)

    def add(self, key, value):
        hash_value = self.hash(key)
        if hash_value not in self.collection:
            self.collection[hash_value] = {}
        self.collection[hash_value][key] = value

    def remove(self, key):
        hash_value = self.hash(key)
        
        if hash_value in self.collection:
            if key in self.collection[hash_value]:
                del self.collection[hash_value][key]
        return None

    def lookup(self, key):
        hash_value = self.hash(key)
        if hash_value in self.collection:
            if key in self.collection[hash_value]:
                return self.collection[hash_value][key]
            
my_dict = HashTable()
my_dict.add('1', 'Chima-001')
my_dict.add('2', 'Github.com')
my_dict.add('3', 'Command')

print(my_dict.lookup('1'))
print(my_dict.lookup('2'))
print(my_dict.lookup('3'))

print(my_dict.hash('Chima-001'))
print(my_dict.hash('Github.com'))
print(my_dict.hash('Command'))