# LeetCode 3226: Number of Bit Changes to Make Two Integers Equal

**LeetCode Problem #3226 — Number of Bit Changes to Make Two Integers Equal**
Solve LeetCode Number of Bit Changes to Make Two Integers Equal using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Bit Changes to Make Two Integers Equal |
| LeetCode | #3226 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two positive integers `n` and `k`.

You can choose **any** bit in the **binary representation** of `n` that is equal to 1 and change it to 0.

Return the *number of changes* needed to make `n` equal to `k`. If it is impossible, return -1.

## Constraints
- `1 <= n, k <= 10^6`

## Examples
### Example 1
- **Input:** `n = 13, k = 4`
- **Output:** `2`
- **Explanation:** Initially, the binary representations of `n` and `k` are `n = (1101)_2` and `k = (0100)_2`. 
We can change the first and fourth bits of `n`. The resulting integer is n = (

### Example 2
- **Input:** `n = 21, k = 21`
- **Output:** `0`
- **Explanation:** `n` and `k` are already equal, so no changes are needed.

### Example 3
- **Input:** `n = 14, k = 13`
- **Output:** `-1`
- **Explanation:** It is not possible to make `n` equal to `k`.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Number of Bit Changes to Make Two Integers Equal**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 13, k = 4`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** Initially, the binary representations of `n` and `k` are `n = (1101)_2` and `k = (0100)_2`. 
We can change the first and fourth bits of `n`. The resulting integer is n = (

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
    def minChanges(self, n, k):
        if n & k != k:
            return -1
        return bin(n ^ k).count('1')
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
- [3377. Digit Operations to Make Two Integers Equal](../../3001-3500/3377-digit-operations-to-make-two-integers-equal/)
- [1611. Minimum One Bit Operations to Make Integers Zero](../../1501-2000/1611-minimum-one-bit-operations-to-make-integers-zero/)
- [3621. Number of Integers With Popcount-Depth Equal to K I](../../3501-4000/3621-number-of-integers-with-popcount-depth-equal-to-k-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-bit-changes-to-make-two-integers-equal/)
