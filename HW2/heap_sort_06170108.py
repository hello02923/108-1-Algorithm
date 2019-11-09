class Solution(object):
    
    def maxheapify(self,a,pa,n):
        kid=2*pa+1
        while kid<n:       ###向下換確認
            if kid + 1 < n:
                if a[pa]<a[kid]:      ##情況分成三種
                    if a[kid]<a[kid+1]:
                        kid=kid+1
                    a[pa],a[kid]=a[kid],a[pa]

                elif a[pa]<a[kid+1]:
                    kid=kid+1
                    a[pa],a[kid]=a[kid],a[pa]
            else:
                if a[pa]<a[kid]:
                    a[pa],a[kid]=a[kid],a[pa]
                break
            pa=kid        ###把交換的繼續交換
            kid=2*pa+1
            
            
    def heap(self, a):        ####假設有8個數字 有4個要檢查的
        n=len(a)
        i = int(n / 2 - 1)
        while i >= 0:       ####從最後的爸爸開始檢查
            self.maxheapify(a,i,n)
            i=i-1
        
    def heap_sort(self,a):

        arr = []       
        end = len(a)-1
        self.heap(a)
        
        while end>=0:      ####[0],[end]交換,建立一個新的放入,繼續跑
            
            a[0],a[end]=a[end],a[0]
            arr.append(a[end])
            self.maxheapify(a,0,end)

            end-=1
        return arr
