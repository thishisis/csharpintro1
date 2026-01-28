class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, key):
        return sum(ord(char) for char in key)
    
    def add(self, key, value):
        hashed_key = self.hash(key)
        if hashed_key in self.collection:
            self.collection[hashed_key][key] = value
        else:
            self.collection[hashed_key] = {key: value}
            
    def remove(self, key):
        hashed_key = self.hash(key)
        if hashed_key in self.collection:
            if len(self.collection[hashed_key]) > 1:
                if key in self.collection[hashed_key]:
                    del self.collection[hashed_key][key]
            else:
                del self.collection[hashed_key]
                
    def lookup(self, key):
        hashed_key = self.hash(key)
        pair = self.collection.get(hashed_key, None)
        if pair:
            return pair.get(key, None)
        return None
    
if __name__ == "__main__":
    ht = HashTable()
    ht.add("apple", 1)
    ht.add("banana", 2)
    ht.add("apple", 3)
    
    print("apple:", ht.lookup("apple")) 
    print("banana:", ht.lookup("banana"))
    
    ht.remove("apple")
    print("apple:", ht.lookup("apple")) 
    
    ht.remove("apple")
    print("apple:", ht.lookup("apple"))
    
    print(ht.remove("wrongkey")) 
    
    print("banana:", ht.lookup("banana"))
    
    ht.add('golf', 'sport')
    print(ht.collection)