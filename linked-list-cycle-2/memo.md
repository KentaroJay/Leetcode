## ステップ1

最初のアイデアは、各インデックスのノードを追跡するための辞書を持つことでした。辞書内のノードと一致するノードを取得したら、それに関連付けられたインデックスを返します。時間計算量はO(n)、メモリ空間はO(n)です。これは定数メモリ空間を満たしません。

定数メモリ空間を実現するために、以前と同様にfast/slowポインタを活用する必要があると思います。

~ . . . . . (.) . .
      ^-----------|

(.)をslowポインタとfastポインタが出会う場所と考え、Mと表記します。
2つのポインタが出会ったとき、それがループを開始する正確なノードであることを意味しないことに注意してください。
5分間進展できなかったので、以下を見ました：
- https://github.com/katsukii/leetcode/pull/13/files#r1934759094
- https://github.com/pineappleYogurt/leetCode/pull/3

このソリューションはO(1)のメモリ空間を使用するため、これを採用します。

## ステップ2

反復ロジックをジェネレータに隠すことを考えました。しかし、今回はネストされたループがあります。そのため、ジェネレータは別のロジックを持つことになり、このコードの可読性が低下します。

`from_head`と`from_collision`という名前付けが好きですが、異論がある人もいるかもしれません。
今回はコードをそのままにしておきます。

## ステップ3

4分で終了しました。

## 備考

O(1)メモリ空間でソリューションを思いつくのは非常に困難でした。しかし、以前に参照したGitHubコメントで議論されたことによると、自然言語でソリューションを理解し、コードを説明できることは、アイデアを思いつくことよりも重要です。

---

## step1

Initial idea is to have a dict to keep track of nodes at each index. When we get a node that matches with one from the dict then return the index associated with it. Time complexity is O(n), memory space is O(n). This does not satisfy constant memory space.

In order to achieve constant memory space, I think I need to leverage fast/slow pointer as before.

~ . . . . . (.) . .
      ^-----------|

Let's consider (.) is where the slow and the fast pointer meets, denoted as M.
Note that when two pointers meet, that does not mean it's the exact node that starts the loop.
I couldn't progress for 5 mins so I took a look at:
- https://github.com/katsukii/leetcode/pull/13/files#r1934759094
- https://github.com/pineappleYogurt/leetCode/pull/3

This solution takes O(1) memory space, so I will adopt this one.

## step2

I thought about hiding the iteration logic in a generator. However, this time I have nested loop. So the generator will have another logic which will diminish the readability of this code.

I like naming `from_head` and `from_collision` but some might argue otherwise.
This time I keep the code as it is.

## step3

I finished in 4 mins.

## Remark

It was extremely hard to come up with the solution with O(1) memory space. However, according to what was discussed in the earlier referred GitHub comments, understanding the solution in natural language and being able to explain the code is more important than coming up with the idea.
