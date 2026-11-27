# LeetCode 3622: Check Divisibility by Digit Sum and Product

**LeetCode Problem #3622 — Check Divisibility by Digit Sum and Product**
Solve LeetCode Check Divisibility by Digit Sum and Product using C, Python and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check Divisibility by Digit Sum and Product |
| LeetCode | #3622 |
| Difficulty | Easy |
| Language | C, Python |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a positive integer `n`. Determine whether `n` is divisible by the **sum **of the following two values:

The **digit sum** of `n` (the sum of its digits).

The **digit** **product** of `n` (the product of its digits).

Return `true` if `n` is divisible by this sum; otherwise, return `false`.

## Constraints
- `1 <= n <= 10^6`

## Examples
### Example 1
- **Input:** `n = 99`
- **Output:** `true`
- **Explanation:** Since 99 is divisible by the sum (9 + 9 = 18) plus product (9 * 9 = 81) of its digits (total 99), the output is true.

### Example 2
- **Input:** `n = 23`
- **Output:** `false`
- **Explanation:** Since 23 is not divisible by the sum (2 + 3 = 5) plus product (2 * 3 = 6) of its digits (total 11), the output is false.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Check Divisibility by Digit Sum and Product**, we observe the problem requirements and utilize the **Math & Logic** technique. We iterate through the inputs using **Mathematical Simulation & Modular Arithmetic**, leveraging a **Primitive Types** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Primitive Types**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 99`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** Since 99 is divisible by the sum (9 + 9 = 18) plus product (9 * 9 = 81) of its digits (total 99), the output is true.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
C, Python

## Source Code
- [solution.c](./solution.c)
- [solution.py](./solution.py)


### C
```c
bool checkDivisibility(int n) {
    int temp = n;
    int sum = 0;
    int product = 1;

    while (temp > 0) {
        int digit = temp % 10;

        sum += digit;
        product *= digit;

        temp /= 10;
    }

    return n % (sum + product) == 0;
}
```

### Python
```python
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        temp = n
        digit_sum = 0
        digit_product = 1
        
        while temp > 0:
            digit = temp % 10
            digit_sum += digit
            digit_product *= digit
            temp //= 10
            
        return n % (digit_sum + digit_product) == 0
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
- [2160. Minimum Sum of Four Digit Number After Splitting Digits](../../2001-2500/2160-minimum-sum-of-four-digit-number-after-splitting-digits/)
- [2180. Count Integers With Even Digit Sum](../../2001-2500/2180-count-integers-with-even-digit-sum/)
- [2243. Calculate Digit Sum of a String](../../2001-2500/2243-calculate-digit-sum-of-a-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/)
