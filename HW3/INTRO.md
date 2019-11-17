

#insert(新增資料):  
>可以視為Search()的延伸.   

1.根據規則，先找到將要新增之node適合的位置  

2.再將欲新增的node接上tree. 

#delete(刪除資料): 

  1.執行刪除資料(被刪除的node稱為A),必須讓刪除A後的tree仍然維持tree的性質。  
  
  2.因此，「具有指向A的pointer」之node(也就是A的parent、leftchild以及rightchild)都必須調整該pointer，使其指向新的記憶體位置。  
  
____.以下有三種可能 
  
  Case1：欲刪除之node沒有child pointer. 
  
  solve1:將欲刪除之node的parent指向NULL.   
  
  Case2：欲刪除之node只有一個child pointer(不論是leftchild或rightchild). 
  
  solve2:將欲刪除之node的parent指向child pointer(不論是leftchild或rightchild). 
  
  Case3：欲刪除之node有兩個child pointer. 
  
  solve3:將欲刪除之node的rightchild往連上node的parent，往下連上leftchild. 
  
 圖片說明：
 ![](delete_case3png)
      

#search(搜尋資料):  
  1.利用Key(L)<Key(Current)<Key(R)，判斷Current應該往left subtree走，還是往right subtree走。
  
  2.Current移動到NULL，表示搜尋失敗。KEY與Current的key相同，表示搜尋成功；
  

##上面這三項操作的時間複雜度皆為O(height)
