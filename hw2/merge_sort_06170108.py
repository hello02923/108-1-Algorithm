#!/usr/bin/env python
# coding: utf-8

# In[95]:


###### merge_sort_ID.py
arr = [2,-3,4,11,-6,5.3,7]
class Solution(object):
    def merge_sort(self,array):
        """
        :type nums: List[int] ex:[3,2,-4,6,4,2,19],[5,1,1,2,0,0]
        :rtype: List[int] ex:[-4,2,2,3,4,6,19],[0,0,1,1,2,5]
        """
        if len(array) <= 1:        
            return array
        else:        #####拆到只剩下一個，這裡是不耗時的
            middle=len(array)//2
            left_array=array[:middle]
            right_array=array[middle:]
            merge_sort(left_array)
            merge_sort(right_array)

            i=0
            j=0
            a=[]

            while i < len(left_array) and j < len(right_array):    #####在左右陣列都還有東西的情況下
                if left_array[i] < right_array[j]:                 ####左右比完放入新的陣列
                    a.append(left_array.pop(0))
                    i+=1
                else:
                    a.append(right_array.pop(0))
                    j+=1


            if right_array:      #####當左邊陣列都用完時，右邊直接放下來  #####當右邊陣列都用完時，左邊直接放下來
                a+=right_array
            else:
                a+=left_array
                    
            return a


# In[96]:


Solution().merge_sort(arr)


# In[ ]:


####樓下還在修正～～


# In[83]:


class Solution(object):
    
    def merge_sort(self,arr):
        ans = self.divide(arr)
        print(ans)
    
    def divide(self,arr):
        n = len(arr)
        if n<1:
            return arr
        else:
            mid=n//2
            left_array=arr[:mid]
            right_array=arr[mid:]
            
            
            merge=self.merge(left_array,right_array)
            left_array = self.divide(left_array)
            right_array = self.divide(right_array)
        return merge
    
    def merge(self,left_array,right_array):
        newarr=[]
        
        while left_array and right_array:                      #####在左右陣列都還有東西的情況下
            if left_array[0] < right_array[0]:                 ####左右比完放入新的陣列
                newarr.append(left_array(0))
                left_array.pop(0)
            else:
                newarr.append(right_array(0))
                right_array.pop(0)
            
        if right_array:      #####當左邊陣列都用完時，右邊直接放下來  #####當右邊陣列都用完時，左邊直接放下來
            newarr+=right_array
        else:
            newarr+=left_array
                    
        return newarr


# In[ ]:





# In[ ]:




