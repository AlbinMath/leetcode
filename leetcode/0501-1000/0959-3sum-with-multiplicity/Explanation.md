# LeetCode 923: 3Sum With Multiplicity

**LeetCode Problem #923 — 3Sum With Multiplicity**
Solve LeetCode 3Sum With Multiplicity using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | 3Sum With Multiplicity |
| LeetCode | #923 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `arr`, and an integer `target`, return the number of tuples `i, j, k` such that `i < j < k` and `arr[i] + arr[j] + arr[k] == target`.

As the answer can be very large, return it **modulo** `10^9 + 7`.

## Constraints
- `3 <= arr.length <= 3000`
- `0 <= arr[i] <= 100`
- `0 <= target <= 300`

## Examples
### Example 1
- **Input:** `arr = [1,1,2,2,3,3,4,4,5,5], target = 8`
- **Output:** `20`
- **Explanation:** Enumerating by the values (arr[i], arr[j], arr[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.

### Example 2
- **Input:** `arr = [1,1,2,2,2,2], target = 5`
- **Output:** `12`
- **Explanation:** arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.

### Example 3
- **Input:** `arr = [2,1,3], target = 6`
- **Output:** `1`
- **Explanation:** (1, 2, 3) occured one time in the array so we return 1.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **3Sum With Multiplicity**, we observe the problem requirements and utilize the **Two Pointers** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [1,1,2,2,3,3,4,4,5,5], target = 8`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `20`.
4. **Verification:** Enumerating by the values (arr[i], arr[j], arr[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from collections import Counter

class Solution:
    def threeSumMulti(self, arr: list[int], target: int) -> int:
        MOD = 10**9 + 7
        c = Counter(arr)
        ans = 0
        for x in range(101):
            if c[x] == 0:
                continue
            for y in range(x, 101):
                if c[y] == 0:
                    continue
                z = target - x - y
                if z < y or z > 100 or c[z] == 0:
                    continue
                if x == y == z:
                    ans += c[x] * (c[x] - 1) * (c[x] - 2) // 6
                elif x == y:
                    ans += c[x] * (c[x] - 1) // 2 * c[z]
                elif y == z:
                    ans += c[x] * (c[y] * (c[y] - 1) // 2)
                else:
                    ans += c[x] * c[y] * c[z]
        return ans % MOD
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [15. 3Sum](../../0001-0500/0015-3sum/)
- [16. 3Sum Closest](../../0001-0500/0016-3sum-closest/)
- [2. Add Two Numbers](../../0001-0500/0002-add-two-numbers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/3sum-with-multiplicity/)
