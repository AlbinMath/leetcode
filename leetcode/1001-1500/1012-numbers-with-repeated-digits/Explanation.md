# LeetCode 1012: Numbers With Repeated Digits

**LeetCode Problem #1012 — Numbers With Repeated Digits**
Solve LeetCode Numbers With Repeated Digits using Python and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Numbers With Repeated Digits |
| LeetCode | #1012 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer `n`, return *the number of positive integers in the range *`[1, n]`* that have **at least one** repeated digit*.

## Constraints
- `1 <= n <= 10^9`

## Examples
### Example 1
- **Input:** `n = 20`
- **Output:** `1`
- **Explanation:** The only positive number (<= 20) with at least 1 repeated digit is 11.

### Example 2
- **Input:** `n = 100`
- **Output:** `10`
- **Explanation:** The positive numbers (<= 100) with atleast 1 repeated digit are 11, 22, 33, 44, 55, 66, 77, 88, 99, and 100.

### Example 3
- **Input:** `n = 1000`
- **Output:** `262`

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Numbers With Repeated Digits**, we observe the problem requirements and utilize the **Math & Logic** technique. We iterate through the inputs using **Mathematical Simulation & Modular Arithmetic**, leveraging a **Primitive Types** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Primitive Types**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 20`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** The only positive number (<= 20) with at least 1 repeated digit is 11.

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
import math

class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        digits = [int(d) for d in str(n + 1)]
        L = len(digits)
        unique_count = 0
        
        for length in range(1, L):
            unique_count += 9 * math.perm(9, length - 1)
            
        seen = set()
        for i, curr_digit in enumerate(digits):
            start_digit = 1 if i == 0 else 0
            for d in range(start_digit, curr_digit):
                if d not in seen:
                    unique_count += math.perm(9 - i, L - 1 - i)
                    
            if curr_digit in seen:
                break
            seen.add(curr_digit)
            
        return n - unique_count
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
- [357. Count Numbers with Unique Digits](../../0001-0500/0357-count-numbers-with-unique-digits/)
- [1295. Find Numbers with Even Number of Digits](../../1001-1500/1295-find-numbers-with-even-number-of-digits/)
- [258. Add Digits](../../0001-0500/0258-add-digits/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/numbers-with-repeated-digits/)
