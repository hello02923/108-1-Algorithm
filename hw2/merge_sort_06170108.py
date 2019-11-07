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

