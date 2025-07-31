# 日本語訳

## ステップ1

私はPythonを使用しているので、int型は32ビットを超える数値を扱えますが、より厳格な型システムを持つ他の言語ではどのように扱う必要があるか疑問に思いました。
（文脈は変わりますが、興味があったので）Pythonで2 ** 1000を計算する実験をしたところ、エラーが発生しました。

```
TypeError: Integer exceeds 64-bit range
Line 203 in _serialize (./python3/__serializer__.py)
```

シリアライザーライブラリには64ビット整数の制限があると推測しています。

返す整数を追跡するために`answer`変数を持つことを考えており、デフォルトで0に設定されています。また、`sign`変数は-1または1を保持し、デフォルトで1に設定されています。
最後に`answer` * `sign`を掛けます。`answer`はデフォルトで0に設定されているためです。→後で、これは間違いだと気づきました。`sign`は`s[i]`と掛け合わせるべきです。

各反復で、数字文字を取得していると仮定して、`answer *= 10`を実行した後に`answer += s[i]`を実行します。→これは`answer += sign * s[i]`であるべきです。

他の人の解決策を見てみましたが、上記とほぼ同じことをしているようでした。

## ステップ2

先頭の0をチェックする部分は必要ないことに気づきました。計算プロセスに含めても結果に影響しないからです。
各変数の宣言を、参照される直前に配置しました。

## ステップ3

最初の試行で9分で完了しました。

---

# Original (English)

## step1

I am using Python so int type can handle numbers over 32bits but I wondered how I have to handle that with other languages that have stricter type system.
I experimented calculating 2 ** 1000 in Python, it raises an error.

```
TypeError: Integer exceeds 64-bit range
Line 203 in _serialize (./python3/__serializer__.py)
```

I am guessing the serializer library has the limitation to 64 bits of integer.

I am thinking about having a variable `answer` to keep track of the integer to return, set to 0 by default. Also `sign` variable either holds -1 or 1, set to 1 by default.
Multiply `answer` * `sign` at the end, since `answer` is set to 0 by default. -> Later on I realized this was mistaken. `sign` should be multipled by with `s[i]`.

Each iteration, assuming I am getting digit character, I do `answer += s[i]` after doing `answer *= 10`. -> This should be `answer += sign * s[i]`.

I took a look at other peoples' solutions but seemed like they did almost the same as above.

## step2

I noticed that I didn't need the part that's checking leading 0, since even if we took it into our calculation process, it wouldn't hurt the result.
I placed the declaration of each variables right before they're referenced.

## step3

I finished in 9 minutes at the first trial.
