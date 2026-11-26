# LeetCode 1864: Minimum Number of Swaps to Make the Binary String Alternating

**LeetCode Problem #1864 — Minimum Number of Swaps to Make the Binary String Alternating**
Solve LeetCode Minimum Number of Swaps to Make the Binary String Alternating using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Number of Swaps to Make the Binary String Alternating |
| LeetCode | #1864 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a binary string `s`, return *the **minimum** number of character swaps to make it **alternating**, or *`-1`* if it is impossible.*

The string is called **alternating** if no two adjacent characters are equal. For example, the strings `"010"` and `"1010"` are alternating, while the string `"0100"` is not.

Any two characters may be swapped, even if they are **not adjacent**.

## Constraints
- `1 <= s.length <= 1000`
- `s[i]` is either `'0'` or `'1'`.

## Examples
### Example 1
- **Input:** `s = "111000"`
- **Output:** `1`
- **Explanation:** Swap positions 1 and 4: "1 1 10 0 0" -> "1 0 10 1 0"
The string is now alternating.

### Example 2
- **Input:** `s = "010"`
- **Output:** `0`
- **Explanation:** The string is already alternating, no swaps are needed.

### Example 3
- **Input:** `s = "1110"`
- **Output:** `-1`

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Number of Swaps to Make the Binary String Alternating**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "111000"`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** Swap positions 1 and 4: "1 1 10 0 0" -> "1 0 10 1 0"
The string is now alternating.

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
    def minSwaps(self, s: str) -> int:
        n = len(s)
        ones = s.count('1')
        zeros = n - ones

        if abs(ones - zeros) > 1:
            return -1

        # mismatches against the target that starts with '0': 0101...
        mis0 = sum(1 for i, ch in enumerate(s) if ch != str(i % 2))
        # mismatches against the target that starts with '1': 1010...
        mis1 = n - mis0

        if ones > zeros:
            return mis1 // 2   # '1' must be at even indices
        if zeros > ones:
            return mis0 // 2   # '0' must be at even indices
        return min(mis0, mis1) // 2
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
- [1888. Minimum Number of Flips to Make the Binary String Alternating](../../1501-2000/1888-minimum-number-of-flips-to-make-the-binary-string-alternating/)
- [1758. Minimum Changes To Make Alternating Binary String](../../1501-2000/1758-minimum-changes-to-make-alternating-binary-string/)
- [1963. Minimum Number of Swaps to Make the String Balanced](../../1501-2000/1963-minimum-number-of-swaps-to-make-the-string-balanced/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/)
