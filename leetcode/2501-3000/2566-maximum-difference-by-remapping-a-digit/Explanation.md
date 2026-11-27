# LeetCode 2566: Maximum Difference by Remapping a Digit

**LeetCode Problem #2566 — Maximum Difference by Remapping a Digit**
Solve LeetCode Maximum Difference by Remapping a Digit using Python and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Difference by Remapping a Digit |
| LeetCode | #2566 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer `num`. You know that Bob will sneakily **remap** one of the `10` possible digits (`0` to `9`) to another digit.

Return *the difference between the maximum and minimum values Bob can make by remapping **exactly** **one** digit in *`num`.

**Notes:**

When Bob remaps a digit d1 to another digit d2 , Bob replaces all occurrences of `d1` in `num` with `d2`. 
 Bob can remap a digit to itself, in which case `num` does not change. 
 Bob can remap different digits for obtaining minimum and maximum values respectively. 
 The resulting number after remapping can contain leading zeroes.

## Constraints
- `1 <= num <= 10^8`

## Examples
### Example 1
- **Input:** `num = 11891`
- **Output:** `99009`
- **Explanation:** To achieve the maximum value, Bob can remap the digit 1 to the digit 9 to yield 99899.
To achieve the minimum value, Bob can remap the digit 1 to the digit 0, yielding 890.
The difference between these two numbers is 99009.

### Example 2
- **Input:** `num = 90`
- **Output:** `99`
- **Explanation:** The maximum value that can be returned by the function is 99 (if 0 is replaced by 9) and the minimum value that can be returned by the function is 0 (if 9 is replaced by 0).
Thus, we return 99.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Difference by Remapping a Digit**, we observe the problem requirements and utilize the **Math & Logic** technique. We iterate through the inputs using **Mathematical Simulation & Modular Arithmetic**, leveraging a **Primitive Types** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Primitive Types**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `num = 11891`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `99009`.
4. **Verification:** To achieve the maximum value, Bob can remap the digit 1 to the digit 9 to yield 99899.
To achieve the minimum value, Bob can remap the digit 1 to the digit 0, yielding 890.
The difference between these two numbers is 99009.

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
    def minMaxDifference(self, num: int) -> int:
        s = str(num)

        hi = s
        for c in s:
            if c != '9':
                hi = s.replace(c, '9')
                break

        lo = s.replace(s[0], '0')

        return int(hi) - int(lo)
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
- [1026. Maximum Difference Between Node and Ancestor](../../1001-1500/1026-maximum-difference-between-node-and-ancestor/)
- [1913. Maximum Product Difference Between Two Pairs](../../1501-2000/1913-maximum-product-difference-between-two-pairs/)
- [1938. Maximum Genetic Difference Query](../../1501-2000/1938-maximum-genetic-difference-query/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/)
