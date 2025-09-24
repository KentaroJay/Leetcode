## ステップ1

最初のアイデア：
配列内のゼロの数を追跡するカウンターを設定し、
代替配列（`moved_array`として示される）を設定し、
与えられた配列をループし、0を取得したらカウンターをインクリメントし、
他の値を取得したら`moved_array`に追加し、
ループの後、カウンターの値と同じ数のゼロを追加する。

これは問題設定の要件に準拠していない。

2番目のアイデア：
配列をループし、0を取得したら配列からポップし、
その後の要素を左にシフトして、最後に配置する。

このアプローチは最悪の場合O(n^2)かかるため最適ではない。
nは配列の長さ。

* 実験

[0,1,0,3,12]
 ^ 値が0の場合、右側の左端の非ゼロ値を探して
   それらを交換する
[1,0,0,3,12]
   ^
[1,3,0,0,12]
     ^
[1,3,12,0,0]
        ^ 隣接がなくなったら終了

この方法では、計算量は最良のシナリオでO(n)となり、
最悪のシナリオでO(n*d)未満となる。dはゼロの位置から
左端の非ゼロ値までの平均距離。

## ステップ2

step1からの段階的な最適化のために[これ](https://github.com/fhiyo/leetcode/pull/54/files/40f6172e4c7a6b29303a6b66464dd512300ac477#diff-2f8b85074aa38861aa9dd6fbe0c5f1b540a06f8618d7552b4ffd05da21f795d3R138)
からインスピレーションを受けた。

参照した他の解決策：

- https://github.com/fhiyo/leetcode/pull/54
  アイデア：非ゼロが現れたら、まだ影響を受けていないポイントを上書きする

  ```python
  class Solution:
      def moveZeroes(self, nums: List[int]) -> None:
          last_nonzero_index = 0 # overwritable_indexなどの方が良い命名だと思う
          for num in nums:
              if num == 0:
                  continue
              nums[last_nonzero_index] = num
              last_nonzero_index += 1
          for i in range(last_nonzero_index, len(nums)):
              nums[i] = 0
  ```

  アイデア：ゼロ値がないことを保証できる部分を定義し、
  その部分の外側にゼロ値がなくなるまで拡張し続ける。

  ```python
  class Solution:
      def moveZeroes(self, nums: List[int]) -> None:
          def find_leftmost_index_by(condition: Callable[[int], bool], start: int):
              i = start
              while i < len(nums) and not condition(nums[i]):
                  i += 1
              return i

          next_nonzero_index = -1
          last_nonzero_index = 0 # nums[:last_nonzero_index]のすべての要素は0ではない
          while True:
              last_nonzero_index = find_leftmost_index_by(lambda x: x == 0, last_nonzero_index)
              next_nonzero_index = find_leftmost_index_by(lambda x: x != 0, max(next_nonzero_index, last_nonzero_index))
              if next_nonzero_index == len(nums):
                  break
              nums[last_nonzero_index], nums[next_nonzero_index] = nums[next_nonzero_index], nums[last_nonzero_index]
              last_nonzero_index += 1
  ```

  その他
  ジェネレーターの使用：基本的なアイデアは上記と同じ

  ```python
  class Solution:
      def moveZeroes(self, nums: List[int]) -> None:
          eq0 = (i for i, x in enumerate(nums) if x == 0)
          neq0 = (i for i, x in enumerate(nums) if x != 0)
          while (pos0 := next(eq0, len(nums))) < len(nums): # == 0のアイテムを取得
              while (posn0 := next(neq0, pos0)) < pos0: # != 0のアイテムを取得
                  pass
              nums[pos0], nums[posn0] = nums[posn0], nums[pos0]
  ```

- https://github.com/shining-ai/leetcode/pull/54/files
  アイデア：非ゼロが現れたら、まだ影響を受けていないポイントを上書きする

  ```python
  class Solution:
      def moveZeroes(self, nums: List[int]) -> None:
          first_zero_index = 0
          for i in range(len(nums)):
              if nums[i] == 0:
                  continue
              nums[first_zero_index], nums[i] = (nums[i], nums[first_zero_index])
              first_zero_index += 1
  ```

上記のコードに基づいて、`step2-alt.py`を実装した。

## ステップ3

問題を解くのに2分かかった

---

## step1

First idea:
set a counter to keep track of the number of zeros in the array,
set an alternative array(denoted as `moved_array`),
loop over the given array in which if you get 0, increment the counter,
and if you get other values, append them to `moved_array`,
after the loop, append as many zeros as the value of the counter.

This does not comply with the requirement of the problem settings.

Second idea:
loop over the array, in which if you get 0, pop it out of the array
and shift the elements after it to the left, placing it to the end.

This approach is not optimal since in the worst case it will take O(n^2),
n being the length of the array.

* Experiment

[0,1,0,3,12]
 ^ if the value is 0, look for left-most non-zero value on the right side
   and swap them
[1,0,0,3,12]
   ^
[1,3,0,0,12]
     ^
[1,3,12,0,0]
        ^ finish if there is no more neighbor

In this way, computational complexity takes O(n) in the best scenario
and less than O(n*d) in the worst scenario, d being the average distance
from the point of zero to the left-most non-zero value.

## step2

Took an inspiration from [this](https://github.com/fhiyo/leetcode/pull/54/files/40f6172e4c7a6b29303a6b66464dd512300ac477#diff-2f8b85074aa38861aa9dd6fbe0c5f1b540a06f8618d7552b4ffd05da21f795d3R138)
 for an incremental optimazation from step1.

Other solutions I referrenced:

- https://github.com/fhiyo/leetcode/pull/54
  Idea: If non-zero appears overwrite the point that hasn't been affected
  
  ```python
  class Solution:
      def moveZeroes(self, nums: List[int]) -> None:
          last_nonzero_index = 0 # I think overwritable_index or something is better naming
          for num in nums:
              if num == 0:
                  continue
              nums[last_nonzero_index] = num
              last_nonzero_index += 1
          for i in range(last_nonzero_index, len(nums)):
              nums[i] = 0
  ```

  Idea: define the part you can guarantee there is no zero values
  and keep expanding it until there is no more zero value out side the part.

  ```python
  class Solution:
      def moveZeroes(self, nums: List[int]) -> None: 
          def find_leftmost_index_by(condition: Callable[[int], bool], start: int):
              i = start 
              while i < len(nums) and not condition(nums[i]):
                  i += 1
              return i
          
          next_nonzero_index = -1
          last_nonzero_index = 0 # any elements in nums[:last_nonzero_index] are not 0
          while True:
              last_nonzero_index = find_leftmost_index_by(lambda x: x == 0, last_nonzero_index)
              next_nonzero_index = find_leftmost_index_by(lambda x: x != 0, max(next_nonzero_index, last_nonzero_index))
              if next_nonzero_index == len(nums):
                  break
              nums[last_nonzero_index], nums[next_nonzero_index] = nums[next_nonzero_index], nums[last_nonzero_index]
              last_nonzero_index += 1
  ```
  
  Miscellaneous
  Using generators: Basic idea is the same as above

  ```python
  class Solution:
      def moveZeroes(self, nums: List[int]) -> None:
          eq0 = (i for i, x in enumerate(nums) if x == 0)
          neq0 = (i for i, x in enumerate(nums) if x != 0)
          while (pos0 := next(eq0, len(nums))) < len(nums): # fetch such item that == 0
              while (posn0 := next(neq0, pos0)) < pos0: # fetch such item that != 0
                  pass
              nums[pos0], nums[posn0] = nums[posn0], nums[pos0]
  ```

- https://github.com/shining-ai/leetcode/pull/54/files
  Idea:  If non-zero appears overwrite the point that hasn't been affected

  ```python
  class Solution:
      def moveZeroes(self, nums: List[int]) -> None:
          first_zero_index = 0
          for i in range(len(nums)):
              if nums[i] == 0:
                  continue
              nums[first_zero_index], nums[i] = (nums[i], nums[first_zero_index])
              first_zero_index += 1
  ```

Basing on the code above, I implemented `step2-alt.py`.

## step3

I took 2 mins to solve the problem
