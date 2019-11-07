>hw2. 
[詳細筆記](https://github.com/hello02923/lai/tree/master/content/week6#week6). 
##
1.**Heap sort推機排序法**. 

> Heap 利用在資料結構中二元樹的堆積樹來做資料排序，以改善選擇排序需要做的執行次數。  
> 特性：「parent-child」之關係. 
        需要連續的空間. 
        較不穩定. 
        **由左至右**都有節點。
> 分成：max heap(大到小)/min heap(小到大)/Min-max heap/Deap  四種  



  **MaxHeapify**  
> 概念：由上而下，對有child的node進行調整。  
a.把「第一個node」和「最後一個node」互換位置。    
b.假裝最後一個node消失不見.   
c.對「第一個node」進行MaxHeapify()。    


2.**Merge sort合併排序法**. 
> 利用Divide and Conquer的演算法
> 簡單概念：“分裂”到最小（**把數列拆解分割到只有一個元素**），再進行“合併”。    
> 採用演算法中分治法 Divide and conquer 的方式來解決排序問題(與Quick Sort一樣)

##方法：  
依據 左子數列(A) 與 右子數列(B) 的大小，來創建一空數列(C)。  
若 A 數列中已無任何元素，將 B 數列中剩餘的所有元素 加入 C 數列。  
若 B 數列中已無任何元素，將 A 數列中剩餘的所有元素 加入 C 數列。  
比較 A、B 兩數列的最小值，將最小值加入 C 數列。    

#heap&merge 比較  
>Heap sort是比merge sort還要來的**快速**, 但是heap sort 是in-place sorting(只需一額外記錄空間) , 也就是說它不像merge sort 每次method call 都需要去跟記憶體要一塊位置,但整體來說Heap sort 是比merge sort還要好的 .  
  
  
![image](https://github.com/hello02923/lai/blob/master/image/截圖%202019-11-07%20下午7.23.15.png)


###heapsort 參考連結:    
https://www.youtube.com/watch?v=MtQL_ll5KhQ.   
https://jason-chen-1992.weebly.com/home/selection-merge-heap. 
http://notepad.yehyeh.net/Content/Algorithm/Sort/Heap/Heap.php. 
https://zh.wikipedia.org/wiki/堆排序.   
http://alrightchiu.github.io/SecondRound/comparison-sort-heap-sortdui-ji-pai-xu-fa.html


###mergesort 參考資料：  
https://medium.com/appworks-school/初學者學演算法-排序法進階-合併排序法-6252651c6f7e. 
http://alrightchiu.github.io/SecondRound/comparison-sort-merge-sorthe-bing-pai-xu-fa.html。   
https://jason-chen-1992.weebly.com/home/selection-merge-heap. 
http://spaces.isu.edu.tw/upload/18833/3/web/sorting.htm


    



#流程圖。

heap![](https://github.com/hello02923/lai/blob/master/image/heap_sort.png).   

merge![](https://github.com/hello02923/lai/blob/master/image/merge_sort.png). 
 



