# LeetCode 393: UTF-8 Validation

**LeetCode Problem #393 — UTF-8 Validation**
Solve LeetCode UTF-8 Validation using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | UTF-8 Validation |
| LeetCode | #393 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `data` representing the data, return whether it is a valid **UTF-8** encoding (i.e. it translates to a sequence of valid UTF-8 encoded characters).

A character in **UTF8** can be from **1 to 4 bytes** long, subjected to the following rules:

For a **1-byte** character, the first bit is a `0`, followed by its Unicode code. 
 For an **n-bytes** character, the first `n` bits are all one's, the `n + 1` bit is `0`, followed by `n - 1` bytes with the most significant `2` bits being `10`.

This is how the UTF-8 encoding would work:

Number of Bytes | UTF-8 Octet Sequence
 | (binary)
 --------------------+-----------------------------------------
 1 | 0xxxxxxx
 2 | 110xxxxx 10xxxxxx
 3 | 1110xxxx 10xxxxxx 10xxxxxx
 4 | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

`x` denotes a bit in the binary form of a byte that may be either `0` or `1`.

**Note: **The input is an array of integers. Only the **least significant 8 bits** of each integer is used to store the data. This means each integer represents only 1 byte of data.

## Constraints
- `1 <= data.length <= 2 * 10^4`
- `0 <= data[i] <= 255`

## Examples
### Example 1
- **Input:** `data = [197,130,1]`
- **Output:** `true`
- **Explanation:** data represents the octet sequence: 11000101 10000010 00000001.
It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.

### Example 2
- **Input:** `data = [235,140,4]`
- **Output:** `false`
- **Explanation:** data represented the octet sequence: 11101011 10001100 00000100.
The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
The next byte is a continuation byte which starts with 10 and that's correct.
But the second continuation byte does not start with 10, so it is invalid.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **UTF-8 Validation**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `data = [197,130,1]`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** data represents the octet sequence: 11000101 10000010 00000001.
It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.

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
from typing import List

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        need = 0  # continuation bytes still expected

        for byte in data:
            byte &= 0xFF
            if need == 0:
                if byte >> 7 == 0b0:
                    need = 0
                elif byte >> 5 == 0b110:
                    need = 1
                elif byte >> 4 == 0b1110:
                    need = 2
                elif byte >> 3 == 0b11110:
                    need = 3
                else:
                    return False
            else:
                if byte >> 6 != 0b10:
                    return False
                need -= 1

        return need == 0
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
- [8. String to Integer (atoi)](../../0001-0500/0008-string-to-integer-atoi/)
- [89. Gray Code](../../0001-0500/0089-gray-code/)
- [137. Single Number II](../../0001-0500/0137-single-number-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/utf-8-validation/)
