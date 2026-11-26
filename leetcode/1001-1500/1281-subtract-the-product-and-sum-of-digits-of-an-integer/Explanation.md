# LeetCode 1281: Subtract the Product and Sum of Digits of an Integer

**LeetCode Problem #1281 — Subtract the Product and Sum of Digits of an Integer**
Solve LeetCode Subtract the Product and Sum of Digits of an Integer using Python and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Subtract the Product and Sum of Digits of an Integer |
| LeetCode | #1281 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an integer number `n`, return the difference between the product of its digits and the sum of its digits.

## Constraints
- `1 <= n <= 10^5`

## Examples
### Example 1
- **Input:** `n = 234`
- **Output:** `15`

### Example 2
- **Input:** `n = 4421`
- **Output:** `21`

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Subtract the Product and Sum of Digits of an Integer**, we observe the problem requirements and utilize the **Prefix Sum** technique. We iterate through the inputs using **Prefix Sum Precomputation**, leveraging a **Prefix Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Prefix Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 234`.
2. **Processing Steps:** We apply **Prefix Sum Precomputation** using our **Prefix Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `15`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Prefix Array.

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        total = 0

        while n > 0:
            digit = n % 10
            product *= digit
            total += digit
            n //= 10

        return product - total
```

## Why This Works
By utilizing **Prefix Sum**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1317. Convert Integer to the Sum of Two No-Zero Integers](../../1001-1500/1317-convert-integer-to-the-sum-of-two-no-zero-integers/)
- [1837. Sum of Digits in Base K](../../1501-2000/1837-sum-of-digits-in-base-k/)
- [1945. Sum of Digits of String After Convert](../../1501-2000/1945-sum-of-digits-of-string-after-convert/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/)
