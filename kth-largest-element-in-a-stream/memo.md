## ステップ1

k番目に大きい値を追跡するためにヒープを使うことを考えました
（後で他の人のコードを見たときに、マップを使う方がより自然な方法だとわかりました）。

基本的に、初期化時に与えられたすべてのnumsをヒープに入れてから
不要なアイテムを削除し、その後`add`メソッドがヒープへのポップとプッシュを
処理します。

ストリームから不要なアイテムを削除することについては、
`__init__`メソッド内で行うのが自然だと思いました。
しかし、後で`add`メソッドを呼び出すだけでコードの複雑さが
減ることに気づきました。

## ステップ2

**改善点**

1. `__init__`メソッド内で`add`メソッドを呼び出す。
2. `add`メソッド内で`heappush`を1回呼び出す。
3. `add`メソッド内で`self.stream[0]`を1回呼び出す。

また、[こちら](https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0)のコードも参考にしました。

いくつかの解答にはヒープの実装が含まれていましたが、今回はそれをしないことにしました。

## ステップ3

2分で完了しました。

---

## step1

I thought about using heap to keep track of kth largest value
(which turned out later on when I was looking at other people's code that map 
would be more natural way).

Basically, put all the given nums into the heap at initialization before 
removing unnecessary items, and then `add` method would handle pop and push
to the heap.

As for removing unnecessary items from the stream,
doing such inside `__init__` method would be natural, I thought. 
However, later on I realized just calling `add` method decreases
code complexity.

## step2

**Improvements**

1. call `add` method inside `__init__` method.
2. call `heappush` once in `add` method.
3. call `self.stream[0]` once in `add` method.

I also referred to code from
[here](https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0).

Some solutions included implementations of heap, but I decided not to do it this time.

## step3

Finished in 2 mins.
