## step1

n pairs = n left parenthesis and n right parenthesis. Let's call nl and nr respectively.

- When nl < nr, you can either chose to append left parenthesis or right parenthesis.
- When nl >= nr, you can only append left parenthesis.

Starting from an empty string, use depth first search to generate
a set of valid parentheses.

I used an array of strings so every append operation does not take up O(n),
since string is immutable and creates copy each time.

I struggled to name `parentheses` and `generatedParentheses` varibles. I should
have at least named them in the reversed order, because then logner length variable
`generatedParentheses` would be repeated less.

## step2

Generally, I can do:

- `a == 0 and b == 0` should be `a == b == 0`.

This time I used array join to reduce string copy, but this operation is not
that critically slow. So I can just use string alternatively.

### Pattern: use string

This indeed lowers the performance, but slightly easier to read.

### Generator pattern: step2-generator.py

I like this one about being able to reduce the parameter for keeping track of
the string during the recursion.

### Pattern: keep track of numbers of unclosed brackets and right brackets

I coded this just for exploration.

## step3

It took 12min to solve at the first try.
Second try took 5 mins.
