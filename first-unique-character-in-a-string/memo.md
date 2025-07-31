## 日本語訳

### 問題の説明
文字列sが与えられたとき、その中で最初に現れる繰り返しのない文字を見つけ、そのインデックスを返します。存在しない場合は-1を返します。

例1:
入力: s = "leetcode"
出力: 0
説明: インデックス0の文字'l'は、他のインデックスに現れない最初の文字です。

例2:
入力: s = "loveleetcode"
出力: 2

例3:
入力: s = "aabb"
出力: -1

### ステップ1
以下のような辞書を考えます：
{キー: 値} | キー = 文字、値 = [文字の出現インデックス]

与えられた文字列をループする中で、このような辞書を定義できます。
ループの後、値のサイズが1のペアを抽出します。最小のインデックスを返すことができます。

ループはO(n)、最小インデックスの検索はO(n)です。合計の実行時間の空間計算量はO(n)です。

別のアイデアとして、与えられた文字列と同じサイズの配列を0で初期化し、辞書を用意します。キーは文字、値は最初の出現インデックスです。
文字列を反復処理する際：
- 辞書に既にキーがあるかチェックします。
  - 肯定的な場合、辞書に格納されたインデックスが指す配列の値を増加させます。
  - 否定的な場合、与えられた文字列の現在のインデックスに対応する配列の値を増加させ、辞書に新しい項目を追加します。

反復の後、配列を通過して値が1に等しい最初のインデックスを返します。

配列の作成はO(n)、ループはO(n)、もう一つのループもO(n)です。したがって、合計の実行時間の空間計算量はO(n)です。

全体的に、2番目の実装は分かりやすいと思います。

### ステップ2
他の人の解答を見ました。文字とその出現回数のマッピングを作成し、後で与えられた文字列をループしながら出現回数を調べるだけで良いことがわかりました。

代替案として、LRUキャッシュを活用し、与えられた文字列で一度だけ現れた文字のみを追跡することができます。この解答は2回目のループ反復を含まないので、この解答を2番目のステップ2として採用したいと思います。

Nodeデータクラスにカウンターを持つことは冗長だと思いました。文字が一度だけ現れたか、それ以上現れたかだけを気にするからです。したがって、Nodeからカウンターを削除します。

### ステップ3
わずかな変更を加え、Node構造のprevとnextをそれぞれprev_nodeとnext_nodeに名前を変更しました。これは、Pythonには`next()`というイテレータ用の関数があり、コードリーダーを混乱させる可能性があるためです。

---

## Problem Description
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

```
Example 1:

Input: s = "leetcode"

Output: 0

Explanation:

The character 'l' at index 0 is the first character that does not occur at any other index.
```

```
Example 2:

Input: s = "loveleetcode"

Output: 2
```

```
Example 3:

Input: s = "aabb"

Output: -1
```

## Step1
Think of a dictionary like below:
```
{key: value} | key = character, value = [index of the character occurence]
```
We can define such dictionary during the loop over the given string.
After the loop, extract pairs with the size of 1 in the value. We can return the smallest index.

The loop is O(n), finding the smallest index takes O(n). The total rutime space complexity is O(n).

Another idea is to have an array of same size of the given string, initialized with 0, and a dictionary; key being the character and value being the index of its first occurence.
While iterating through the string:
- Check if there's already a key in the dictionary.
    - If positive, increment the value in the array that the stored index in the dictionary points at.
    - If negative, increment the value in the array that corresponds to the current index of the given string, and put a new item in the dictionary.

After the interation, you can go through the array and return the first index when the value equals to 1.

Creation of the array is O(n), the loop is O(n), another loop is also O(n). Therefore, the total runtime space complexity is O(n).

Overall, I think the second implementation is straighforward.

## Step2
I took a look at others' solutions. It turns out I could just create a mapping between a character and its occurence, later on looking up the occurence while looping through the given string.

Alternatively, you can leverage LRUcache, tracking only characters that appered once in the given string. This solution doesn't involve second loop iteration, so I'd like to adopt this solution as the second step2.

I thought having counter in Node data class was redundant, as we only care if the character appeared only once or more. Therefore eliminating the counter from Node

## step3

I made a slight change, renaming prev and next on Node structure to prev_node and next_node respectively. This is because in Python we have the function for interator called `next()`, which might confuse the code reader.
