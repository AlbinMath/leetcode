# LeetCode 3010: Divide an Array Into Subarrays With Minimum Cost I

**LeetCode Problem #3010 — Divide an Array Into Subarrays With Minimum Cost I**
Solve LeetCode Divide an Array Into Subarrays With Minimum Cost I using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Divide an Array Into Subarrays With Minimum Cost I |
| LeetCode | #3010 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array of integers `nums` of length `n`.

The **cost** of an array is the value of its **first** element. For example, the cost of `[1,2,3]` is `1` while the cost of `[3,4,1]` is `3`.

You need to divide `nums` into `3` **disjoint contiguous ** subarrays .

Return *the **minimum** possible **sum** of the cost of these subarrays*.

## Constraints
- `3 <= n <= 50`
- `1 <= nums[i] <= 50`

## Examples
### Example 1
- **Input:** `nums = [1,2,3,12]`
- **Output:** `6`
- **Explanation:** The best possible way to form 3 subarrays is: [1], [2], and [3,12] at a total cost of 1 + 2 + 3 = 6.
The other possible ways to form 3 subarrays are:
- [1], [2,3], and [12] at a total cost of 1 + 2 + 12 = 15.
- [1,2], [3], and [12] at a total cost of 1 + 3 + 12 = 16.

### Example 2
- **Input:** `nums = [5,4,3]`
- **Output:** `12`
- **Explanation:** The best possible way to form 3 subarrays is: [5], [4], and [3] at a total cost of 5 + 4 + 3 = 12.
It can be shown that 12 is the minimum cost achievable.

### Example 3
- **Input:** `nums = [10,3,1,1]`
- **Output:** `12`
- **Explanation:** The best possible way to form 3 subarrays is: [10,3], [1], and [1] at a total cost of 10 + 1 + 1 = 12.
It can be shown that 12 is the minimum cost achievable.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Divide an Array Into Subarrays With Minimum Cost I**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,12]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** The best possible way to form 3 subarrays is: [1], [2], and [3,12] at a total cost of 1 + 2 + 3 = 6.
The other possible ways to form 3 subarrays are:
- [1], [2,3], and [12] at a total cost of 1 + 2 + 12 = 15.
- [1,2], [3], and [12] at a total cost of 1 + 3 + 12 = 16.

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
from typing import List

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        rest = sorted(nums[1:])
        return nums[0] + rest[0] + rest[1]
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
- [3013. Divide an Array Into Subarrays With Minimum Cost II](../../3001-3500/3013-divide-an-array-into-subarrays-with-minimum-cost-ii/)
- [3500. Minimum Cost to Divide Array Into Subarrays](../../3001-3500/3500-minimum-cost-to-divide-array-into-subarrays/)
- [2206. Divide Array Into Equal Pairs](../../2001-2500/2206-divide-array-into-equal-pairs/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/)
