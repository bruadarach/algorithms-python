
""" STRING KEYS PRACTICE
Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string.

Your table will store strings in buckets by their first two letters, 
according to the formula below:

[Hash Value = (ASCII Value of First Letter * 100) + ASCII Value of Second Letter]
"""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        hv = self.calculate_hash_value(string)
        if hv != -1:
            if self.table[hv] != None:
                self.table[hv].append(string)
            else:
                self.table[hv] = [string]

    def lookup(self, string):
        hv = self.calculate_hash_value(string)
        if hv != -1:
            if self.table[hv] != None:
                if string in self.table[hv]:
                    return hv
        return -1

    def calculate_hash_value(self, string):
        value = ord(string[0])*100 + ord(string[1])
        return value


# TEST
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print(hash_table.calculate_hash_value('SUJI')) # 8385 

# Test lookup edge case
# Should be -1
print(hash_table.lookup('SUJI')) # -1

# Test store
hash_table.store('SUJI')
# Should be 8568
print(hash_table.lookup('SUJI')) # 8385

# Test store edge case
hash_table.store('SUJEONG')
# Should be 8568
print(hash_table.lookup('SUJEONG')) # 8385
