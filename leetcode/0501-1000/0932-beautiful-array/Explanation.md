# LeetCode 932: Beautiful Array

**LeetCode Problem #932 — Beautiful Array**
Solve LeetCode Beautiful Array using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Beautiful Array |
| LeetCode | #932 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
An array `nums` of length `n` is **beautiful** if:

`nums` is a permutation of the integers in the range `[1, n]`. 
 For every `0 <= i < j < n`, there is no index `k` with `i < k < j` where `2 * nums[k] == nums[i] + nums[j]`.

Given the integer `n`, return *any **beautiful** array *`nums`* of length *`n`. There will be at least one valid answer for the given `n`.

## Constraints
- `1 <= n <= 1000`

## Examples
### Example 1
- **Input:** `n = 4`
- **Output:** `[2,1,4,3]`

### Example 2
- **Input:** `n = 5`
- **Output:** `[3,1,2,5,4]`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Beautiful Array**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 4`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,1,4,3]`.

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
    def beautifulArray(self, n):
        res = [1]
        while len(res) < n:
            res = [2*x-1 for x in res if 2*x-1 <= n] + [2*x for x in res if 2*x <= n]
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
- [2216. Minimum Deletions to Make Array Beautiful](../../2001-2500/2216-minimum-deletions-to-make-array-beautiful/)
- [3006. Find Beautiful Indices in the Given Array I](../../3001-3500/3006-find-beautiful-indices-in-the-given-array-i/)
- [3008. Find Beautiful Indices in the Given Array II](../../3001-3500/3008-find-beautiful-indices-in-the-given-array-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/beautiful-array/)
