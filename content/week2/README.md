## week 2
 > Topic: Design a linked list

1. What's class?
    * Class，類別，可視為屬性集合而非所有物。    
    * def __init__(self,名字,年齡)，因為self是class本身 所以第一個不用更動.   
    *接下來再設定.   
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
![image](https://github.com/hello02923/lai/blob/master/image/截圖%202019-11-01%20下午6.40.01.png). 



>##時間複雜度：完全地執行程式所需的計算機時間，重點開始用使用的時間  

>##空間複雜度：完全地執行程式所需的記憶體量
