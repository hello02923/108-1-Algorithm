from Crypto.Hash import MD5
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        self.size=0

    def add(self, key):
        h = MD5.new()
        h.update(key.encode("utf-8"))
        keycode = int(h.hexdigest(),16)
        index = keycode % self.capacity

        if not self.data[index]:
            self.data[index] = ListNode(keycode)
        else:
            temp = self.data[index]
            while temp.next:
                temp = temp.next
            temp.next = ListNode(keycode)

    def remove(self, key):
        h = MD5.new()
        h.update(key.encode("utf-8"))
        keycode = int(h.hexdigest(),16)
        index = keycode % self.capacity
        
        if not self.data[index]:
            return False
        else:
            temp=self.data[index]
            if temp.val == keycode:
                if temp.next is True:
                    self.data[index]=temp.next
                else:
                    self.data[index] = None
            else:
                while temp:
                    if temp.next == keycode:
                        temp.next = temp.next.next
                        return
                    temp = temp.next
                return False

    def contains(self, key):
        h = MD5.new()
        h.update(key.encode("utf-8"))
        keycode = int(h.hexdigest(),16)
        index = keycode % self.capacity 
        if self.data[index] is None:
            return False     
        else:
            temp = self.data[index]
            while temp:
                if temp.val == keycode:
                    return True
                elif temp.val != keycode:
                    temp = temp.next
                   
            return False

