## week6  

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








