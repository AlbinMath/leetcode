# LeetCode 2546: Apply Bitwise Operations to Make Strings Equal

**LeetCode Problem #2546 — Apply Bitwise Operations to Make Strings Equal**
Solve LeetCode Apply Bitwise Operations to Make Strings Equal using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Apply Bitwise Operations to Make Strings Equal |
| LeetCode | #2546 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two **0-indexed binary** strings `s` and `target` of the same length `n`. You can do the following operation on `s` **any** number of times:

Choose two **different** indices `i` and `j` where `0 <= i, j < n`. 
 Simultaneously, replace `s[i]` with (`s[i]` **OR** `s[j]`) and `s[j]` with (`s[i]` **XOR** `s[j]`).

For example, if `s = "0110"`, you can choose `i = 0` and `j = 2`, then simultaneously replace `s[0]` with (`s[0]` **OR** `s[2]` = `0` **OR** `1` = `1`), and `s[2]` with (`s[0]` **XOR** `s[2]` = `0` **XOR** `1` = `1`), so we will have `s = "1110"`.

Return `true` *if you can make the string *`s`* equal to *`target`*, or *`false`* otherwise*.

## Constraints
- `n == s.length == target.length`
- `2 <= n <= 10^5`
- `s` and `target` consist of only the digits `0` and `1`.

## Examples
### Example 1
- **Input:** `s = "1010", target = "0110"`
- **Output:** `true`
- **Explanation:** We can do the following operations:
- Choose i = 2 and j = 0. We have now s = "

### Example 2
- **Input:** `s = "11", target = "00"`
- **Output:** `false`
- **Explanation:** It is not possible to make s equal to target with any number of operations.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Apply Bitwise Operations to Make Strings Equal**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "1010", target = "0110"`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** We can do the following operations:
- Choose i = 2 and j = 0. We have now s = "

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
    def makeStringsEqual(self, s, target):
        return ('1' in s) == ('1' in target)
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
- [3091. Apply Operations to Make Sum of Array Greater Than or Equal to k](../../3001-3500/3091-apply-operations-to-make-sum-of-array-greater-than-or-equal-to-k/)
- [1887. Reduction Operations to Make the Array Elements Equal](../../1501-2000/1887-reduction-operations-to-make-the-array-elements-equal/)
- [2602. Minimum Operations to Make All Array Elements Equal](../../2501-3000/2602-minimum-operations-to-make-all-array-elements-equal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/apply-bitwise-operations-to-make-strings-equal/)
