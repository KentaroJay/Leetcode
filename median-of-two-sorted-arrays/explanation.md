## Partition(Create two virtual array)

- Create two virtual that represents the former part and the latter part of the answer array.
- In order to do it, we create partitions in each given arrays.

### What is partition?

Think of two queues of people, sorted by their heights. We basically want to tell people to form another type of queues that represents the former part and the latter part of the queue that all the people from both queues sorted in heights.
In order to do that, we want to put "flags" to both of the queues.
The people before the flag have to go to the fomer part queue, meanwhile the people after the flag have to go to the latter queue.

**Example**
[int, int, | int, ..., int, int, int] -> This means the first two people have to go to the former queue, the others have to go to the latter.
[int, int, int, ..., int, int, int | ] -> This means all people from this queue have to go to the former queue.

### How to determine the positions of the partitions?
**Constraints**
1. The partition has to be somewhere in the queue.
2. We define partitions so indexes of both partitions added together equals to the index of the median.

array = former array + latter array
if array length is even, then the median is `(last item from the former array + the first item from the latter array) / 2`.
if array length is odd, then the median is `last item from the former array`.

We think of a window to binary search the proper place to put the partition.
Initially, we have the window that spans over the array.

[int, int, int, ..., int, int, int]
 ^left                              ^right

Then we get the middle of it. The second constraint can determine the other parition as well at this point.
Basically, we want as much items to get to the index of the median.

[int, int, int, ..., int | int, .., int, int, int]          [int, int, ..., int, int]
 ^left                   ^mid                      ^right  ^  ^    ^         ^    ^   ^  the other partitions is somewhere

> mid = (right - left) // 2, representing the index of the first value in the right window.
> denote k as the index of the half point.
> if mid - left < k + 1, then we want `k + 1 - (mid - left)` items from the other array.
> if mid - left == k + 1, then we don' want any items from the other array.
> if mid - left > k + 1, then we want to binary search on this window.

if max(items of the left windows) <= min(items of the right windows), then that is a proper partition.
if the last item of left hand in the first array > the first item of the right hand in the second array, then right = mid - 1.
if the last item of left hand in the second array > the first item of the right hand in the first array, then left = mid + 1. 

## Binary Search(Prune unneccessary elements)
