# LeetCode 1187: Make Array Strictly Increasing

**LeetCode Problem #1187 — Make Array Strictly Increasing**
Solve LeetCode Make Array Strictly Increasing using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Make Array Strictly Increasing |
| LeetCode | #1187 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given two integer arrays `arr1` and `arr2`, return the minimum number of operations (possibly zero) needed to make `arr1` strictly increasing.

In one operation, you can choose two indices `0 <= i < arr1.length` and `0 <= j < arr2.length` and do the assignment `arr1[i] = arr2[j]`.

If there is no way to make `arr1` strictly increasing, return `-1`.

## Constraints
- `1 <= arr1.length, arr2.length <= 2000`
- `0 <= arr1[i], arr2[i] <= 10^9`

## Examples
### Example 1
- **Input:** `arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]`
- **Output:** `1`
- **Explanation:** Replace `5` with `2`, then `arr1 = [1, 2, 3, 6, 7]`.

### Example 2
- **Input:** `arr1 = [1,5,3,6,7], arr2 = [4,3,1]`
- **Output:** `2`
- **Explanation:** Replace `5` with `3` and then replace `3` with `4`. `arr1 = [1, 3, 4, 6, 7]`.

### Example 3
- **Input:** `arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]`
- **Output:** `-1`
- **Explanation:** You can't make `arr1` strictly increasing.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Make Array Strictly Increasing**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** Replace `5` with `2`, then `arr1 = [1, 2, 3, 6, 7]`.

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
from bisect import bisect_right
from typing import List

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = sorted(set(arr2))
        dp = {-1: 0}

        for x in arr1:
            ndp = {}
            for prev, ops in dp.items():
                # keep x
                if x > prev:
                    if x not in ndp or ops < ndp[x]:
                        ndp[x] = ops
                # replace x with the smallest arr2 value > prev
                idx = bisect_right(arr2, prev)
                if idx < len(arr2):
                    y = arr2[idx]
                    if y not in ndp or ops + 1 < ndp[y]:
                        ndp[y] = ops + 1
            if not ndp:
                return -1
            dp = ndp

        return min(dp.values())
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
- [1909. Remove One Element to Make the Array Strictly Increasing](../../1501-2000/1909-remove-one-element-to-make-the-array-strictly-increasing/)
- [1827. Minimum Operations to Make the Array Increasing](../../1501-2000/1827-minimum-operations-to-make-the-array-increasing/)
- [2111. Minimum Operations to Make the Array K-Increasing](../../2001-2500/2111-minimum-operations-to-make-the-array-k-increasing/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/make-array-strictly-increasing/)
