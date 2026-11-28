# LeetCode 1561: Maximum Number of Coins You Can Get

**LeetCode Problem #1561 — Maximum Number of Coins You Can Get**
Solve LeetCode Maximum Number of Coins You Can Get using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Number of Coins You Can Get |
| LeetCode | #1561 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There are `3n` piles of coins of varying size, you and your friends will take piles of coins as follows:

In each step, you will choose **any **`3` piles of coins (not necessarily consecutive). 
 Of your choice, Alice will pick the pile with the maximum number of coins. 
 You will pick the next pile with the maximum number of coins. 
 Your friend Bob will pick the last pile. 
 Repeat until there are no more piles of coins.

Given an array of integers `piles` where `piles[i]` is the number of coins in the `i^th` pile.

Return the maximum number of coins that you can have.

## Constraints
- `3 <= piles.length <= 10^5`
- `piles.length % 3 == 0`
- `1 <= piles[i] <= 10^4`

## Examples
### Example 1
- **Input:** `piles = [2,4,1,2,7,8]`
- **Output:** `9`
- **Explanation:** Choose the triplet (2, 7, 8), Alice Pick the pile with 8 coins, you the pile with

### Example 2
- **Input:** `piles = [2,4,5]`
- **Output:** `4`

### Example 3
- **Input:** `piles = [9,8,7,6,5,1,2,3,4]`
- **Output:** `18`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Number of Coins You Can Get**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `piles = [2,4,1,2,7,8]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `9`.
4. **Verification:** Choose the triplet (2, 7, 8), Alice Pick the pile with 8 coins, you the pile with

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
    def maxCoins(self, piles):
        piles.sort()
        return sum(piles[len(piles)//3::2])
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
- [1798. Maximum Number of Consecutive Values You Can Make](../../1501-2000/1798-maximum-number-of-consecutive-values-you-can-make/)
- [1935. Maximum Number of Words You Can Type](../../1501-2000/1935-maximum-number-of-words-you-can-type/)
- [1953. Maximum Number of Weeks for Which You Can Work](../../1501-2000/1953-maximum-number-of-weeks-for-which-you-can-work/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-number-of-coins-you-can-get/)
