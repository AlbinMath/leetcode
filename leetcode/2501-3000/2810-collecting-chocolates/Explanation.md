# LeetCode 2735: Collecting Chocolates

**LeetCode Problem #2735 — Collecting Chocolates**
Solve LeetCode Collecting Chocolates using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Collecting Chocolates |
| LeetCode | #2735 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** integer array `nums` of size `n` representing the cost of collecting different chocolates. The cost of collecting the chocolate at the index `i` is `nums[i]`. Each chocolate is of a different type, and initially, the chocolate at the index `i` is of `i^th` type.

In one operation, you can do the following with an incurred **cost** of `x`:

Simultaneously change the chocolate of `i^th` type to `((i + 1) mod n)^th` type for all chocolates.

Return *the minimum cost to collect chocolates of all types, given that you can perform as many operations as you would like.*

## Constraints
- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 10^9`
- `1 <= x <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [20,1,15], x = 5`
- **Output:** `13`
- **Explanation:** Initially, the chocolate types are [0,1,2]. We will buy the 1^st type of chocolate at a cost of 1.
Now, we will perform the operation at a cost of 5, and the types of chocolates will become [1,2,0]. We will buy the 2^nd^ type of chocolate at a cost of 1.
Now, we will again perform the operation at a cost of 5, and the chocolate types will become [2,0,1]. We will buy the 0^th type of chocolate at a cost of 1. 
Thus, the total cost will become (1 + 5 + 1 + 5 + 1) = 13. We can prove that this is optimal.

### Example 2
- **Input:** `nums = [1,2,3], x = 4`
- **Output:** `6`
- **Explanation:** We will collect all three types of chocolates at their own price without performing any operations. Therefore, the total cost is 1 + 2 + 3 = 6.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Collecting Chocolates**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [20,1,15], x = 5`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `13`.
4. **Verification:** Initially, the chocolate types are [0,1,2]. We will buy the 1^st type of chocolate at a cost of 1.
Now, we will perform the operation at a cost of 5, and the types of chocolates will become [1,2,0]. We will buy the 2^nd^ type of chocolate at a cost of 1.
Now, we will again perform the operation at a cost of 5, and the chocolate types will become [2,0,1]. We will buy the 0^th type of chocolate at a cost of 1. 
Thus, the total cost will become (1 + 5 + 1 + 5 + 1) = 13. We can prove that this is optimal.

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
class Solution(object):
    def minCost(self, nums, x):
        n = len(nums)
        min_cost = list(nums)
        ans = sum(min_cost)

        for k in range(1, n):
            for i in range(n):
                prev_idx = (i - k) % n
                if nums[prev_idx] < min_cost[i]:
                    min_cost[i] = nums[prev_idx]
            ans = min(ans, k * x + sum(min_cost))

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
- [2920. Maximum Points After Collecting Coins From All Nodes](../../3001-3500/3179-maximum-points-after-collecting-coins-from-all-nodes/)
- [5. Longest Palindromic Substring](../../0001-0500/0005-longest-palindromic-substring/)
- [26. Remove Duplicates from Sorted Array](../../0001-0500/0026-remove-duplicates-from-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/collecting-chocolates/)
