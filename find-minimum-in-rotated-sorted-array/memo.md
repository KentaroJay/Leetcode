## ステップ 1

問題文でアルゴリズムの時間計算量を `O(log n)` にするよう求められているため、
解法は二分探索的なアプローチに関係しているはずです。

* 実験

[4,5,6,7,0,1,2]
 ^l    ^mid  ^r

もし `mid` > `r` なら、`l` = `mid`

[4,5,6,7,0,1,2]
       ^l^m  ^r

もし `mid` < `r` なら、`r` = `mid`

[4,5,6,7,0,1,2]
       ^l^r
       ^mid

終了条件：`l` > `r` を満たす隣接する `l` と `r` を見つける。

問題文では配列内のすべての要素が一意であると述べられていますが、
要素が同一の場合についても考えました。

## ステップ 2

### 参考資料

* [https://github.com/thonda28/leetcode/pull/7/files](https://github.com/thonda28/leetcode/pull/7/files)
  * `left, right = -1, len(nums) - 1` の背後にある考え方がわかりません。
  * left より前はすべて配列の大きい部分で、
  right より後はすべて配列の小さい部分であるという考え方は理解できます。
  * しかし、配列が最小値から始まるときに起こる問題を
  `left = -1` を割り当てることでなぜ修正できるのか理解できません。
  （または、`left = 0` に設定したときに問題が発生する場合に、
  `left = -1` に設定するというアイデアをどのように思いつくかがわからないというべきか）
  * インデックス0が大きい部分でないときに `left = 0` に設定するのが
  間違っていることには気づけると思いますが、`left = -1` に設定すれば
  それが修正されることには自分では気づけないと思いました。

  ```python
  class Solution:
      def findMin(self, nums: List[int]) -> int:
          left = 0  # `nums` が最小値から始まる場合にパスしない
          right = len(nums) - 1
          while right - left > 1:
              mid = (left + right) // 2
              if nums[mid] > nums[right]:
                  left = mid
              else:
                  right = mid
          return nums[right]
  ```

* [https://github.com/seal-azarashi/leetcode/pull/39/files](https://github.com/seal-azarashi/leetcode/pull/39/files)
  * `middle` の値を除外できるので、
  `left = middle + 1` とできることに気づきました

全体的に、`left` と `right` の間の範囲が閉区間か開区間かを
考慮していなかったことがわかりました。

また、与えられた配列が空の場合について考えることができませんでした。
そのため、そのためのロジックも追加しました。

その他可能な代替解法：

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            raise ValueError

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= nums[-1]:
                right = mid
            else:
                left = mid + 1
        return nums[left]
```

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            raise ValueError

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[right] < nums[mid]:
                left = mid + 1
                if nums[left] < nums[right]:
                    return nums[left]
            elif nums[mid] < nums[right]:
                right = mid
            else: # nums[mid] == nums[right]
                # 与えられた配列に重複がある
                raise ValueError
        return nums[left]
```

## ステップ3

問題を2分50秒で解きました。

---

## step 1

Since the problem description says to write an algorithm so that its
time complexity is `O(log n)`, the solution must have something to
do with binary search-ish approach.

* Experiment  

[4,5,6,7,0,1,2]
 ^l    ^mid  ^r

if `mid` > `r`, `l` = `mid`

[4,5,6,7,0,1,2]
       ^l^m  ^r

if `mid` < `r`, `r` = `mid`

[4,5,6,7,0,1,2]
       ^l^r
       ^mid

Termination condition: find adjacent `l` and `r` that meets `l` > `r`.

I also thought about, even though the problem description states
that all items in the array are unique, a case where items are identical.

## step 2

### Referrence

* [https://github.com/thonda28/leetcode/pull/7/files](https://github.com/thonda28/leetcode/pull/7/files)
  * I don't know the idea behind `left, right = -1, len(nums) - 1`.
  * I get the idea that
  anything before left is the larger part of the array and
  anything after right is the smaller part of the array.
  * However, I don't understand why assigning `left = -1` fix the
  problem that happens when the array starts with the smallest value.
  (Or I should say how to come up with the idea to set `left = -1`
  when the problem happens if you have set `left = 0`)
  * I think I can notice that setting `left = 0` when index 0 is not
  the larger part is wrong, but I don't think I can notice setting
  `left = -1` would fix it.

  ```python
  class Solution:
      def findMin(self, nums: List[int]) -> int:
          left = 0  # does not pass when `nums` starts with the smallest value
          right = len(nums) - 1
          while right - left > 1:
              mid = (left + right) // 2
              if nums[mid] > nums[right]:
                  left = mid
              else:
                  right = mid
          return nums[right]
  ```

* [https://github.com/seal-azarashi/leetcode/pull/39/files](https://github.com/seal-azarashi/leetcode/pull/39/files)
  * I realized I could do `left = middle + 1`
  since I can exclude the value at `middle`

Overall, I understand that I did not concern about if the range
between `left` and `right` is closed space or open.

Also, I failed to think about when the given array is empty. So I added
a logic for that as well.

Possible alternative solutions are:

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            raise ValueError

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= nums[-1]:
                right = mid
            else:
                left = mid + 1
        return nums[left]
```

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            raise ValueError

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[right] < nums[mid]:
                left = mid + 1
                if nums[left] < nums[right]:
                    return nums[left]
            elif nums[mid] < nums[right]:
                right = mid
            else: # nums[mid] == nums[right]
                # There is a duplication in the given array
                raise ValueError
        return nums[left]
```

## step3

Solved the problem in 2 mins 50 secs.
