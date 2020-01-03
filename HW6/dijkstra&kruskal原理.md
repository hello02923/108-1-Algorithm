# dijkstra&kruskal
dijkstra 原理說明

最短路徑算法，用於計算一個節點到其他所有節點的最短路徑。
主要特點是以起始點為中心向外層層擴展，直到擴展到終點為止。

算法思維：

#### 第一組為已求出最短路徑的頂點集合
（用S表示，初始時S中只有一個源點，以後每求得一條最短路徑, 就將加入到集合S中，直到全部頂點都加入到S中，算法就結束了）
#### 第二組為其餘未確定最短路徑的頂點集合
（用U表示），按最短路徑長度的遞增次序依次把第二組的頂點加入S中。
![](https://i.imgur.com/KDGmJ74.jpg)


在加入的過程中，總保持從源點v到S中各頂點的最短路徑長度不大於從源點v到U中任何頂點的最短路徑長度。此外，每個頂點對應一個距離，S中的頂點的距離就是從v到此頂點的最短路徑長度，U中的頂點的距離，是從v到此頂點只包括S中的頂點為中間頂點的當前最短路徑長度。



資料來源：https://blog.csdn.net/yalishadaa/article/details/55827681

kruskal's 原理說明

首先我們把所有的邊按照權值先從小到大排列，接著按照順序選取每條邊，如果這條邊的兩個端點不屬於同一集合，那麼就將它們合併，直到所有的點都屬於同一個集合為止。

算法思維：

1.將圖G看做一個森林，每個頂點為一棵獨立的樹

2.將所有的邊加入集合S，即一開始S = E

3.從S中拿出一條最短的邊(u,v)，如果(u,v)不在同一棵樹內，則連接u,v合併這兩棵樹，同時將(u,v)加入生成樹的邊集E'

4.重複(3)直到所有點屬於同一棵樹，邊集E'就是一棵最小生成樹

![](https://i.imgur.com/JkbtSHF.jpg)


資料來源：https://blog.csdn.net/luomingjun12315/article/details/47700237



資料來源https://blog.csdn.net/u010558281/article/details/53905807
https://gist.github.com/sabit-zahin/4366d29eeb0230ecc4e65e4d666062d1
https://github.com/jason-28/06170136



float("inf")   # 正無窮
float("-inf")  # 負無窮
利用 inf(infinite) 乘以 0 會得到 not-a-number(NaN)。如果一個數超出 infinite，那就是一個 NaN 數
http://kuanghy.github.io/2016/12/03/python-inf-nan



