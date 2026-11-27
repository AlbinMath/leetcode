# LeetCode 667: Beautiful Arrangement II

**LeetCode Problem #667 — Beautiful Arrangement II**
Solve LeetCode Beautiful Arrangement II using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Beautiful Arrangement II |
| LeetCode | #667 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given two integers `n` and `k`, construct a list `answer` that contains `n` different positive integers ranging from `1` to `n` and obeys the following requirement:

Suppose this list is `answer = [a_1, a_2, a_3, ... , a_n]`, then the list `[|a_1 - a_2|, |a_2 - a_3|, |a_3 - a_4|, ... , |a_n-1 - a_n|]` has exactly `k` distinct integers.

Return *the list* `answer`. If there multiple valid answers, return **any of them**.

## Constraints
- `1 <= k < n <= 10^4`

## Examples
### Example 1
- **Input:** `n = 3, k = 1`
- **Output:** `[1,2,3]`

### Example 2
- **Input:** `n = 3, k = 2`
- **Output:** `[1,3,2]`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Beautiful Arrangement II**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3, k = 1`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,2,3]`.

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
class Solution:
    def constructArray(self, n: int, k: int) -> list[int]:
        ans = list(range(1, n - k))
        left, right = n - k, n
        while left <= right:
            ans.append(left)
            left += 1
            if left <= right:
                ans.append(right)
                right -= 1
                
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
- [526. Beautiful Arrangement](../../0501-1000/0526-beautiful-arrangement/)
- [2097. Valid Arrangement of Pairs](../../2001-2500/2097-valid-arrangement-of-pairs/)
- [932. Beautiful Array](../../0501-1000/0932-beautiful-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/beautiful-arrangement-ii/)
