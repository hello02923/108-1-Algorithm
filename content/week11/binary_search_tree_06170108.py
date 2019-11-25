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
                return root.left
            else:
                return self.insert(root.left,val)
                    
        else:
            if root.right == None:
                root.right = newnode
                return root.right
            else:
                return self.insert(root.right,val)
    

        
    def minValueNode(self,node):
        curr = node
        point = node.right
        while(point.left != None):
            curr = point
            point=point.left           
            return point


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
            ##one kid
            elif (root.left == None) and root.right:

                if root.right:
                    root = root.right
                    self.delete(root, target)
            elif root.left and (root.right == None):
                if root.left:
                    root = root.left
                    self.delete(root, target)
    
                    
            ##two kid
            elif root.left and root.right:
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
        ###找到回來繼續改
        if root:
            if root.val == target:
                root.val = new_val       
        if root.left:
            self.modify(root.left, target, new_val)
        
        if root.right:
            self.modify(root.right, target, new_val)
            
        return root
