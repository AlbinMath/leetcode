# LeetCode 13: Roman to Integer

**LeetCode Problem #13 — Roman to Integer**
Solve LeetCode Roman to Integer using Python and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Roman to Integer |
| LeetCode | #13 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.

**Symbol** **Value**
I 1
V 5
X 10
L 50
C 100
D 500
M 1000

For example, `2` is written as `II` in Roman numeral, just two ones added together. `12` is written as `XII`, which is simply `X + II`. The number `27` is written as `XXVII`, which is `XX + V + II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:

`I` can be placed before `V` (5) and `X` (10) to make 4 and 9. 
 `X` can be placed before `L` (50) and `C` (100) to make 40 and 90. 
 `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

## Constraints
- `1 <= s.length <= 15`
- `s` contains only the characters `('I', 'V', 'X', 'L', 'C', 'D', 'M')`.
- It is **guaranteed** that `s` is a valid roman numeral in the range `[1, 3999]`.

## Examples
### Example 1
- **Input:** `s = "III"`
- **Output:** `3`
- **Explanation:** III = 3.

### Example 2
- **Input:** `s = "LVIII"`
- **Output:** `58`
- **Explanation:** L = 50, V= 5, III = 3.

### Example 3
- **Input:** `s = "MCMXCIV"`
- **Output:** `1994`
- **Explanation:** M = 1000, CM = 900, XC = 90 and IV = 4.

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We define a dictionary `values` that maps each Roman numeral character to its corresponding integer value.
We initialize a `total` variable to `0`.
We iterate through the string `s`. For each character at index `i`:
- If there is a next character (`i + 1 < len(s)`) and its value is strictly greater than the current character's value, it represents a subtractive combination (like `IV` or `IX`). We subtract the current character's value from `total`.
- Otherwise, we add the current character's value to `total`.

## Algorithm
1. Initialize state variables / data structure (**Prefix Array**).
2. Process elements sequentially using **Prefix Sum Precomputation**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `s = "III"`.
2. **Processing Steps:** We apply **Prefix Sum Precomputation** using our **Prefix Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** III = 3.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Prefix Array.

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution(object):
    def romanToInt(self, s):
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0

        for i in range(len(s)):
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]

        return total
```

## Why This Works
By utilizing **Prefix Sum**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [12. Integer to Roman](../../0001-0500/0012-integer-to-roman/)
- [7. Reverse Integer](../../0001-0500/0007-reverse-integer/)
- [8. String to Integer (atoi)](../../0001-0500/0008-string-to-integer-atoi/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/roman-to-integer/)
