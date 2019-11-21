

##insert(新增資料):  
>可以視為Search()的延伸.   

1.根據規則，先找到將要新增之node適合的位置  

2.再將欲新增的node接上tree. 

##delete(刪除資料): 

  1.執行刪除資料(被刪除的node稱為A),必須讓刪除A後的tree仍然維持tree的性質。  
  
  2.因此，「具有指向A的pointer」之node(也就是A的parent、leftchild以及rightchild)都必須調整該pointer，使其指向新的記憶體位置。  
  
____.以下有三種可能 
  
  Case1：欲刪除之node沒有child pointer. 
  
  solve1:將欲刪除之node的parent指向NULL.   
  
  Case2：欲刪除之node只有一個child pointer(不論是leftchild或rightchild). 
  
  solve2:將欲刪除之node的parent指向child pointer(不論是leftchild或rightchild). 
  
  Case3：欲刪除之node有兩個child pointer. 
  
  solve3:以下有兩種方式：  
  
  (a)從欲刪除的node的**左邊**樹狀結構下找出**最大**. 
  
  (b)從欲刪除的node的**右邊**樹狀結構下找出**最小**
      
      放在欲刪除的node的位置
      
      
 圖片說明：
 ![](https://github.com/hello02923/lai/blob/master/image/deletecase1.png)
 ![](https://github.com/hello02923/lai/blob/master/image/deletecase2.png)
 ![]()
 
 **Summary:**
先以Search()確認想要刪除的node是否存在tree中；
把真正會被釋放記憶體的pointer調整成「至多只有一個child」的node；
把真正會被釋放記憶體的node的child指向新的parent；
把真正會被釋放記憶體的node的parent指向新的child；
若真正會被釋放記憶體是「替身」，再把替身的資料放回BST中。
      

##search(搜尋資料):  
  1.利用Key(L)<Key(Current)<Key(R)，判斷Current應該往left subtree走，還是往right subtree走。
  
  2.Current移動到NULL，表示搜尋失敗。KEY與Current的key相同，表示搜尋成功；
  

##上面這三項操作的時間複雜度皆為O(height)

參考資料：  
http://alrightchiu.github.io/SecondRound/binary-search-tree-introjian-jie.html  
http://alrightchiu.github.io/SecondRound/binary-search-tree-searchsou-xun-zi-liao-insertxin-zeng-zi-liao.html  
http://alrightchiu.github.io/SecondRound/binary-search-tree-searchsou-xun-zi-liao-insertxin-zeng-zi-liao.html

