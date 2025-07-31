## ステップ1

**例1**
s: ace
   ^ 
t: abcde
   ^

sのポインタが指す文字「a」が与えられたとき、tのポインタがいずれかの時点で「a」を取得するかを評価します。
この場合、「a」を取得します。したがって、sのポインタを前に進めて「c」を取得します。tのポインタが「c」を取得するまでtを走査し、インデックス2でそれを取得します。
今度はsのポインタから「e」を取得し、「e」を取得するまでtを走査します。これはインデックス4になります。sの最初から最後まですべてを走査したので、Trueを返します。

**例2**
s: bae
   ^
t: abcde
   ^

同様に、sのポインタから「b」を取得し、tのインデックス1でそれを取得します。しかし、sの次の文字「a」はtのインデックス1以降では見つかりません。
したがって、tの最後に到達したためFalseを返します。

## step2.py

コードは十分シンプルなので（少なくとも私にとっては）、リファクタリングの余地はないと思いました。
`s_at`と`t_at`という変数を作成するのはやりすぎだと主張する人もいるかもしれませんが、私にとってこれらは変数になるのに十分重要な値です。
または、これらの変数の命名がもっと良いかもしれません。しかし、今のところもっと良いものは思いつきません。

# step3.py

6分半ほどで終了しました。

## step1

**Example 1**
s: ace
   ^ 
t: abcde
   ^

Given pointer at s points at the character "a", evaluate if at any point pointer at t gets "a".
In this case, we get "a". Therefore, move the pointer at s forward, and get "c". Traverse t until pointer at t gets "c" and we get it at the index of 2.
Now we get "e" from the pointer at s, traverse t until we get "e", which will be at the index 4. Because we have traveled all the way from the beginning and the end of s, return True.

**Example 2**
s: bae
   ^
t: abcde
   ^

Likewise, we get "b" from the pointer at s, and we get that at the index of 1 in t. However, the next character in s "a" cannot be found in t after the index of 1.
Therefore, we return False, as we reach to the end of t.

## step2.py

I thought there was no room for refactor, as the code is simple enough (at least to me).
I can assume some might argue that creating variables `s_at` and `t_at` is too much but to me these are prominent values enough to become varibales.
Or naming of these variables could be better. However I don't come up with better ones on top of my head right now.

# step3.py

I finished in 6 minutes and a half or so. 

