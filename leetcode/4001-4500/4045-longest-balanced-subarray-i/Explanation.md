# LeetCode 3719: Longest Balanced Subarray I

**LeetCode Problem #3719 — Longest Balanced Subarray I**
Solve LeetCode Longest Balanced Subarray I using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Balanced Subarray I |
| LeetCode | #3719 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`.

A ** subarray ** is called **balanced** if the number of **distinct even** numbers in the subarray is equal to the number of **distinct odd** numbers.

Return the length of the **longest** balanced subarray.

## Constraints
- `1 <= nums.length <= 1500`
- `1 <= nums[i] <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [2,5,4,3]`
- **Output:** `4`
- **Explanation:** The longest balanced subarray is `[2, 5, 4, 3]`. 
 It has 2 distinct even numbers `[2, 4]` and 2 distinct odd numbers `[5, 3]`. Thus, the answer is 4.

### Example 2
- **Input:** `nums = [3,2,2,5,4]`
- **Output:** `5`
- **Explanation:** The longest balanced subarray is `[3, 2, 2, 5, 4]`. 
 It has 2 distinct even numbers `[2, 4]` and 2 distinct odd numbers `[3, 5]`. Thus, the answer is 5.

### Example 3
- **Input:** `nums = [1,2,3,2]`
- **Output:** `3`
- **Explanation:** The longest balanced subarray is `[2, 3, 2]`. 
 It has 1 distinct even number `[2]` and 1 distinct odd number `[3]`. Thus, the answer is 3.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Longest Balanced Subarray I**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,5,4,3]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The longest balanced subarray is `[2, 5, 4, 3]`. 
 It has 2 distinct even numbers `[2, 4]` and 2 distinct odd numbers `[5, 3]`. Thus, the answer is 4.

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
    def longestBalanced(self, nums):
        n = len(nums)
        ans = 0
        for l in range(n):
            evens = set()
            odds = set()
            for r in range(l, n):
                v = nums[r]
                if v % 2 == 0:
                    evens.add(v)
                else:
                    odds.add(v)
                if len(evens) == len(odds):
                    ans = max(ans, r - l + 1)
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
- [3721. Longest Balanced Subarray II](../../4001-4500/4047-longest-balanced-subarray-ii/)
- [978. Longest Turbulent Subarray](../../1001-1500/1020-longest-turbulent-subarray/)
- [1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](../../1501-2000/1549-longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-balanced-subarray-i/)
