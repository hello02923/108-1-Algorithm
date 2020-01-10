Quick Sort是把大問題分成小問題處理
挑選基準值：從數列中挑出一個元素，稱為「基準」（pivot). 

分割：重新排序數列，所有比基準值小的元素擺放在基準前面，所有比基準值大的元素擺在基準後面（與基準值相等的數可以到任何一邊. 

在這個分割結束之後，對基準值的排序就已經完成. 

遞迴排序子序列：遞迴地將小於基準值元素的子序列和大於基準值元素的子序列排序. 

遞迴到最底部的判斷條件是數列的大小是零或一，此時該數列顯然已經有序. 


# [程式碼](https://nbviewer.jupyter.org/github/hello02923/lai/blob/master/hw/quicksort_code2.ipynb)

# 流程圖
![](quicksort_chart.png)



#參考理解網站：  
http://alrightchiu.github.io/SecondRound/comparison-sort-quick-sortkuai-su-pai-xu-fa.html. 
https://www.george.tw/2019/05/05/快速排序-quick-sort/. 

 
