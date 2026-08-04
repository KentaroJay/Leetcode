## ステップ1

* 実験

配列: [1,2,3]

1. 末尾から一つ前を見る: 2
2. 現在位置より後で、2より大きい最小値を探す
3. 3がヒット、それらを交換

配列: [1,2,4,3] -> [1,3,2,4]

1. 末尾から一つ前を見る: 4
2. 現在位置より後で、4より大きい最小値を探す
3. ヒットなし
4. 左に移動: 2
5. 2と同じ操作をして3を取得、それらを交換 [1,3,4,2]
6. 右に移動: 4
7. 現在位置より後で、4より小さい最小値を探す
8. 2がヒット、それらを交換

気づき:

1. 現在位置より前の整数を置き換えると、辞書順で下がる
2. 現在位置より後の整数を置き換えると、辞書順で上がる

* もう一つの実験

[1,2,3,4,5,6,7,8,9]
[1,2,3,4,5,6,7,9,8]
[1,2,3,4,5,6,8,7,9]
[1,2,3,4,5,6,8,9,7]
[1,2,3,4,5,6,9,7,8]
[1,2,3,4,5,6,9,8,7]
[1,2,3,4,5,7,6,8,9]

* 一般化

末尾から一つ前 = n-1番目から開始

1. 現在のインデックスより後で、現在の値より大きい最小値を探す
2. 見つからない場合、一つ左に移動して1を繰り返す
3. 見つかった場合、それらを交換
    1. 右に移動
    2. 現在のインデックスより後の最小値を探す
    3. 見つからない場合、終了
    4. 見つかった場合、交換して3.1を繰り返す

* 他のアプローチを参照

- https://github.com/shining-ai/leetcode/pull/58/files
- https://github.com/SuperHotDogCat/coding-interview/pull/8/files
- https://en.cppreference.com/w/cpp/algorithm/next_permutation.html

操作3.1-3.4は単純なソートであることに気づいた。基本的には3を実行する位置を見つけるだけ。

## ステップ2

高速化のため、サイズが1の場合はnumsを返すことができる。

```python
return nums.reverse()
```

この部分はPython初心者にとって誤解を招く可能性があると思った。
逆順の配列を返すという考えを導入するかもしれないため。

```python
nums.reverse()
return
```

この部分を分離することで、reverseメソッドが配列`nums`を
破壊的に逆順にすることが理解できる。

```python
array[indx_h:indx_t].reverse()
```

この操作はスライスされた配列をインプレースで逆順にしないことを学んだ。
どうやら、[スライスは元の配列のコピーを作成する](https://docs.python.org/3/library/copy.html#:~:text=Shallow%20copies%20of%20dictionaries%20can%20be%20made%20using%20dict.copy()%2C%20and%20of%20lists%20by%20assigning%20a%20slice%20of%20the%20entire%20list%2C%20for%20example%2C%20copied_list%20%3D%20original_list%5B%3A%5D.)。

## ステップ3

6分18秒で問題を解決した。

---

## step1

* Experiment

arr: [1,2,3]

1. Look up the one before the end: 2
2. Loou for the value minimum larger than 2 after the current pos
3. 3 hits, swap them

arr: [1,2,4,3] -> [1,3,2,4]

1. Look at the one before the end: 4
2. Look for the value minimum larger than 4 after the current pos
3. Nothing hits
4. Moving on to the left: 2
5. Same as 2. and you get 3, swap them [1,3,4,2]
6. Moving on the the right: 4
7. Look for the value minimum smaller than 4 after the current pos
8. 2 hits, swap them

Realizaion:

1. If you replace the integer behind where you are, you are goinng down
lexicographically.
2. If you replcae the integer after where you are, you are going up
lexicographically.

* Another Experiment

[1,2,3,4,5,6,7,8,9]
[1,2,3,4,5,6,7,9,8]
[1,2,3,4,5,6,8,7,9]
[1,2,3,4,5,6,8,9,7]
[1,2,3,4,5,6,9,7,8]
[1,2,3,4,5,6,9,8,7]
[1,2,3,4,5,7,6,8,9]

* Generalization

start from the one before the end = n-1th

1. look for a value that's minimal larger than the current val
after the current index
2. If not found, move one to the left and repeat 1
3. If found, swap them
    1. move to the right
    2. look for the minimum val after the current index
    3. If not found, finish
    4. If found, swap and repeat 3.1

* Referring to other approaches

- https://github.com/shining-ai/leetcode/pull/58/files
- https://github.com/SuperHotDogCat/coding-interview/pull/8/files
- https://en.cppreference.com/w/cpp/algorithm/next_permutation.html

I realized the operation 3.1 - 3.4 is just a simple sorting. Basically you just
find the position to execute 3.

## step2

I can return nums when the size of it is 1 in order to make it faster.

```python
return nums.reverse()
```

I thought this part might be misleading for Python beginners,
as it may introduce an idea that this is returning the reversed array.

```python
nums.reverse()
return
```

By separating this part, you can understand that the reverse method
distructively reverses the array `nums`.

```python
array[indx_h:indx_t].reverse()
```

I learned that this operation does not reverse the sliced array in-place.
Apparently, [slicing creates a copy of the original array](https://docs.python.org/3/library/copy.html#:~:text=Shallow%20copies%20of%20dictionaries%20can%20be%20made%20using%20dict.copy()%2C%20and%20of%20lists%20by%20assigning%20a%20slice%20of%20the%20entire%20list%2C%20for%20example%2C%20copied_list%20%3D%20original_list%5B%3A%5D.).

## step3

I solved the problem in 6 mins 18 secs.
