## step1

Think of that you're looking at the ith fence, to get the number of ways to paint this particular fence, you need to take a look at the two previous fences.
If those fences are painted in the same color, you can chose k - 1 colors for the ith fence.
Otherwise you can chose k colors.
--There are p1 and p2 parallel universes for the two previous fences before getting to the ith fence, and you have only k universes where you can chose k-1 color. In other universes you can pick k color.--

I took a look at solutions from other people. 
- https://github.com/goto-untrapped/Arai60/pull/44

Why do you add `totalWays[i - 1] + totalWays[i - 2]`? It doesn't make sense.
(I asked calude to explain this logic) So when decing the color of ith fence, you have 2 options:
1. Chose a different color from i - 1 th fence: That's k - 1 universe.
2. Chose the same color as i - 1 ith fence: chose a different k - 1 color form i - 2. (k - 1) * (all the valid permutations at i - 2)
Therefore, (k - 1) * (number of ways at i - 1) + (k - 1) * (number of ways at i - 2)


This implementation takes O(2^n) computational complexity.
```
public class PaintFence {
    class Solution {
        public int numWays(int n, int k) {
            if (n == 1) {
                return k;
            }
            if (n == 2) {
                return k * k;
            }
            return (k - 1) * (numWays(n - 1, k) + numWays(n - 2, k));
        }
    }
```

One idea is to reduce computational complexity is to cahce the method.
Another idea is to create a list that will hold number of ways at each fence. Additionally, you can omit the list and just keep track of the most recent 2 fences.
Another idea is to use LRU cache.

The computational complexity will be O(n) for the both.
There is a discussion to optimize the solution down to O(log n) by applying fibonacci techniques but I didn't spend much time to understand it.

## step2

Took inspiration from [this code](https://github.com/goto-untrapped/Arai60/pull/44/files):

```
    public int numWays2_4(int n, int k) {
        if (n == 1) {
            return k;
        }
        int prevNumWays = k;
        int currentNumWays = k * k;
        for (int i = 3; i < n + 1; i++) {
            int nextNumWays = (k - 1) * (prevNumWays + currentNumWays);
            prevNumWays = currentNumWays;
            currentNumWays = nextNumWays;
        } 
        return currentNumWays;
    }
```

I like naming `same_color` and `different_color` to be descriptive.

## step3

I finished in 6 mins(I was talking to my sister and eating wuffles so this duration is not accurate)
