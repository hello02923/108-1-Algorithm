class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.linkedlist=list()
        ##直接設一個list
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= len(self.linkedlist):
            return -1
        else:
            return self.linkedlist[index]
           
         ##在index合理的範圍內，可指到下一個
            

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.linkedlist.insert(0,val)
        
        ##直接插入頭

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.linkedlist.append(val)
        
        ##在最後加一個值
     
        
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if 0 <= index and index <= len(self.linkedlist):
            self.linkedlist.insert(index,val)
            
            ##在合理範圍內加入值
    
    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if 0 <= index and index < len(self.linkedlist):
            self.linkedlist.pop(index)
            
            
            ##在範圍內刪除最後一個值
      
        
            
        
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
