## 発想
LinkedListを一つずつtraverseする. この時片方がNoneであるかもしれないことに気をつける. 両方がNoneであればそこで終了. 前のループからの繰り上げにも気をつける(最初はこれに気付けずパスしなかった). sumを計算して繰り上げに関する処理を行う.


## step1

while ループのcondition文はできるだけdescriptiveにしたく、ベタ書きではなくメソッドとして切り出した（staticmethod等にするか迷ったがとりあえず速度重視でネストメソッドにした）. 繰り上げのステート管理を実装した. last_calculated とかにベタッと保存してしまって、それを後から演算して必要な情報を取り出すやり方も考えたが、このやり方がよりわかりやすいと思った.

## step3

conditionの部分のメソッドをstaticmethodにした. 理由はネストメソッドだとテストできないため. 
carryを使って実装している(模範回答)[https://leetcode.com/problems/add-two-numbers/solutions/5184763/video-simple-addition-algorithm-python-javascript-java-and-c]を見て、やっぱりincrementalとしてステート管理した方がコード読みやすくないか？と思い不採用にした（が、多くの人はccarryを使った実装のほうが読みやすいと感じるのかもしれないとも思った）.

