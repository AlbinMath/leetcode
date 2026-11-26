# LeetCode 3728: Stable Subarrays With Equal Boundary and Interior Sum

**LeetCode Problem #3728 — Stable Subarrays With Equal Boundary and Interior Sum**
Solve LeetCode Stable Subarrays With Equal Boundary and Interior Sum using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Stable Subarrays With Equal Boundary and Interior Sum |
| LeetCode | #3728 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `capacity`.

A subarray `capacity[l..r]` is considered **stable** if:

Its length is **at least** 3. 
 The **first** and **last** elements are each equal to the **sum** of all elements **strictly between** them (i.e., `capacity[l] = capacity[r] = capacity[l + 1] + capacity[l + 2] + ... + capacity[r - 1]`).

Return an integer denoting the number of **stable subarrays**.

## Constraints
- `3 <= capacity.length <= 10^5`
- `-10^9 <= capacity[i] <= 10^9`

## Examples
### Example 1
- **Input:** `capacity = [9,3,3,3,9]`
- **Output:** `2`
- **Explanation:** `[9,3,3,3,9]` is stable because the first and last elements are both 9, and the sum of the elements strictly between them is `3 + 3 + 3 = 9`. 
 `[3,3,3]` is stable because the first and last elements are both 3, and the sum of the elements strictly between them is 3.

### Example 2
- **Input:** `capacity = [1,2,3,4,5]`
- **Output:** `0`
- **Explanation:** No subarray of length at least 3 has equal first and last elements, so the answer is 0.

### Example 3
- **Input:** `capacity = [-4,4,0,0,-8,-4]`
- **Output:** `1`
- **Explanation:** `[-4,4,0,0,-8,-4]` is stable because the first and last elements are both -4, and the sum of the elements strictly between them is `4 + 0 + 0 + (-8) = -4`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Stable Subarrays With Equal Boundary and Interior Sum**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `capacity = [9,3,3,3,9]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** `[9,3,3,3,9]` is stable because the first and last elements are both 9, and the sum of the elements strictly between them is `3 + 3 + 3 = 9`. 
 `[3,3,3]` is stable because the first and last elements are both 3, and the sum of the elements strictly between them is 3.

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
from collections import defaultdict
from typing import List

class Solution:
    def countStableSubarrays(self, capacity: List[int]) -> int:
        n = len(capacity)
        P = [0] * (n + 1)
        for i, v in enumerate(capacity):
            P[i + 1] = P[i] + v

        cnt = defaultdict(int)
        res = 0
        for r in range(2, n):
            l = r - 2
            cnt[(capacity[l], P[l + 1])] += 1
            v = capacity[r]
            res += cnt.get((v, P[r] - v), 0)
        return res
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
- [416. Partition Equal Subset Sum](../../0001-0500/0416-partition-equal-subset-sum/)
- [689. Maximum Sum of 3 Non-Overlapping Subarrays](../../0501-1000/0689-maximum-sum-of-3-non-overlapping-subarrays/)
- [698. Partition to K Equal Sum Subsets](../../0501-1000/0698-partition-to-k-equal-sum-subsets/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/stable-subarrays-with-equal-boundary-and-interior-sum/)
