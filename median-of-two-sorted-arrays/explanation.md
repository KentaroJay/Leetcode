(英語で書いたものをClaudeで日本語に訳しているのでちょっと変かもしれません。英語も練習中なので英語自体も変かもしれませんが)

## パーティション（2つの仮想配列の作成）

- 解答配列の前半部分と後半部分を表す2つの仮想配列を作成します。
- そのために、各配列にパーティションを作成します。

### パーティションとは？

身長順に並んだ2つの人の列を考えてください。基本的には、両方の列の全員を身長順に並べた時の前半部分と後半部分を表す別のタイプの列を形成するように人々に指示したいのです。
そのために、両方の列に「フラグ」を置きたいのです。
フラグの前にいる人は前半の列に行き、フラグの後ろにいる人は後半の列に行かなければなりません。

**例**
[int, int, | int, ..., int, int, int] -> これは最初の2人が前半の列に行き、残りは後半に行くことを意味します。
[int, int, int, ..., int, int, int | ] -> これはこの列の全員が前半の列に行くことを意味します。

### パーティションの位置をどのように決定するか？
**制約**

1. パーティションは列のどこかになければなりません。
2. 両方のパーティションのインデックスを足し合わせると中央値のインデックスに等しくなるようにパーティションを定義します。

配列 = 前半配列 + 後半配列
配列の長さが偶数の場合、中央値は `(前半配列の最後の要素 + 後半配列の最初の要素) / 2` です。
配列の長さが奇数の場合、中央値は `前半配列の最後の要素` です。

パーティションを置く適切な場所を二分探索するためのウィンドウを考えます。
最初に、配列全体にまたがるウィンドウがあります。

[int, int, int, ..., int, int, int]
 ^left                              ^right

次にその中間を取得します。2番目の制約により、この時点で他のパーティションも決定できます。
基本的に、中央値のインデックスまでできるだけ多くの要素が欲しいのです。

[int, int, int, ..., int | int, .., int, int, int]          [int, int, ..., int, int]
 ^left                   ^mid                      ^right  ^  ^    ^         ^    ^   ^  他のパーティションはどこか

> mid = (right - left) // 2、右側ウィンドウの最初の値のインデックスを表します。
> kを中間点のインデックスとします。
> mid - left < k + 1 の場合、他の配列から `k + 1 - (mid - left)` 個の要素が必要です。
> mid - left == k + 1 の場合、他の配列から要素は必要ありません。
> mid - left > k + 1 の場合、このウィンドウで二分探索を行います。

max(左側ウィンドウの要素) <= min(右側ウィンドウの要素) の場合、それは適切なパーティションです。
最初の配列の左側の最後の要素 > 2番目の配列の右側の最初の要素の場合、right = mid - 1。
2番目の配列の左側の最後の要素 > 最初の配列の右側の最初の要素の場合、left = mid + 1。

---

## Partition(Create two virtual array)

- Create two virtual that represents the former part and the latter part of the answer array.
- In order to do it, we create partitions in each given arrays.

### What is partition?

Think of two queues of people, sorted by their heights. We basically want to tell people to form another type of queues that represents the former part and the latter part of the queue that all the people from both queues sorted in heights.
In order to do that, we want to put "flags" to both of the queues.
The people before the flag have to go to the fomer part queue, meanwhile the people after the flag have to go to the latter queue.

**Example**
[int, int, | int, ..., int, int, int] -> This means the first two people have to go to the former queue, the others have to go to the latter.
[int, int, int, ..., int, int, int | ] -> This means all people from this queue have to go to the former queue.

### How to determine the positions of the partitions?
**Constraints**

1. The partition has to be somewhere in the queue.
2. We define partitions so indexes of both partitions added together equals to the index of the median.

array = former array + latter array
if array length is even, then the median is `(last item from the former array + the first item from the latter array) / 2`.
if array length is odd, then the median is `last item from the former array`.

We think of a window to binary search the proper place to put the partition.
Initially, we have the window that spans over the array.

[int, int, int, ..., int, int, int]
 ^left                              ^right

Then we get the middle of it. The second constraint can determine the other parition as well at this point.
Basically, we want as much items to get to the index of the median.

[int, int, int, ..., int | int, .., int, int, int]          [int, int, ..., int, int]
 ^left                   ^mid                      ^right  ^  ^    ^         ^    ^   ^  the other partitions is somewhere

> mid = (right - left) // 2, representing the index of the first value in the right window.
> denote k as the index of the half point.
> if mid - left < k + 1, then we want `k + 1 - (mid - left)` items from the other array.
> if mid - left == k + 1, then we don' want any items from the other array.
> if mid - left > k + 1, then we want to binary search on this window.

if max(items of the left windows) <= min(items of the right windows), then that is a proper partition.
if the last item of left hand in the first array > the first item of the right hand in the second array, then right = mid - 1.
if the last item of left hand in the second array > the first item of the right hand in the first array, then left = mid + 1.
