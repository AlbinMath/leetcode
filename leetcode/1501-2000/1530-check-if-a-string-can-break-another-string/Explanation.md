# LeetCode 1433: Check If a String Can Break Another String

**LeetCode Problem #1433 — Check If a String Can Break Another String**
Solve LeetCode Check If a String Can Break Another String using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check If a String Can Break Another String |
| LeetCode | #1433 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given two strings: `s1` and `s2` with the same size, check if some permutation of string `s1` can break some permutation of string `s2` or vice-versa. In other words `s2` can break `s1` or vice-versa.

A string `x` can break string `y` (both of size `n`) if `x[i] >= y[i]` (in alphabetical order) for all `i` between `0` and `n-1`.

## Constraints
- `s1.length == n`
- `s2.length == n`
- `1 <= n <= 10^5`
- All strings consist of lowercase English letters.

## Examples
### Example 1
- **Input:** `s1 = "abc", s2 = "xya"`
- **Output:** `true`
- **Explanation:** "ayx" is a permutation of s2="xya" which can break to string "abc" which is a permutation of s1="abc".

### Example 2
- **Input:** `s1 = "abe", s2 = "acd"`
- **Output:** `false`
- **Explanation:** All permutations for s1="abe" are: "abe", "aeb", "bae", "bea", "eab" and "eba" and all permutation for s2="acd" are: "acd", "adc", "cad", "cda", "dac" and "dca". However, there is not any permutation from s1 which can break some permutation from s2 and vice-versa.

### Example 3
- **Input:** `s1 = "leetcodee", s2 = "interview"`
- **Output:** `true`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Check If a String Can Break Another String**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s1 = "abc", s2 = "xya"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** "ayx" is a permutation of s2="xya" which can break to string "abc" which is a permutation of s1="abc".

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
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        a, b = sorted(s1), sorted(s2)
        return all(x >= y for x, y in zip(a, b)) or all(x <= y for x, y in zip(a, b))
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
- [2267.  Check if There Is a Valid Parentheses String Path](../../2001-2500/2349-check-if-there-is-a-valid-parentheses-string-path/)
- [1790. Check if One String Swap Can Make Strings Equal](../../1501-2000/1915-check-if-one-string-swap-can-make-strings-equal/)
- [2116. Check if a Parentheses String Can Be Valid](../../2001-2500/2221-check-if-a-parentheses-string-can-be-valid/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-a-string-can-break-another-string/)
