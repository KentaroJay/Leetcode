## ステップ1

2つのポインターを使用し、1つは1ノードずつ進み、もう1つは1つ飛ばしで進みます。これらのポインターをそれぞれスローポインターとファストポインターと呼びましょう。
リストが循環している場合、ある時点で2つのポインターが同じノードを指すことが保証されます。次の2つのケースを考えてみてください。

**状態1**

. . .
^   ^
f   s

次のステップでは、

. . . . .
    ^ ^
    f s

最後に、

. . . . .
        ^^
        fs 同じノードを指している

**状態2**

. .
^ ^

これは状態1の第2段階と同じ状態です。

合計30分で完了しました。

## ステップ2

走査ロジックを隠すためにジェネレーターを使用してみました。
ジェネレーターを使用すると明らかに実行時間が遅くなります。
理由1：関数呼び出し、コールスタックに追加の作業が発生します。
理由2：yieldは単純な再代入よりもオーバーヘッド（*1）が大きい。
理由3：タプルのアンパッキング。

*1: https://docs.python.org/3/glossary.html#term-generator-iterator
> 各yieldは処理を一時的に中断し、実行状態（ローカル変数と保留中のtry文を含む）を記憶します。ジェネレーターイテレーターが再開すると、中断したところから再開します（毎回新しく始まる関数とは対照的に）。

## ステップ3

4分36秒で完了しました。

---

## step1

Two pointers, one traverses one node by one, the other traverses by skipping one. Let's call these pointers slow pointer and fast pointer respectively.
If the list is cyclic, it is ensured to have two pointers pointing at the same node at some point. Think about the following two cases.

**state 1**

. . .
^   ^
f   s

In the next step,

. . . . .
    ^ ^
    f s

At last,

. . . . .
        ^^
        fs pointing at the same node

**state 2**

. .
^ ^

It's the same state as the second phase of the state 1.

I finished in 30 mins total.

## step2

I tried using generator to hide traversing logic.
Using generators slows down the ET apparently.
Reason 1: Function call, it adds extra work in the call stack.
Reason 2: yield has more overhead(*1) than a simple reassertion.
Reason 3: tuple unpacking.

*1: https://docs.python.org/3/glossary.html#term-generator-iterator
> Each yield temporarily suspends processing, remembering the execution state (including local variables and pending try-statements). When the generator iterator resumes, it picks up where it left off (in contrast to functions which start fresh on every invocation).

## step3

I finished in 4 mins and 36 seconds.
