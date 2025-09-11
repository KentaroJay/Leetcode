## step1.py

LeetCode Premiumの問題にアクセスできなかったため、類似の[LintCodeの問題](https://www.lintcode.com/problem/847/description)を参照しました。

これは問題を解こうとした際の未完成のコードです。

```python
class Solution:
    """
    @param root: 与えられた木
    @param v: ターゲット値
    @return: 分割後のルートTreeNode
    """
    def split_b_s_t(self, root: TreeNode, v: int) -> TreeNode:
        def recursive_search(node: TreeNode):
            if node.val == v:
                node_right = node.right
                node.val = node_right.val if node_right else None
                node.right = node_right.right if node_right else None
                node.left = node_right.left if node_right else None
                return root
            if node.val > v:
                if node.left:
                    return recursive_search(node.left)
                return node
            if node.right and node.right.val > v:
                return node.right
            if node.right:
                return recursive_search(node.right)
            return None
```

解答を見ずには問題を解くことができませんでした。
- https://github.com/hayashi-ay/leetcode/pull/53/files
- https://github.com/goto-untrapped/Arai60/pull/54/files
- https://github.com/shining-ai/leetcode/pull/47
- https://github.com/Mike0121/LeetCode/pull/16/files

（後で気づいたのですが、戻り値がLeetCodeとは異なっていました。
そのため、自分の解答を検証することができませんでした。他の人の解答と比較するだけでした。）

どうやら、この問題を解く方法は2つあるようです：BFSまたはDFS。
DFSの方がはるかに簡単に見えます。しかし、学習のためにstep2でBFSを実装してみたいと思います。

## step2

私の観点からすると、step1.pyにはあまりやることがありませんでした。
BFS部分を実装します。

BFSを使ってこの問題をどう解くべきか分からなかったので、Claudeに@bfs_solution.pyで解いてもらいました。しかし、その解答はDFSよりもはるかに難しく見えます。
このシナリオでBFSが直感的でないことを考えれば、それは自然なことです。

DFSに戻って、早期リターンを使わず、代わりに`else`句を使って
この[コードが対称的である](https://github.com/Mike0121/LeetCode/pull/16/files#r1605978794)ことを暗黙的に示そうとしました。

## step3

3分で問題を解きました
（時計を始めるのを忘れたので確かではありませんが、おおよそ正しいです）

---

## step1.py

I didn't have an access to the LeetCode Premium problems so I referred to the
similar [LintCode problem](https://www.lintcode.com/problem/847/description).

This was the unfinished code in an attempt to solve the problem.

```python
class Solution:
    """
    @param root: the given tree
    @param v: the target value
    @return: the root TreeNode after splitting
    """
    def split_b_s_t(self, root: TreeNode, v: int) -> TreeNode:
        def recursive_search(node: TreeNode):
            if node.val == v:
                node_right = node.right
                node.val = node_right.val if node_right else None
                node.right = node_right.right if node_right else None
                node.left = node_right.left if node_right else None
                return root
            if node.val > v:
                if node.left:
                    return recursive_search(node.left)
                return node
            if node.right and node.right.val > v:
                return node.right
            if node.right:
                return recursive_search(node.right)
            return None
```

I couldn't solve the problem without looking at the answer.
- https://github.com/hayashi-ay/leetcode/pull/53/files
- https://github.com/goto-untrapped/Arai60/pull/54/files
- https://github.com/shining-ai/leetcode/pull/47
- https://github.com/Mike0121/LeetCode/pull/16/files

(Later on, I realized that the returning value is different from that of LeetCode.
So I couldn't verify my solution. I just compared the solution from other people.)

Apparently, there are two ways to solve this question: BFS or DFS.
DFS looks a lot more easier than the other. However I would like to implement BFS for 
my learning at the step2.

## step2

There was not much thing to do to step1.py from my point of view. 
Implementing BFS part.

I did not know how I could solve the problem using BFS so I let Claude do it for 
me @bfs_solution.py. However, the solution looks a lot more difficult than DFS.
That's natural since BFS in this senario is not ituitive at all.

Getting back with DFS, I tried not using early return and instead using the `else` clause
to implicitly imply this [code is symmetrical](https://github.com/Mike0121/LeetCode/pull/16/files#r1605978794).

## step3

I solved the problem in 3 mins
(not sure since I forgot to start the clock but more or less correct)
