
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
            L=self.merge_sort(left_array)
            R=self.merge_sort(right_array)

            i=0
            j=0
            a=[]

            while i < len(L) and j < len(R):    #####在左右陣列都還有東西的情況下
                if L[i] <= R[j]:                 ####左右比完放入新的陣列
                    a.append(L[i])
                    i+=1
                else:
                    a.append(R[j])
                    j+=1


            a+=L[i:]+R[j:]
                    
            return a
