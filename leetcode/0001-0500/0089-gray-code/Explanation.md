# LeetCode 89: Gray Code

**LeetCode Problem #89 — Gray Code**
Solve LeetCode Gray Code using JavaScript, Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Gray Code |
| LeetCode | #89 |
| Difficulty | Medium |
| Language | JavaScript, Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
An **n-bit gray code sequence** is a sequence of `2^n` integers where:

Every integer is in the **inclusive** range `[0, 2^n - 1]`, 
 The first integer is `0`, 
 An integer appears **no more than once** in the sequence, 
 The binary representation of every pair of **adjacent** integers differs by **exactly one bit**, and 
 The binary representation of the **first** and **last** integers differs by **exactly one bit**.

Given an integer `n`, return *any valid **n-bit gray code sequence***.

## Constraints
- `1 <= n <= 16`

## Examples
### Example 1
- **Input:** `n = 2`
- **Output:** `[0,1,3,2]`
- **Explanation:** The binary representation of [0,1,3,2] is [00,01,11,10].
- 0 0 and 0 1 differ by one bit
- 0 1 and 1 1 differ by one bit
- 1 1 and 1 0 differ by one bit
- 1 0 and 0 0 differ by one bit
[0,2,3,1] is also a valid gray code sequence, whose binary representation is [00,10,11,01].
- 0 0 and 1 0 differ by one bit
- 1 0 and 1 1 differ by one bit
- 1 1 and 0 1 differ by one bit
- 0 1 and 0 0 differ by one bit

### Example 2
- **Input:** `n = 1`
- **Output:** `[0,1]`

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Gray Code**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 2`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[0,1,3,2]`.
4. **Verification:** The binary representation of [0,1,3,2] is [00,01,11,10].
- 0 0 and 0 1 differ by one bit
- 0 1 and 1 1 differ by one bit
- 1 1 and 1 0 differ by one bit
- 1 0 and 0 0 differ by one bit
[0,2,3,1] is also a valid gray code sequence, whose binary representation is [00,10,11,01].
- 0 0 and 1 0 differ by one bit
- 1 0 and 1 1 differ by one bit
- 1 1 and 0 1 differ by one bit
- 0 1 and 0 0 differ by one bit

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Integer Bitmask.

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### JavaScript
```javascript
var grayCode = function(n) {
    const result = [];
    const total = 1 << n;

    for (let i = 0; i < total; i++) {
        result.push(i ^ (i >> 1));
    }

    return result;
};
```

### Python
```python
class Solution:
    def grayCode(self, n: int) -> list[int]:
        return [i ^ (i >> 1) for i in range(1 << n)]
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
- [804. Unique Morse Code Words](../../0501-1000/0804-unique-morse-code-words/)
- [3606. Coupon Code Validator](../../3501-4000/3606-coupon-code-validator/)
- [8. String to Integer (atoi)](../../0001-0500/0008-string-to-integer-atoi/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/gray-code/)
