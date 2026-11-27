# LeetCode 1262: Greatest Sum Divisible by Three

**LeetCode Problem #1262 — Greatest Sum Divisible by Three**
Solve LeetCode Greatest Sum Divisible by Three using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Greatest Sum Divisible by Three |
| LeetCode | #1262 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `nums`, return *the **maximum possible sum **of elements of the array such that it is divisible by three*.

## Constraints
- `1 <= nums.length <= 4 * 10^4`
- `1 <= nums[i] <= 10^4`

## Examples
### Example 1
- **Input:** `nums = [3,6,5,1,8]`
- **Output:** `18`
- **Explanation:** Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).

### Example 2
- **Input:** `nums = [4]`
- **Output:** `0`
- **Explanation:** Since 4 is not divisible by 3, do not pick any number.

### Example 3
- **Input:** `nums = [1,2,3,4,4]`
- **Output:** `12`
- **Explanation:** Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Greatest Sum Divisible by Three**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,6,5,1,8]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `18`.
4. **Verification:** Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).

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
    def maxSumDivThree(self, nums: List[int]) -> int:
        NEG = float('-inf')
        dp = [0, NEG, NEG]
        for x in nums:
            new = dp[:]
            for r in range(3):
                if dp[r] != NEG:
                    nr = (r + x) % 3
                    new[nr] = max(new[nr], dp[r] + x)
            dp = new
        return dp[0]
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
- [3780. Maximum Sum of Three Numbers Divisible by Three](../../3501-4000/3780-maximum-sum-of-three-numbers-divisible-by-three/)
- [1590. Make Sum Divisible by P](../../1501-2000/1590-make-sum-divisible-by-p/)
- [2435. Paths in Matrix Whose Sum Is Divisible by K](../../2001-2500/2435-paths-in-matrix-whose-sum-is-divisible-by-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/greatest-sum-divisible-by-three/)
