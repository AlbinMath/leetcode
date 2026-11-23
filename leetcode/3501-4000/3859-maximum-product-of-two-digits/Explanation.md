# LeetCode 3536: Maximum Product of Two Digits

**LeetCode Problem #3536 — Maximum Product of Two Digits**
Solve LeetCode Maximum Product of Two Digits using Erlang and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Product of Two Digits |
| LeetCode | #3536 |
| Difficulty | Easy |
| Language | Erlang |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a positive integer `n`.

Return the **maximum** product of any two digits in `n`.

**Note:** You may use the **same** digit twice if it appears more than once in `n`.

## Constraints
- `10 <= n <= 10^9`

## Examples
### Example 1
- **Input:** `n = 31`
- **Output:** `3`
- **Explanation:** The digits of `n` are `[3, 1]`. 
 The possible products of any two digits are: `3 * 1 = 3`. 
 The maximum product is 3.

### Example 2
- **Input:** `n = 22`
- **Output:** `4`
- **Explanation:** The digits of `n` are `[2, 2]`. 
 The possible products of any two digits are: `2 * 2 = 4`. 
 The maximum product is 4.

### Example 3
- **Input:** `n = 124`
- **Output:** `8`
- **Explanation:** The digits of `n` are `[1, 2, 4]`. 
 The possible products of any two digits are: `1 * 2 = 2`, `1 * 4 = 4`, `2 * 4 = 8`. 
 The maximum product is 8.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Product of Two Digits**, we observe the problem requirements and utilize the **Math & Logic** technique. We iterate through the inputs using **Mathematical Simulation & Modular Arithmetic**, leveraging a **Primitive Types** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Primitive Types**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 31`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The digits of `n` are `[3, 1]`. 
 The possible products of any two digits are: `3 * 1 = 3`. 
 The maximum product is 3.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
Erlang

## Source Code
- [solution.erl](./solution.erl)


```erlang
-spec max_product(N :: integer()) -> integer().

max_product(N) ->
    Digits = [D - $0 || D <- integer_to_list(N)],
    Sorted = lists:sort(Digits),
    Len = length(Sorted),
    lists:nth(Len, Sorted) * lists:nth(Len - 1, Sorted).
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
- [1464. Maximum Product of Two Elements in an Array](../../1501-2000/1574-maximum-product-of-two-elements-in-an-array/)
- [1913. Maximum Product Difference Between Two Pairs](../../2001-2500/2042-maximum-product-difference-between-two-pairs/)
- [1960. Maximum Product of the Length of Two Palindromic Substrings](../../1001-1500/1336-maximum-product-of-the-length-of-two-palindromic-substrings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-product-of-two-digits/)
