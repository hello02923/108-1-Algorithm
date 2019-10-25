# 108_1_Data Structure and Algorithm
I'm 永琪。Here is my weekly learning notes. :)
  
## Content
- [week 2] 
- [week 3]
- [week 4]
- [week 6]



## week 1
 > Topic: 演算法小常識. 
 
1.演算法的簡單定義：輸入 +演算法 = 輸出. 

2.時間複雜度：衡量演算法執行好壞的工具. 

3.大 O 符號：用來描述演算法在輸入 n 個東西時，所需時間與 n 的關係. 

4.在 n 非常大時，好的演算法設計可以省下非常多時間. 

5.演算法的速度不是以秒計算，而是以**步驟次數**. 

6.實務上，我們只會紀錄最高次方的那一項，並忽略其所有的係數. 



## week 2
 > Topic: Design a linked list

1. What's class?
    * Class，類別，可視為屬性集合而非所有物。    
    
    * def __init__(self,名字,年齡)，因為self是class本身 所以第一個不用更動.   
    
     接下來再設定.   
     self.名字=名字.   
     self.年齡=年齡.   
     在這邊self.的設定 就代表你之後可以用的class屬性.   
     *temp是temporary的縮寫，代表一個“臨時”的變量.   
     *return語句用於退出函数。    
     
     
     

    
    
    
2. What's a linked-list?
   * linked-list由節點`node`與指南`pointer`組成，節點是資料實際存放的點，可散落在記憶體的不同位置，透過指南可以從第一個節點走訪到下一個節點，達成有效利用記憶體空間的目的。
   * 不同於array，array在記憶體中佔去連續的位置，但無法活用零碎的記憶體位置進行連結。  
   
   *三種功能  
   
    1.新增：加前，加後. 
    
    2.刪除：去頭，去尾，走訪所有NODE來刪除. 
    
    3.查詢：需走訪所有NODE  
    ＊可辨識性，每個Ｎode內部：至少會包含(1)data來代表資料，與(2)pointer指向下一個node，（３)hash值（位置). 
    
   
  > cf.array:  
   ＊優點：  
   （１）較Linked list為節省記憶體空間. 
   
   （２）只要利用index即可在O(1)時間對Array的資料做存取. 
   
   ～補充O(1)：陣列讀取:代表著不管你輸入多少個東西，程式都會在**同一個時間跑完**. 
   

## 時間複雜度
![image](https://github.com/hello02923/lai/blob/master/截圖%202019-10-25%20下午1.42.42.png)


## week 3
 > Topic : Stack and Queue
   * stack 疊盤，後進先出/像是復原（在儲存前都存在這)  
   #兩個指令  
    ＿push( )：新增元素至陣列的尾端，並回傳陣列的新長度。  
    ＿pop( )：刪除且回傳陣列的最後一個元素。  
    
   * queue 排隊不能插隊，先進先出/一次只能做一件事. 
   #兩個指令  
   ＿shift( )刪除且回傳陣列的第一個元素。  
   ＿push( )：新增元素至陣列的尾端，並回傳陣列的新長度。    
   
   
 stack and queue 都是一種儲存資料的方式
  
  
## week 4
1.**insertion-sort**. 
>(欲將資料由左至右以「小到大」排序)

*簡單概念：從最左邊開始，取一個，放到最後右邊，依序取左邊的去跟最右邊做比較，從小到大。  
*當問題的**資料量較小**時(欲排序的元素之數目較小)，使用Insertion Sort會很有效率，或是當問題已經「接近完成排序」的狀態時。


2.**Quick Sort**. 
>像二分法，分成左邊部分和右邊部分，把大問題分成小問題處理

*簡單概念：有一串list，取一個點當“基準點”，右邊都比他小（想成一個list，裡面是亂的），左邊都比他大（想成另一個list，亂的），現有兩個list，重複步驟。
*適用於**資料量大**時。




## week6  

1.**heap sort**. 
> 特性：「parent-child」之關係，從左往右. 
> 分成：max heap(大到小)/min heap(小到大)    


  **MaxHeapify**  
> 概念：由上而下，對有child的node進行調整。  


a.把「第一個node」和「最後一個node」互換位置。    
b.假裝最後一個node消失不見.   
c.對「第一個node」進行MaxHeapify()。    


**********************************************************
#資料來源：    

Stack and Queue：https://ithelp.ithome.com.tw/articles/10205260
quick sort:http://alrightchiu.github.io/SecondRound/comparison-sort-quick-sortkuai-su-pai-xu-fa.html
heap sort:http://alrightchiu.github.io/SecondRound/comparison-sort-heap-sortdui-ji-pai-xu-fa.html



