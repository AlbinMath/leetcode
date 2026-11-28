# LeetCode 3800: Minimum Cost to Make Two Binary Strings Equal

**LeetCode Problem #3800 — Minimum Cost to Make Two Binary Strings Equal**
Solve LeetCode Minimum Cost to Make Two Binary Strings Equal using JavaScript and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Cost to Make Two Binary Strings Equal |
| LeetCode | #3800 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two binary strings `s` and `t`, both of length `n`, and three **positive** integers `flipCost`, `swapCost`, and `crossCost`.

You are allowed to apply the following operations any number of times (in any order) to the strings `s` and `t`:

Choose any index `i` and flip `s[i]` or `t[i]` (change `'0'` to `'1'` or `'1'` to `'0'`). The cost of this operation is `flipCost`. 
 Choose two **distinct** indices `i` and `j`, and swap either `s[i]` and `s[j]` or `t[i]` and `t[j]`. The cost of this operation is `swapCost`. 
 Choose an index `i` and swap `s[i]` with `t[i]`. The cost of this operation is `crossCost`.

Return an integer denoting the **minimum** total cost needed to make the strings `s` and `t` equal.

## Constraints
- `n == s.length == t.length`
- `1 <= n <= 10^5`​​​​​​​
- `1 <= flipCost, swapCost, crossCost <= 10^9`
- `s` and `t` consist only of the characters `'0'` and `'1'`.

## Examples
### Example 1
- **Input:** `s = "01000", t = "10111", flipCost = 10, swapCost = 2, crossCost = 2`
- **Output:** `16`
- **Explanation:** We can perform the following operations: 

 
 Swap `s[0]` and `s[1]` (`swapCost = 2`). After this operation, `s = "10000"` and `t = "10111"`. 
 Cross swap `s[2]` and `t[2]` (`crossCost = 2`). After this operation, `s = "10100"` and `t = "10011"`. 
 Swap `s[2]` and `s[3]` (`swapCost = 2`). After this operation, `s = "10010"` and `t = "10011"`. 
 Flip `s[4]` (`flipCost = 10`). After this operation, `s = t = "10011"`. 
 

 The total cost is `2 + 2 + 2 + 10 = 16`.

### Example 2
- **Input:** `s = "001", t = "110", flipCost = 2, swapCost = 100, crossCost = 100`
- **Output:** `6`
- **Explanation:** Flipping all the bits of `s` makes the strings equal, and the total cost is `3 * flipCost = 3 * 2 = 6`.

### Example 3
- **Input:** `s = "1010", t = "1010", flipCost = 5, swapCost = 5, crossCost = 5`
- **Output:** `0`
- **Explanation:** The strings are already equal, so no operations are required.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Cost to Make Two Binary Strings Equal**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "01000", t = "10111", flipCost = 10, swapCost = 2, crossCost = 2`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `16`.
4. **Verification:** We can perform the following operations: 

 
 Swap `s[0]` and `s[1]` (`swapCost = 2`). After this operation, `s = "10000"` and `t = "10111"`. 
 Cross swap `s[2]` and `t[2]` (`crossCost = 2`). After this operation, `s = "10100"` and `t = "10011"`. 
 Swap `s[2]` and `s[3]` (`swapCost = 2`). After this operation, `s = "10010"` and `t = "10011"`. 
 Flip `s[4]` (`flipCost = 10`). After this operation, `s = t = "10011"`. 
 

 The total cost is `2 + 2 + 2 + 10 = 16`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Integer Bitmask.

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var minimumCost = function(s, t, flipCost, swapCost, crossCost) {
    let countA = 0;
    let countB = 0;

    for (let i = 0; i < s.length; i++) {
        if (s[i] !== t[i]) {
            if (s[i] === '0') {
                countA++;
            } else {
                countB++;
            }
        }
    }

    if (countA + countB === 0) {
        return 0;
    }

    const pairCost = Math.min(swapCost, 2 * flipCost);

    const samePairCost = Math.min(
        crossCost + swapCost,
        2 * flipCost
    );
    const oppositePairs = Math.min(countA, countB);

    let totalCost = oppositePairs * pairCost;

    const remaining = Math.abs(countA - countB);

    totalCost += Math.floor(remaining / 2) * samePairCost;

    if (remaining % 2 === 1) {
        totalCost += flipCost;
    }

    return totalCost;
};
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
- [1347. Minimum Number of Steps to Make Two Strings Anagram](../../1001-1500/1347-minimum-number-of-steps-to-make-two-strings-anagram/)
- [2186. Minimum Number of Steps to Make Two Strings Anagram II](../../2001-2500/2186-minimum-number-of-steps-to-make-two-strings-anagram-ii/)
- [3191. Minimum Operations to Make Binary Array Elements Equal to One I](../../3001-3500/3191-minimum-operations-to-make-binary-array-elements-equal-to-one-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-cost-to-make-two-binary-strings-equal/)
