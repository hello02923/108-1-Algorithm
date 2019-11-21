
class TreeNode(object):
    def __init__(self,x):
        
        self.val = x
        self.left = None
        self.right = None
        
    def printtree(self):
        if self.left:
            
            self.left.printtree()
        
        print(self.val)
        
        if self.right:
            self.right.printtree()


class Solution(object):
    
    def insert(self, root, val):
        
        newnode=TreeNode(val)
        if root.val >= newnode.val:
            if root.left == None:
                root.left = newnode
            else:
                self.insert(root.left,val)
                    
        else:
            if root.right == None:
                root.right = newnode
            else:
                self.insert(root.right,val)
                        

    def delete(self, root, target):  
        
        if root is None: 
            return root
        
        while target!=root.val:    
            ####no child
            if target < root.val:
                root.left = self.delete(root.left,target)
            elif target > root.val:
                root.right = self.delete(root.right,target)

                ####one child 
            else:
                if root.left == None : 
                    temp = root.right  
                    root = None 
                    return temp  

                elif root.right == None : 
                    temp = root.left  
                    root = None
                    return temp 

                ###two child 
                temp = root.right
                mininode = temp.val
                while temp.left:
                    temp=temp.left
                    mininode=temp.val

                root.val=mininode
                root.right = self.delete(root.right,root.val)  

            return root
        

    def search(self, root, target):
        
        while target!=root.val:
            if target < root.val:
                if root.left == None:
                    return None
                else:
                    return self.search(root.left,target)
                
            elif target > root.val:
                
                if root.right==None:
                    return None
                else:
                    return self.search(root.right,target)
        while target == root.val:
            return root
            

    def modify(self, root, target, new_val):
        a = [0]
        def dfs_a(root, target):
            if root:
                if root.val == target:
                    a[0] = a[0]+1
                dfs_a(root.left, target)
                dfs_a(root.right, target)
        dfs_a(root, target)
        self.delete(root, target)

        for i in range(a[0]):
            self.insert(root,new_val)
        
        return root
        
        
