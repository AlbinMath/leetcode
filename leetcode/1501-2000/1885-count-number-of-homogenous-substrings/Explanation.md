# LeetCode 1759: Count Number of Homogenous Substrings

**LeetCode Problem #1759 — Count Number of Homogenous Substrings**
Solve LeetCode Count Number of Homogenous Substrings using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Number of Homogenous Substrings |
| LeetCode | #1759 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string `s`, return *the number of **homogenous** substrings of *`s`*.* Since the answer may be too large, return it **modulo** `10^9 + 7`.

A string is **homogenous** if all the characters of the string are the same.

A **substring** is a contiguous sequence of characters within a string.

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists of lowercase letters.

## Examples
### Example 1
- **Input:** `s = "abbcccaa"`
- **Output:** `13`
- **Explanation:** The homogenous substrings are listed as below:
"a" appears 3 times.
"aa" appears 1 time.
"b" appears 2 times.
"bb" appears 1 time.
"c" appears 3 times.
"cc" appears 2 times.
"ccc" appears 1 time.
3 + 1 + 2 + 1 + 3 + 2 + 1 = 13.

### Example 2
- **Input:** `s = "xy"`
- **Output:** `2`
- **Explanation:** The homogenous substrings are "x" and "y".

### Example 3
- **Input:** `s = "zzzzz"`
- **Output:** `15`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Number of Homogenous Substrings**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abbcccaa"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `13`.
4. **Verification:** The homogenous substrings are listed as below:
"a" appears 3 times.
"aa" appears 1 time.
"b" appears 2 times.
"bb" appears 1 time.
"c" appears 3 times.
"cc" appears 2 times.
"ccc" appears 1 time.
3 + 1 + 2 + 1 + 3 + 2 + 1 = 13.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10**9 + 7
        run = 0
        total = 0

        for i, ch in enumerate(s):
            if i > 0 and ch == s[i - 1]:
                run += 1
            else:
                run = 1
            total += run

        return total % MOD
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3234. Count the Number of Substrings With Dominant Ones](../../3001-3500/3479-count-the-number-of-substrings-with-dominant-ones/)
- [696. Count Binary Substrings](../../0501-1000/0696-count-binary-substrings/)
- [828. Count Unique Characters of All Substrings of a Given String](../../0501-1000/0855-count-unique-characters-of-all-substrings-of-a-given-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-number-of-homogenous-substrings/)
