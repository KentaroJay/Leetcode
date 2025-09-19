## ステップ1

この解法について事前に調査したので、基本的なアイデアは
理解しています。しかし、いつも取るステップを踏むことで、
理解を復習するのにも良いでしょう。

* 実験

1: 0
2: 01
3: 0110
4: 01101001
5: 0110100110010110
6: 01101001100101101001011001101001

重要なポイント：

1. n行目の前半は、前の行と同一です。
2. n行目の後半は、前の行を反転したものと同一です。

* 第一のアプローチ

この2つの特性を使って、再帰的アプローチで値を取得できます。
計算複雑度 -> O(n)

* 第二のアプローチ

nに達するまで現在の状態から次の行を生成します。
kで指定された値を返します。
計算複雑度 -> O(2^n)

* 第三のアプローチ

これを二分木として扱います。(n, k)の親は(n-1, k+1 // 2)です。
n == 1に達するまで再帰を使い、0を返します。
計算複雑度 -> O(n)

今回は、典型的な解法と思われる第三のアプローチを実装したいと
思います。第一のアプローチも良いですが、少しトリッキーで、
面接中に第一のアプローチを期待されることはないと思います。

## ステップ2

1. ドキュメントを追加しました。
2. RULE -> GRAMMARに名前を変更し、コード内のドメイン知識を反映しました。

## ステップ3

5分39秒で問題を解きました。

---

## step1

Since I did some homework about this solution, I know the basic idea
on how to solve this question. However, I will go through a normal step
that I always take, which is also good for me to revise my understanding.

* Experiment

1: 0
2: 01
3: 0110
4: 01101001
5: 0110100110010110
6: 01101001100101101001011001101001

Key takeaways:

1. at the nth row, first half is identical to the previous row.
2. at the nth row, second half is identical to the flipped version of
the previous row.

* First Approach

Using this two trait, we can employ recursive approach to get the value.
Computational Complexity -> O(n)

* Second Approach

Generate the next row from the current state until it reaches to n.
Return the value that is designated by k.
Computational Complexity -> O(2^n).

* Third Approach

Deem this as a binary tree. The parent of (n, k) is (n-1, k+1 // 2).
Employ recursive until it reaches to n == 1 and return 0.
Computational Complexity -> O(n)

This time, I want to implement the third approach as it seems to be
a typical solution. The first approach is good, but it seems a bit
tricky to come up with and I don't think during the interview I will
be expected to do the first approach.

## step2

1. Added some documentation.
2. Renamed RULE -> GRAMMAR to reflect domain knowledge in the code.

## step3

Solved the problem in 5 mins and 39 secs.

