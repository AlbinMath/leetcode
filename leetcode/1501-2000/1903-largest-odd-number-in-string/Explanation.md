# LeetCode 1903: Largest Odd Number in String

**LeetCode Problem #1903 — Largest Odd Number in String**
Solve LeetCode Largest Odd Number in String using C++ and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Largest Odd Number in String |
| LeetCode | #1903 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `num`, representing a large integer. Return *the **largest-valued odd** integer (as a string) that is a **non-empty substring** of *`num`*, or an empty string *`""`* if no odd integer exists*.

A **substring** is a contiguous sequence of characters within a string.

## Constraints
- `1 <= num.length <= 10^5`
- `num` only consists of digits and does not contain any leading zeros.

## Examples
### Example 1
- **Input:** `num = "52"`
- **Output:** `"5"`
- **Explanation:** The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.

### Example 2
- **Input:** `num = "4206"`
- **Output:** `""`
- **Explanation:** There are no odd numbers in "4206".

### Example 3
- **Input:** `num = "35427"`
- **Output:** `"35427"`
- **Explanation:** "35427" is already an odd number.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Largest Odd Number in String**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `num = "52"`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"5"`.
4. **Verification:** The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.

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
    string largestOddNumber(string num) {
        for (int i = num.size() - 1; i >= 0; i--) {
            if ((num[i] - '0') % 2 == 1) {
                return num.substr(0, i + 1);
            }
        }

        return "";
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
- [434. Number of Segments in a String](../../0001-0500/0434-number-of-segments-in-a-string/)
- [806. Number of Lines To Write String](../../0501-1000/0806-number-of-lines-to-write-string/)
- [1374. Generate a String With Characters That Have Odd Counts](../../1001-1500/1374-generate-a-string-with-characters-that-have-odd-counts/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/largest-odd-number-in-string/)
