# LeetCode 1404: Number of Steps to Reduce a Number in Binary Representation to One

**LeetCode Problem #1404 — Number of Steps to Reduce a Number in Binary Representation to One**
Solve LeetCode Number of Steps to Reduce a Number in Binary Representation to One using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Steps to Reduce a Number in Binary Representation to One |
| LeetCode | #1404 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given the binary representation of an integer as a string `s`, return *the number of steps to reduce it to *`1`* under the following rules*:

If the current number is even, you have to divide it by `2`.

If the current number is odd, you have to add `1` to it.

It is guaranteed that you can always reach one for all test cases.

## Constraints
- `1 <= s.length <= 500`
- `s` consists of characters '0' or '1'
- `s[0] == '1'`

## Examples
### Example 1
- **Input:** `s = "1101"`
- **Output:** `6`
- **Explanation:** "1101" corressponds to number 13 in their decimal representation.
Step 1) 13 is odd, add 1 and obtain 14. 
Step 2) 14 is even, divide by 2 and obtain 7.
Step 3) 7 is odd, add 1 and obtain 8.
Step 4) 8 is even, divide by 2 and obtain 4. 
Step 5) 4 is even, divide by 2 and obtain 2. 
Step 6) 2 is even, divide by 2 and obtain 1.

### Example 2
- **Input:** `s = "10"`
- **Output:** `1`
- **Explanation:** "10" corresponds to number 2 in their decimal representation.
Step 1) 2 is even, divide by 2 and obtain 1.

### Example 3
- **Input:** `s = "1"`
- **Output:** `0`

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Number of Steps to Reduce a Number in Binary Representation to One**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "1101"`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** "1101" corressponds to number 13 in their decimal representation.
Step 1) 13 is odd, add 1 and obtain 14. 
Step 2) 14 is even, divide by 2 and obtain 7.
Step 3) 7 is odd, add 1 and obtain 8.
Step 4) 8 is even, divide by 2 and obtain 4. 
Step 5) 4 is even, divide by 2 and obtain 2. 
Step 6) 2 is even, divide by 2 and obtain 1.

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
class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0
        for i in range(len(s) - 1, 0, -1):
            if int(s[i]) + carry == 1:
                steps += 2
                carry = 1
            else:
                steps += 1
        return steps + carry
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
- [762. Prime Number of Set Bits in Binary Representation](../../0501-1000/0762-prime-number-of-set-bits-in-binary-representation/)
- [1342. Number of Steps to Reduce a Number to Zero](../../1001-1500/1342-number-of-steps-to-reduce-a-number-to-zero/)
- [233. Number of Digit One](../../0001-0500/0233-number-of-digit-one/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/)
