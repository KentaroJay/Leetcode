## ステップ1

nペア = n個の左括弧とn個の右括弧。それぞれnlとnrと呼ぶことにする。

- nl < nrの場合、左括弧か右括弧のどちらかを追加することができる。
- nl >= nrの場合、左括弧のみを追加できる。

空文字列から始めて、深さ優先探索を使用して有効な括弧のセットを生成する。

文字列は不変でコピーを作成するため、各追加操作がO(n)を消費しないように、
文字列の配列を使用した。

`parentheses`と`generatedParentheses`変数の命名に苦労した。少なくとも
逆の順序で命名すべきだった。そうすれば、より長い変数名
`generatedParentheses`の繰り返しが少なくなるから。

## ステップ2

一般的に、以下のことができる：

- `a == 0 and b == 0`は`a == b == 0`にすべき。

今回は文字列のコピーを減らすために配列のjoinを使用したが、この操作は
それほど致命的に遅くはない。そのため、代わりに単純に文字列を使用することもできる。

### パターン：文字列を使用

確かにパフォーマンスは低下するが、わずかに読みやすくなる。

### ジェネレータパターン：step2-generator.py

再帰中に文字列を追跡するためのパラメータを削減できる点が気に入っている。

### パターン：未閉じ括弧と右括弧の数を追跡

探索のためだけにコーディングした。

## ステップ3

最初の試行で解くのに12分かかった。
2回目の試行は5分かかった。

---

## step1

n pairs = n left parenthesis and n right parenthesis. Let's call nl and nr respectively.

- When nl < nr, you can either chose to append left parenthesis or right parenthesis.
- When nl >= nr, you can only append left parenthesis.

Starting from an empty string, use depth first search to generate
a set of valid parentheses.

I used an array of strings so every append operation does not take up O(n),
since string is immutable and creates copy each time.

I struggled to name `parentheses` and `generatedParentheses` varibles. I should
have at least named them in the reversed order, because then logner length variable
`generatedParentheses` would be repeated less.

## step2

Generally, I can do:

- `a == 0 and b == 0` should be `a == b == 0`.

This time I used array join to reduce string copy, but this operation is not
that critically slow. So I can just use string alternatively.

### Pattern: use string

This indeed lowers the performance, but slightly easier to read.

### Generator pattern: step2-generator.py

I like this one about being able to reduce the parameter for keeping track of
the string during the recursion.

### Pattern: keep track of numbers of unclosed brackets and right brackets

I coded this just for exploration.

## step3

It took 12min to solve at the first try.
Second try took 5 mins.
