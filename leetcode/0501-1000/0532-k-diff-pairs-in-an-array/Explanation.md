# LeetCode 532: K-diff Pairs in an Array

**LeetCode Problem #532 — K-diff Pairs in an Array**
Solve LeetCode K-diff Pairs in an Array using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | K-diff Pairs in an Array |
| LeetCode | #532 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array of integers `nums` and an integer `k`, return *the number of unique k-diff pairs in the array*.

A **k-diff** pair is an integer pair `(nums[i], nums[j])`, where the following are true:

`0 <= i, j < nums.length` 
 `i != j` 
 `|nums[i] - nums[j]| == k`

**Notice** that `|val|` denotes the absolute value of `val`.

## Constraints
- `1 <= nums.length <= 10^4`
- `-10^7 <= nums[i] <= 10^7`
- `0 <= k <= 10^7`

## Examples
### Example 1
- **Input:** `nums = [3,1,4,1,5], k = 2`
- **Output:** `2`
- **Explanation:** There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of

### Example 2
- **Input:** `nums = [1,2,3,4,5], k = 1`
- **Output:** `4`
- **Explanation:** There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

### Example 3
- **Input:** `nums = [1,3,1,5,4], k = 0`
- **Output:** `1`
- **Explanation:** There is one 0-diff pair in the array, (1, 1).

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **K-diff Pairs in an Array**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,1,4,1,5], k = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from collections import Counter
from typing import List

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)

        if k == 0:
            return sum(1 for c in freq.values() if c > 1)

        return sum(1 for x in freq if x + k in freq)
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [629. K Inverse Pairs Array](../../0501-1000/0629-k-inverse-pairs-array/)
- [1497. Check If Array Pairs Are Divisible by k](../../1001-1500/1497-check-if-array-pairs-are-divisible-by-k/)
- [2183. Count Array Pairs Divisible by K](../../2001-2500/2183-count-array-pairs-divisible-by-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/k-diff-pairs-in-an-array/)
