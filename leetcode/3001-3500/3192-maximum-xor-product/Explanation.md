# LeetCode 2939: Maximum Xor Product

**LeetCode Problem #2939 — Maximum Xor Product**
Solve LeetCode Maximum Xor Product using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Xor Product |
| LeetCode | #2939 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given three integers `a`, `b`, and `n`, return *the **maximum value** of* `(a XOR x) * (b XOR x)` *where* `0 <= x < 2^n`.

Since the answer may be too large, return it **modulo** `10^9 + 7`.

**Note** that `XOR` is the bitwise XOR operation.

## Constraints
- `0 <= a, b < 2^50`
- `0 <= n <= 50`

## Examples
### Example 1
- **Input:** `a = 12, b = 5, n = 4`
- **Output:** `98`
- **Explanation:** For x = 2, (a XOR x) = 14 and (b XOR x) = 7. Hence, (a XOR x) * (b XOR x) = 98. 
It can be shown that 98 is the maximum value of (a XOR x) * (b XOR x) for all 0 <= x < 2^n .

### Example 2
- **Input:** `a = 6, b = 7 , n = 5`
- **Output:** `930`
- **Explanation:** For x = 25, (a XOR x) = 31 and (b XOR x) = 30. Hence, (a XOR x) * (b XOR x) = 930.
It can be shown that 930 is the maximum value of (a XOR x) * (b XOR x) for all 0 <= x < 2^n.

### Example 3
- **Input:** `a = 1, b = 6, n = 3`
- **Output:** `12`
- **Explanation:** For x = 5, (a XOR x) = 4 and (b XOR x) = 3. Hence, (a XOR x) * (b XOR x) = 12.
It can be shown that 12 is the maximum value of (a XOR x) * (b XOR x) for all 0 <= x < 2^n.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Xor Product**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `a = 12, b = 5, n = 4`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `98`.
4. **Verification:** For x = 2, (a XOR x) = 14 and (b XOR x) = 7. Hence, (a XOR x) * (b XOR x) = 98. 
It can be shown that 98 is the maximum value of (a XOR x) * (b XOR x) for all 0 <= x < 2^n .

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
    def maximumXorProduct(self, a, b, n):
        MOD = 10**9 + 7
        A = (a >> n) << n
        B = (b >> n) << n
        for i in range(n - 1, -1, -1):
            ai = (a >> i) & 1
            bi = (b >> i) & 1
            if ai == bi:
                A |= 1 << i
                B |= 1 << i
            elif A <= B:
                A |= 1 << i
            else:
                B |= 1 << i
        return (A * B) % MOD
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
- [421. Maximum XOR of Two Numbers in an Array](../../0001-0500/0421-maximum-xor-of-two-numbers-in-an-array/)
- [1707. Maximum XOR With an Element From Array](../../1501-2000/1826-maximum-xor-with-an-element-from-array/)
- [1829. Maximum XOR for Each Query](../../1501-2000/1940-maximum-xor-for-each-query/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-xor-product/)
