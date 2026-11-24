# LeetCode 3723: Maximize Sum of Squares of Digits

**LeetCode Problem #3723 — Maximize Sum of Squares of Digits**
Solve LeetCode Maximize Sum of Squares of Digits using Python and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximize Sum of Squares of Digits |
| LeetCode | #3723 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two **positive** integers `num` and `sum`.

A positive integer `n` is **good** if it satisfies both of the following:

The number of digits in `n` is **exactly** `num`. 
 The sum of digits in `n` is **exactly** `sum`.

The **score** of a **good** integer `n` is the sum of the squares of digits in `n`.

Return a **string** denoting the **good** integer `n` that achieves the **maximum** **score**. If there are multiple possible integers, return the **maximum **​​​​​​​one. If no such integer exists, return an empty string.

## Constraints
- `1 <= num <= 2 * 10^5`
- `1 <= sum <= 2 * 10^6`

## Examples
### Example 1
- **Input:** `num = 2, sum = 3`
- **Output:** `"30"`
- **Explanation:** There are 3 good integers: 12, 21, and 30. 

 
 The score of 12 is `1^2 + 2^2 = 5`. 
 The score of 21 is `2^2 + 1^2 = 5`. 
 The score of 30 is `3^2 + 0^2 = 9`. 
 

 The maximum score is 9, which is achieved by the good integer 30. Therefore, the answer is `"30"`.

### Example 2
- **Input:** `num = 2, sum = 17`
- **Output:** `"98"`
- **Explanation:** There are 2 good integers: 89 and 98. 

 
 The score of 89 is `8^2 + 9^2 = 145`. 
 The score of 98 is `9^2 + 8^2 = 145`. 
 

 The maximum score is 145. The maximum good integer that achieves this score is 98. Therefore, the answer is `"98"`.

### Example 3
- **Input:** `num = 1, sum = 10`
- **Output:** `""`
- **Explanation:** There are no integers that have exactly 1 digit and whose digits sum to 10. Therefore, the answer is `""`.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximize Sum of Squares of Digits**, we observe the problem requirements and utilize the **Math & Logic** technique. We iterate through the inputs using **Mathematical Simulation & Modular Arithmetic**, leveraging a **Primitive Types** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Primitive Types**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `num = 2, sum = 3`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"30"`.
4. **Verification:** There are 3 good integers: 12, 21, and 30. 

 
 The score of 12 is `1^2 + 2^2 = 5`. 
 The score of 21 is `2^2 + 1^2 = 5`. 
 The score of 30 is `3^2 + 0^2 = 9`. 
 

 The maximum score is 9, which is achieved by the good integer 30. Therefore, the answer is `"30"`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""
        return "9" * (sum // 9) + str(sum % 9) * (sum % 9 > 0) + "0" * (num - (sum + 8) // 9)
```

## Why This Works
By utilizing **Math & Logic**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2897. Apply Operations on Array to Maximize Sum of Squares](../../2501-3000/2897-apply-operations-on-array-to-maximize-sum-of-squares/)
- [1005. Maximize Sum Of Array After K Negations](../../1001-1500/1005-maximize-sum-of-array-after-k-negations/)
- [1281. Subtract the Product and Sum of Digits of an Integer](../../1001-1500/1281-subtract-the-product-and-sum-of-digits-of-an-integer/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximize-sum-of-squares-of-digits/)
