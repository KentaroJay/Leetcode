## ステップ1

問題の理解：
`s`をセグメントに分割し、すべてのセグメントが単語辞書`wordDict`に存在する場合はTrueを返し、そうでない場合はFalseを返す。

**アイデア1**

前のセグメントの後に文字を蓄積する。各ステップで、文字のセットを`wordDict`のアイテムと比較する。一致するアイテムがある場合は、セットをリセットして前進する。
`s`の終わりに達した後、セットにアイテムがない場合はTrueを返す。それ以外の場合はFalseを返す。

**考察**
`s`が"leetcode"で`wordDict`が["leet", "leetc", "ode"]の場合を考えている。異なるシナリオを考慮する必要がある。
このアイデアではFalseを返すことになる。改善が必要。

5分間止まってしまったので、解決策を見た：https://github.com/hayashi-ay/leetcode/pull/61/files

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def can_split(index):
            if index == len(s):
                return True
            for word in wordDict:
                if s[index:index + len(word)] != word:
                    continue
                if can_split(index + len(word)):
                    return True
            return False
        
        return can_split(0)
```

この解決策は複数のシナリオを考慮したものだ。

**この解決策の基本的なアイデア**
状態i：`s`のi番目の位置
    - 任意の前の状態が状態iに到達できる
    - `wordDict`内のすべての可能な一致アイテムをチェック
    - iが`s`の終わりの場合、Trueを返す


もう一つの解決策は最初のものほど理解しやすくない。

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        can_split = [False] * (len(s) + 1)
        can_split[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if i + len(word) > len(s):
                    continue
                if can_split[i + len(word)] and s[i: i + len(word)] == word:
                    can_split[i] = True
                    break
        return can_split[0]
```

今回は最初のDP解決策を選ぶ。
時間計算量：
- n個の可能な状態がある（nはlen(s)）
- 各状態でm個のアイテムをすべて反復する（mはlen(wordDict)）
- sから単語をスライスするのにLかかる（Lは平均単語長）

したがってO(nmL)

## ステップ2

`index + len(word)`は変数にすべきかもしれない？

## ステップ3

4分21秒で終了した。

---

## step1

My understanding of the problem is:
Divide the `s` into segments, return True if all of the segments exist in the word dictionary `wordDict`, return False otherwise.

**Idea 1**

accumulate characters after the previous segment. and at each step compare the set of characters with the items in `wordDict`. If there is a matching item, reset the set, and move forward.
After reaching to the end of `s`, if there's no item in the set, return True. Return False otherwise.

**Thought**
I am thinking of a case where `s` is "leetcode" and `wordDict` is ["leet", "leetc", "ode"]. We need to take different scinarios into consideration.
With the idea, it would return False. It needs improvement.

I stopped for 5 mins so took a look at solutions: https://github.com/hayashi-ay/leetcode/pull/61/files

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def can_split(index):
            if index == len(s):
                return True
            for word in wordDict:
                if s[index:index + len(word)] != word:
                    continue
                if can_split(index + len(word)):
                    return True
            return False
        
        return can_split(0)
```

This solution is the one takes multiple scinarios into consideration.

**Basic idea of this soluion**
state i: ith position of `s`
    - any previous states can reach state i.
    - check all possible matching item in `wordDict`
    - if i is the end of `s`, return True.


Another type of solution is not as easy to understand as the first one.

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        can_split = [False] * (len(s) + 1)
        can_split[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if i + len(word) > len(s):
                    continue
                if can_split[i + len(word)] and s[i: i + len(word)] == word:
                    can_split[i] = True
                    break
        return can_split[0]
```

This time I am choosing the first DP solution.
Time complexity:
- There are n possible states, n being as len(s).
- Iterating through all the m items at each state, m being as len(wordDict).
- Slicing a word from s takes L, where L is the average word length.

Therefore it's O(nmL)

## step2

Maybe `index + len(word)` should be a variable?

## step3

I finished in 4 mins 21 seconds.
