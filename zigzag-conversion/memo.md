# 日本語訳

## 問題の説明
文字列「PAYPALISHIRING」が指定された行数でジグザグパターンで書かれます（可読性を高めるため、固定幅フォントで表示することをお勧めします）：

> P   A   H   N
> A P L S I I G
> Y   I   R

そして行ごとに読みます：「PAHNAPLSIIGYIR」

文字列と行数を受け取って、この変換を行うコードを書いてください：

> string convert(string s, int numRows);

## 感想

numRows = 3の場合、最初の行に入る文字はインデックス0、4、8、12、...、4*i（i=0、1、2、...）です。
2行目はインデックス1、3、5、7、...、1 + 2*i。
3行目はインデックス2、6、10、14、...、2 + 4*i。

numRows = 4の場合、最初の行は...

文字をどの行に配置するかを表すポインタを考えることができます。与えられた文字を進めながらポインタを移動させます。

ポインタは0、1、2、...、numRows - 1の間を行ったり来たりする必要があります。

## ステップ1

メソッドは`direction`の状態を追跡し、与えられた文字列に文字を配置するためのインデックスをシフトします。

## ステップ2

評価前に`current_row + direction`を計算することが少し複雑になると思いました。そこで、その部分をメソッドの最後に移動しました。
`numRows - 1`を`last_row_idx`などと名付けることを考えましたが、やりませんでした（やるべきでした）。
`numRows`が1の場合のエッジケースは全く思い浮かばなかったので、LeetCodeでエラーが出た後にこの部分を追加しました。

```Python
if numRows == 1:
    return 0
```

## ステップ3

今回は`numRows - 1`を`last_row_idx`と名付けました。

---

# Original English Content

## Problem Description
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

> P   A   H   N
> A P L S I I G
> Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

> string convert(string s, int numRows);

## Impression

If numRows = 3, characters that goes in the first line is index 0, 4, 8, 12, ..., 4*i (i=0, 1, 2, ...).
The second line is index 1, 3, 5, 7, ..., 1 + 2*i.
The third line is index 2, 6, 10, 14, ..., 2 + 4*i.

If numRows = 4, the first line is ...

We can think of a pointer to represent in which line the character should be placed. Move the pointer as we go through the given characters.

The pointer should go back and forth between 0, 1, 2, ..., numRows - 1.

## step1

The method keeps track of the state `direction` and shift the index to put characters in the given string.

## step2

I thought calculating `current_row + direction` before evaluation makes it a bit complex. So I brought the part to the bottom of the method.
I thought about naming `numRows - 1` as `last_row_idx` or something but I didn't(I should have done that).
The edge case of `numRows` being 1 completely didn't come up to my mind so added this part after I got an error on LeetCode.

```Python
if numRows == 1:
    return 0
```

## step3

This time I named `numRows - 1` as `last_row_idx`.
