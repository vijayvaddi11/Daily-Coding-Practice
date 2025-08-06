# hashmap(disctionary) in python

# def get_hash(key):
#     h=0
#     for char in key:
#         h+=ord(char)
#     return h%100
# print(get_hash('march 22'))



class HashTable:
    def __init__(self):
        self.MAX=100
        self.arr=[None for i in range(self.MAX)]
        
    def get_hash(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h%self.MAX   
        
    def __setitem__(self,key,val):
        h=self.get_hash(key)
        self.arr[h]=val
    
    def __getitem__(self,key):
        h=self.get_hash(key)
        return self.arr[h]
        
    def __delitem__(self,key):
        h=self.get_hash(key)
        self.arr[h]=None



t = HashTable()
t['march 6'] = 120
t['march 7'] = 121
t['march 22'] = 10 # uses __setitem__
t['dec 1']=108

del t['march 7']  # uses __delitem__

print(t['march 6'])    # uses __getitem__

print(t.arr)
