# LeetCode 2602: Minimum Operations to Make All Array Elements Equal

**LeetCode Problem #2602 — Minimum Operations to Make All Array Elements Equal**
Solve LeetCode Minimum Operations to Make All Array Elements Equal using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Operations to Make All Array Elements Equal |
| LeetCode | #2602 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array `nums` consisting of positive integers.

You are also given an integer array `queries` of size `m`. For the `i^th` query, you want to make all of the elements of `nums` equal to` queries[i]`. You can perform the following operation on the array **any** number of times:

**Increase** or **decrease** an element of the array by `1`.

Return *an array *`answer`* of size *`m`* where *`answer[i]`* is the **minimum** number of operations to make all elements of *`nums`* equal to *`queries[i]`.

**Note** that after each query the array is reset to its original state.

## Constraints
- `n == nums.length`
- `m == queries.length`
- `1 <= n, m <= 10^5`
- `1 <= nums[i], queries[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [3,1,6,8], queries = [1,5]`
- **Output:** `[14,10]`
- **Explanation:** For the first query we can do the following operations:
- Decrease nums[0] 2 times, so that nums = [1,1,6,8].
- Decrease nums[2] 5 times, so that nums = [1,1,1,8].
- Decrease nums[3] 7 times, so that nums = [1,1,1,1].
So the total number of operations for the first query is 2 + 5 + 7 = 14.
For the second query we can do the following operations:
- Increase nums[0] 2 times, so that nums = [5,1,6,8].
- Increase nums[1] 4 times, so that nums = [5,5,6,8].
- Decrease nums[2] 1 time, so that nums = [5,5,5,8].
- Decrease nums[3] 3 times, so that nums = [5,5,5,5].
So the total number of operations for the second query is 2 + 4 + 1 + 3 = 10.

### Example 2
- **Input:** `nums = [2,9,6,3], queries = [10]`
- **Output:** `[20]`
- **Explanation:** We can increase each value in the array to 10. The total number of operations will be 8 + 1 + 4 + 7 = 20.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Operations to Make All Array Elements Equal**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,1,6,8], queries = [1,5]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[14,10]`.
4. **Verification:** For the first query we can do the following operations:
- Decrease nums[0] 2 times, so that nums = [1,1,6,8].
- Decrease nums[2] 5 times, so that nums = [1,1,1,8].
- Decrease nums[3] 7 times, so that nums = [1,1,1,1].
So the total number of operations for the first query is 2 + 5 + 7 = 14.
For the second query we can do the following operations:
- Increase nums[0] 2 times, so that nums = [5,1,6,8].
- Increase nums[1] 4 times, so that nums = [5,5,6,8].
- Decrease nums[2] 1 time, so that nums = [5,5,5,8].
- Decrease nums[3] 3 times, so that nums = [5,5,5,5].
So the total number of operations for the second query is 2 + 4 + 1 + 3 = 10.

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
from itertools import accumulate
from typing import List

class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        pre = [0] + list(accumulate(nums))
        total = pre[n]

        ans = []
        for q in queries:
            k = bisect_right(nums, q)
            left = q * k - pre[k]
            right = (total - pre[k]) - q * (n - k)
            ans.append(left + right)
        return ans
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
- [2654. Minimum Number of Operations to Make All Array Elements Equal to 1](../../2501-3000/2654-minimum-number-of-operations-to-make-all-array-elements-equal-to-1/)
- [3191. Minimum Operations to Make Binary Array Elements Equal to One I](../../3001-3500/3191-minimum-operations-to-make-binary-array-elements-equal-to-one-i/)
- [2772. Apply Operations to Make All Array Elements Equal to Zero](../../2501-3000/2772-apply-operations-to-make-all-array-elements-equal-to-zero/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal/)
