# LeetCode 191: Number of 1 Bits

**LeetCode Problem #191 — Number of 1 Bits**
Solve LeetCode Number of 1 Bits using JavaScript, Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of 1 Bits |
| LeetCode | #191 |
| Difficulty | Easy |
| Language | JavaScript, Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a positive integer `n`, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight ).

## Constraints
- `1 <= n <= 2^31 - 1`

## Examples
### Example 1
- **Input:** `n = 11`
- **Output:** `3`
- **Explanation:** The input binary string

### Example 2
- **Input:** `n = 128`
- **Output:** `1`
- **Explanation:** The input binary string

### Example 3
- **Input:** `n = 2147483645`
- **Output:** `30`
- **Explanation:** The input binary string

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Number of 1 Bits**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 11`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The input binary string

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
var hammingWeight = function(n) {
    let count = 0;

    while (n !== 0) {
        n = n & (n - 1);
        count++;
    }

    return count;
};
```

### Python
```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
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
- [1356. Sort Integers by The Number of 1 Bits](../../1001-1500/1356-sort-integers-by-the-number-of-1-bits/)
- [693. Binary Number with Alternating Bits](../../0501-1000/0693-binary-number-with-alternating-bits/)
- [762. Prime Number of Set Bits in Binary Representation](../../0501-1000/0762-prime-number-of-set-bits-in-binary-representation/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-1-bits/)
