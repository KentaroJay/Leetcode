## このソリューションの思考プロセス
https://discord.com/channels/1084280443945353267/1201211204547383386/1253026284938858536

### 前提
[int, int, int, int]
[int, int, int, int, int, int]

10 -> インデックス 4, 5
target = 10 // 2 = 5

### 初期ループ
[int, intA, | int, int]
  ^lo                   ^hi
[int, int, int, | intB, int, int]

intA > intB の場合、最初のパーティションを前に進めたい。

### 2回目のループ
[int, | int, int, int]
  ^lo        ^hi
[int, int, int, int, | int, int]

### 初期ループ
[int, int, | intA, int]
  ^lo                   ^hi
[int, int, intB, | int, int, int]

intB > intA の場合、2番目のパーティションを前に進めたい。

### 2回目のループ
[int, int, int, | int]
                   ^lo  ^hi
[int, int, | int, int, int, int]

### スワップが高速な理由
基本配列は適切なパーティションを設定するためのウィンドウのアンカーであるため、サイズが小さいほど検索空間が減少します。ただし、スワップしなくても結果には影響しません。

## このソリューションの思考プロセス
https://leetcode.com/problems/median-of-two-sorted-arrays/solutions/3609515/median-of-two-sorted-arrays

Amid <= B mid と仮定すると、Aleft <= Bright、Aleft + Bleft <= Bright、Aleft <= Aright + Bright と言えます。しかし、他の入力では間違っている可能性があるため、なぜこの説明がされたのかわかりません。 -> 後ほどの探索でこの前提を使う

配列AとBの範囲について、
それぞれの半分を取得し、左半分からの項目の合計数を確認します。その数が中央値ポイント未満の場合、どちらかの半分がマージされた配列の中央値より前にあることが確実にわかります。したがって、それを枝刈りできます。もう一方は、他の配列の右半分にある可能性があるため、枝刈りするかどうかは確実ではありません。

なぜ `a_index + b_index < k` なのか？ `a_index + 1 + b_index + 1 < k + 1` ではないのか？-> これは後者の方が実際には正しい(Claudeより)


