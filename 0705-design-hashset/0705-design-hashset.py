class listNode:
    def __init__(self,key):
        self.key = key
        self.next=None
class MyHashSet:

    def __init__(self):
        self.set = [listNode(0) for i in range(10**4)]
    
    def getHash(self,key):
        return key%len(self.set)
        

    def add(self, key: int) -> None:
        curr = self.set[self.getHash(key)]

        while curr.next:
            if curr.next.key == key:#check key alredy exist to avoid dublicates
                return
            curr=curr.next
        curr.next=listNode(key)

    def remove(self, key: int) -> None:
        curr = self.set[self.getHash(key)]

        while curr.next:
            if curr.next.key == key:
                curr.next=curr.next.next
                return
            curr=curr.next
        

    def contains(self, key: int) -> bool:
        curr = self.set[self.getHash(key)]

        while curr.next:
            if curr.next.key == key:
                return True
            curr=curr.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)