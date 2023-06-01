'''
Leetcode problem for MAY 30:

Design a HashSet without using any built-in hash table libraries.
Implement MyHashSet class:

    -> void add(key) Inserts the value key into the HashSet.
    -> bool contains(key) Returns whether the value key exists in the HashSet or not.
    -> void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
'''


class MyHashSet:

    def __init__(self):
        self.size = 10
        self.table = [None] * self.size

    def calculate(self, key):
        return key % self.size

    def add(self, key):
        hv = self.calculate(key)

        if self.table[hv] == None:
            self.table[hv] = [key]
        else:
            self.table[hv].append(key)
        return self.table

    def remove(self, key):
        hv = self.calculate(key)

        if self.table[hv] != None:
            while key in self.table[hv]:
                self.table[hv].remove(key)
    
    def contains(self, key):
        hv = self.calculate(key)
        
        if self.table[hv] != None:
            return key in self.table[hv]
        else:
            return False
        
obj = MyHashSet()
print(obj.add(3), obj.add(1), obj.add(5))
param_3 = obj.contains(3)
print(param_3)
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
