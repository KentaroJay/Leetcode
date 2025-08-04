## ステップ1

スタックを作成し、開き括弧の場合は文字を追加し、閉じ括弧の場合はポップして現在の文字と比較する。
コードが最後まで到達したら、trueを返す。

正規表現を使用してもこの問題を解決できると思う。思いつかなかったのでClaudeを使用して実装した。
解決策は、'()'、'[]'、または'{}'のいずれかに一致する部分文字列を削除し続け、最終的に空の文字列になったらTrueを返す。それ以外の場合はFalseを返す。

どちらの方法も良いと思うが、この問題の意図はコーダーがスタックを使用できるかどうかを確認することだと感じる。そのため、最初のロジックを実装する。

問題では入力に括弧のみが含まれることが保証されているが、私の観点から、入力を検証する方が良いと思う。

エラーが発生して、ループ中にスタックが空になる可能性を考慮していなかったことに気づいた。
将来的にこれをキャッチできるようにしたい。ポップするためにはスタックが空であってはならないことに気づくべきだった。


## ステップ2

次のようなデータ構造を使用できる：

```python
class Parenthesis:
    shape: "round" | "square" | "curly"
    type: "open" | "close"
```

後でコード内でshapeデータポイントを比較するだけで済み、コードが短くなる。

Enum比較は`is`または`==`を使用すべきか検索したところ、どちらでも良い https://docs.python.org/3/howto/enum.html#comparisons

`previous`変数に対比して`current`変数と名付けた。



## ステップ3

9分31秒で完了



## 備考

ステップ2では、他の人のコードを見ることをやめてしまったが、次のようなことができたはずだ。

```python
open_to_close = {
    "(":")",
    "{":"}",
    "[":"]"
}
```

上記の辞書を使用すると、現在の文字が開き/閉じ括弧かどうかの判断とスタックから期待される文字の取得を同時に行うことができる。

```python
if char in open_to_close:
    stack.append(char)
```

```python
previous = stack.pop()
if char != open_to_close[previous]:
    return False
```

さらに、センチネルを使用して条件処理を排除できる：

```python
open_to_close = {
    "(":")",
    "{":"}",
    "[":"]",
    "*":""  # または \0
}
```
問題では入力に括弧のみが含まれることが保証されているが、入力文字列に"*"が含まれる場合を考慮して、より広範なケースに対応するために"\0"の方が良いと思う。

```python
if len(stack) == 0:  # もう必要ない
    return False     # もう必要ない 
previous = stack.pop()
```

これは小さな修正だが、次のように書くこともできた：

```python
VALID_CHARS = "()[]{}"
```

また、"(abc)[def]"のような一般的な入力に対しても機能するソリューションを検討すべきだった。私のコードはそのような場合には動作しなくなる。良いことは、私のソリューションは動作しないが、その場合にはエラーをスローすることだ。

---

## step1

Create a stack and append a character if it's an opening parenthesis, pop if it's a closing parenthesis and compare with the current character.
If the code reaches to the end, return true.

I think using regex can also solve the problem. I couldn't come up with the idea so I used claude to do it.
The solution is to keep removing substrings that matches either '()', '[]', or '{}', and if we finally get empty string, return True. Return False otherwise.

I think either way is good, but I feel the intent of the problem is to see if a coder can use stack. So I am going to implement the first logic.

Even though the problem enssures the input only contains parenthesis, from my standpoint, I think it's better to validate the input.

I realized after getting an error that I didn't take into consideration that stack might be empty during the loop.
I want to be able to catch that in the future. I should've noticed the stack should not be empty to pop.

## step2

I can use data structure like this:

```python
class Parenthesis:
    shape: "round" | "square" | "curly"
    type: "open" | "close"
```

Later on in the code we can just compare the shape datapoint, which will shorten the code.

I searched for Enum comparison should be `is` or `==`, both are fine https://docs.python.org/3/howto/enum.html#comparisons

Named `current` variable in contrast to `previous` variable.


## step3

Finished in 9 mins 31 sec


## remark

In the step2, I ended up neglecting seeing other people's code but here's what I could have done.

```python
open_to_close = {
    "(":")",
    "{":"}",
    "[":"]"
}
```

Using the dictionary above, judging if the current character is open/close parenthesis and getting expected character from the stack can be done at the same time.

```python
if char in open_to_close:
    stack.append(char)
```

```python
previous = stack.pop()
if char != open_to_close[previous]:
    return False
```

Additionally, we can use sentinel to eliminate conditional handling:

```python
open_to_close = {
    "(":")",
    "{":"}",
    "[":"]",
    "*":""  # or \0
}
```
Even though the problem ensures the input only contains parenthesis, I think "\0" is better in case the input string contains "*" to be sure for broader cases.

```python
if len(stack) == 0:  # Not neccessary anymore
    return False     # Not neccessary anymore 
previous = stack.pop()
```

This is a small fix but I could have written:

```python
VALID_CHARS = "()[]{}"
```

Also, I should have considered solution that would work for general input such as "(abc)[def]". My code stops working in such cases. Good thing is that my solution will not work, but throws an error in that case.

