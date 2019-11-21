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
    

        
    def minValueNode(self,node):
        curr = node
        while(curr.left != None):
            curr = curr.left
            return curr 


    def delete(self, root, target):  
        
        if root is None: 
            return root
          
        if target < root.val:
               root.left = self.delete(root.left,target)
                
        elif target > root.val:
            root.right = self.delete(root.right,target)

        else:
            ##no kid
            if root.left == None and root.right == None:
                root = None
            ###one kid
            elif (root.left == None) and root.right:
                if root.left:
                    root = root.left
                    self.delete(root, target)
                if root.right:
                    root = root.right
                    self.delete(root, target)
            elif root.left and (root.right == None):
                if root.left:
                    root = root.left
                    self.delete(root, target)
                if root.right:
                    root = root.right
                    self.delete(root, target)
            ##two kid
            elif node.left and node.right:
                root.val = self.minValueNode(root).val
                root.right = self.delete(self.minValueNode(root), target)
                
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
                    a[0]+=1
                dfs_a(root.left, target)
                dfs_a(root.right, target)
                
        dfs_a(root, target)
        self.delete(root, target)

        for i in range(a[0]):
            self.insert(root,new_val)
        
        return root
        
