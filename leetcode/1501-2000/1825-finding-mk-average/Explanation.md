# LeetCode 1825: Finding MK Average

**LeetCode Problem #1825 — Finding MK Average**
Solve LeetCode Finding MK Average using Python and Sliding Window. This solution finds the optimal result using Dynamic Sliding Window Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Finding MK Average |
| LeetCode | #1825 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Dynamic Sliding Window Traversal |
| Data Structure | Array / Hash Set |
| Pattern | Sliding Window |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two integers, `m` and `k`, and a stream of integers. You are tasked to implement a data structure that calculates the **MKAverage** for the stream.

The **MKAverage** can be calculated using these steps:

If the number of the elements in the stream is less than `m` you should consider the **MKAverage** to be `-1`. Otherwise, copy the last `m` elements of the stream to a separate container. 
 Remove the smallest `k` elements and the largest `k` elements from the container. 
 Calculate the average value for the rest of the elements **rounded down to the nearest integer**.

Implement the `MKAverage` class:

`MKAverage(int m, int k)` Initializes the **MKAverage** object with an empty stream and the two integers `m` and `k`. 
 `void addElement(int num)` Inserts a new element `num` into the stream. 
 `int calculateMKAverage()` Calculates and returns the **MKAverage** for the current stream **rounded down to the nearest integer**.

## Constraints
- `3 <= m <= 10^5`
- `1 < k*2 < m`
- `1 <= num <= 10^5`
- At most `10^5` calls will be made to `addElement` and `calculateMKAverage`.

## Examples
### Example 1
- **Input:** `["MKAverage", "addElement", "addElement", "calculateMKAverage", "addElement", "calculateMKAverage", "addElement", "addElement", "addElement", "calculateMKAverage"]
[[3, 1], [3], [1], [], [10], [], [5], [5], [5], []]`
- **Output:** `[null, null, null, -1, null, 3, null, null, null, 5]`
- **Explanation:** MKAverage obj = new MKAverage(3, 1); 
obj.addElement(3); // current elements are [3]
obj.addElement(1); // current elements are [3,1]
obj.calculateMKAverage(); // return -1, because m = 3 and only 2 elements exist.
obj.addElement(10); // current elements are [3,1,10]
obj.calculateMKAverage(); // The last 3 elements are [3,1,10].
 // After removing smallest and largest 1 element the container will be [3].
 // The average of [3] equals 3/1 = 3, return 3
obj.addElement(5); // current elements are [3,1,10,5]
obj.addElement(5); // current elements are [3,1,10,5,5]
obj.addElement(5); // current elements are [3,1,10,5,5,5]
obj.calculateMKAverage(); // The last 3 elements are [5,5,5].
 // After removing smallest and largest 1 element the container will be [5].
 // The average of [5] equals 5/1 = 5, return 5

## Key Insight
Maintain a dynamic contiguous window with two pointers (`left` and `right`), expanding to include new elements and shrinking when window invariants are violated.

## Approach
To solve **Finding MK Average**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["MKAverage", "addElement", "addElement", "calculateMKAverage", "addElement", "calculateMKAverage", "addElement", "addElement", "addElement", "calculateMKAverage"]
[[3, 1], [3], [1], [], [10], [], [5], [5], [5], []]`.
2. **Processing Steps:** We apply **Dynamic Sliding Window Traversal** using our **Array / Hash Set**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, null, null, -1, null, 3, null, null, null, 5]`.
4. **Verification:** MKAverage obj = new MKAverage(3, 1); 
obj.addElement(3); // current elements are [3]
obj.addElement(1); // current elements are [3,1]
obj.calculateMKAverage(); // return -1, because m = 3 and only 2 elements exist.
obj.addElement(10); // current elements are [3,1,10]
obj.calculateMKAverage(); // The last 3 elements are [3,1,10].
 // After removing smallest and largest 1 element the container will be [3].
 // The average of [3] equals 3/1 = 3, return 3
obj.addElement(5); // current elements are [3,1,10,5]
obj.addElement(5); // current elements are [3,1,10,5,5]
obj.addElement(5); // current elements are [3,1,10,5,5,5]
obj.calculateMKAverage(); // The last 3 elements are [5,5,5].
 // After removing smallest and largest 1 element the container will be [5].
 // The average of [5] equals 5/1 = 5, return 5

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array / Hash Set.

## Pattern
**Sliding Window**

## Topics
- Sliding Window
- Two Pointers
- Subarrays

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from collections import deque

class MKAverage:
    N = 100000

    def __init__(self, m: int, k: int):
        self.m, self.k = m, k
        self.q = deque()
        self.cnt = [0] * (self.N + 1)
        self.sm = [0] * (self.N + 1)

    def _update(self, v: int, dc: int) -> None:
        ds = dc * v
        i = v
        while i <= self.N:
            self.cnt[i] += dc
            self.sm[i] += ds
            i += i & -i

    def _smallest_sum(self, j: int) -> int:
        # sum of the j smallest elements currently in the window
        pos = c = s = 0
        step = 1 << 16                      # highest power of two <= N
        while step:
            nxt = pos + step
            if nxt <= self.N and c + self.cnt[nxt] < j:
                pos = nxt
                c += self.cnt[nxt]
                s += self.sm[nxt]
            step >>= 1
        # remaining (j - c) elements all have value pos + 1
        return s + (j - c) * (pos + 1)

    def addElement(self, num: int) -> None:
        self.q.append(num)
        self._update(num, 1)
        if len(self.q) > self.m:
            self._update(self.q.popleft(), -1)

    def calculateMKAverage(self) -> int:
        if len(self.q) < self.m:
            return -1
        total = self._smallest_sum(self.m - self.k) - self._smallest_sum(self.k)
        return total // (self.m - 2 * self.k)
```

## Why This Works
By utilizing **Sliding Window**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Shrinking the window too late or missing invalid state checks.
2. Forgetting to update window metrics (e.g. char counts) during contraction.
3. Misinterpreting fixed vs variable window requirements.

## Interview Notes
- **Tests:** Two-pointer window management, state tracking, and contiguous subarray analysis.
- **Follow-up:** How do you handle non-positive integer values in subarray sum windows?

## Related Problems
- [1817. Finding the Users Active Minutes](../../1501-2000/1817-finding-the-users-active-minutes/)
- [1865. Finding Pairs With a Certain Sum](../../1501-2000/1865-finding-pairs-with-a-certain-sum/)
- [2094. Finding 3-Digit Even Numbers](../../2001-2500/2094-finding-3-digit-even-numbers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/finding-mk-average/)
