# LeetCode 2683: Neighboring Bitwise XOR

**LeetCode Problem #2683 — Neighboring Bitwise XOR**
Solve LeetCode Neighboring Bitwise XOR using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Neighboring Bitwise XOR |
| LeetCode | #2683 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A **0-indexed** array `derived` with length `n` is derived by computing the **bitwise XOR** (&oplus;) of adjacent values in a **binary array** `original` of length `n`.

Specifically, for each index `i` in the range `[0, n - 1]`:

If `i = n - 1`, then `derived[i] = original[i] &oplus; original[0]`. 
 Otherwise, `derived[i] = original[i] &oplus; original[i + 1]`.

Given an array `derived`, your task is to determine whether there exists a **valid binary array** `original` that could have formed `derived`.

Return ***true** if such an array exists or **false** otherwise.*

A binary array is an array containing only **0's** and **1's**

## Constraints
- `n == derived.length`
- `1 <= n <= 10^5`
- The values in `derived` are either **0's** or **1's**

## Examples
### Example 1
- **Input:** `derived = [1,1,0]`
- **Output:** `true`
- **Explanation:** A valid original array that gives derived is [0,1,0].
derived[0] = original[0] &oplus; original[1] = 0 &oplus; 1 = 1 
derived[1] = original[1] &oplus; original[2] = 1 &oplus; 0 = 1
derived[2] = original[2] &oplus; original[0] = 0 &oplus; 0 = 0

### Example 2
- **Input:** `derived = [1,1]`
- **Output:** `true`
- **Explanation:** A valid original array that gives derived is [0,1].
derived[0] = original[0] &oplus; original[1] = 1
derived[1] = original[1] &oplus; original[0] = 1

### Example 3
- **Input:** `derived = [1,0]`
- **Output:** `false`
- **Explanation:** There is no valid original array that gives derived.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Neighboring Bitwise XOR**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `derived = [1,1,0]`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** A valid original array that gives derived is [0,1,0].
derived[0] = original[0] &oplus; original[1] = 0 &oplus; 1 = 1 
derived[1] = original[1] &oplus; original[2] = 1 &oplus; 0 = 1
derived[2] = original[2] &oplus; original[0] = 0 &oplus; 0 = 0

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Integer Bitmask.

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution(object):
    def doesValidArrayExist(self, derived):
        x = 0
        for d in derived:
            x ^= d
        return x == 0
```

## Why This Works
By utilizing **Bit Manipulation**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1835. Find XOR Sum of All Pairs Bitwise AND](../../1501-2000/1963-find-xor-sum-of-all-pairs-bitwise-and/)
- [2425. Bitwise XOR of All Pairings](../../2501-3000/2533-bitwise-xor-of-all-pairings/)
- [3702. Longest Subsequence With Non-Zero Bitwise XOR](../../4001-4500/4033-longest-subsequence-with-non-zero-bitwise-xor/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/neighboring-bitwise-xor/)
