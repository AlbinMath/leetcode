# LeetCode 1784: Check if Binary String Has at Most One Segment of Ones

**LeetCode Problem #1784 — Check if Binary String Has at Most One Segment of Ones**
Solve LeetCode Check if Binary String Has at Most One Segment of Ones using C++ and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check if Binary String Has at Most One Segment of Ones |
| LeetCode | #1784 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a binary string `s` **​​​​​without leading zeros**, return `true`​​​ *if *`s`* contains **at most one contiguous segment of ones***. Otherwise, return `false`.

## Constraints
- `1 <= s.length <= 100`
- `s[i]`​​​​ is either `'0'` or `'1'`.
- `s[0]` is `'1'`.

## Examples
### Example 1
- **Input:** `s = "1001"`
- **Output:** `false`
- **Explanation:** The string has two segments of size 1.

### Example 2
- **Input:** `s = "110"`
- **Output:** `true`

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Check if Binary String Has at Most One Segment of Ones**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "1001"`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `false`.
4. **Verification:** The string has two segments of size 1.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Integer Bitmask.

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    bool checkOnesSegment(string s) {
        for (int i = 1; i < s.length(); i++) {
            if (s[i] == '1' && s[i - 1] == '0') {
                return false;
            }
        }

        return true;
    }
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
- [2267.  Check if There Is a Valid Parentheses String Path](../../2001-2500/2349-check-if-there-is-a-valid-parentheses-string-path/)
- [1461. Check If a String Contains All Binary Codes of Size K](../../1501-2000/1557-check-if-a-string-contains-all-binary-codes-of-size-k/)
- [1790. Check if One String Swap Can Make Strings Equal](../../1501-2000/1915-check-if-one-string-swap-can-make-strings-equal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/)
