# LeetCode 2600: K Items With the Maximum Sum

**LeetCode Problem #2600 — K Items With the Maximum Sum**
Solve LeetCode K Items With the Maximum Sum using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | K Items With the Maximum Sum |
| LeetCode | #2600 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is a bag that consists of items, each item has a number `1`, `0`, or `-1` written on it.

You are given four **non-negative **integers `numOnes`, `numZeros`, `numNegOnes`, and `k`.

The bag initially contains:

`numOnes` items with `1`s written on them. 
 `numZeroes` items with `0`s written on them. 
 `numNegOnes` items with `-1`s written on them.

We want to pick exactly `k` items among the available items. Return *the **maximum** possible sum of numbers written on the items*.

## Constraints
- `0 <= numOnes, numZeros, numNegOnes <= 50`
- `0 <= k <= numOnes + numZeros + numNegOnes`

## Examples
### Example 1
- **Input:** `numOnes = 3, numZeros = 2, numNegOnes = 0, k = 2`
- **Output:** `2`
- **Explanation:** We have a bag of items with numbers written on them {1, 1, 1, 0, 0}. We take 2 items with 1 written on them and get a sum in a total of 2.
It can be proven that 2 is the maximum possible sum.

### Example 2
- **Input:** `numOnes = 3, numZeros = 2, numNegOnes = 0, k = 4`
- **Output:** `3`
- **Explanation:** We have a bag of items with numbers written on them {1, 1, 1, 0, 0}. We take 3 items with 1 written on them, and 1 item with 0 written on it, and get a sum in a total of 3.
It can be proven that 3 is the maximum possible sum.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **K Items With the Maximum Sum**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `numOnes = 3, numZeros = 2, numNegOnes = 0, k = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** We have a bag of items with numbers written on them {1, 1, 1, 0, 0}. We take 2 items with 1 written on them and get a sum in a total of 2.
It can be proven that 2 is the maximum possible sum.

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
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if k <= numOnes:
            return k
        if k <= numOnes + numZeros:
            return numOnes
        return numOnes - (k - numOnes - numZeros)
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
- [1191. K-Concatenation Maximum Sum](../../1001-1500/1191-k-concatenation-maximum-sum/)
- [2461. Maximum Sum of Distinct Subarrays With Length K](../../2001-2500/2461-maximum-sum-of-distinct-subarrays-with-length-k/)
- [2656. Maximum Sum With Exactly K Elements ](../../2501-3000/2656-maximum-sum-with-exactly-k-elements/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/k-items-with-the-maximum-sum/)
