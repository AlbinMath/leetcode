# LeetCode 3084: Count Substrings Starting and Ending with Given Character

**LeetCode Problem #3084 — Count Substrings Starting and Ending with Given Character**
Solve LeetCode Count Substrings Starting and Ending with Given Character using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Substrings Starting and Ending with Given Character |
| LeetCode | #3084 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s` and a character `c`. Return *the total number of substrings of *`s`* that start and end with *`c`*.*

## Constraints
- `1 <= s.length <= 10^5`
- `s` and `c` consist only of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "abada", c = "a"`
- **Output:** `6`
- **Explanation:** Substrings starting and ending with `"a"` are: "

### Example 2
- **Input:** `s = "zzz", c = "z"`
- **Output:** `6`
- **Explanation:** There are a total of `6` substrings in `s` and all start and end with `"z"`.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Substrings Starting and Ending with Given Character**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abada", c = "a"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** Substrings starting and ending with `"a"` are: "

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
    def countSubstrings(self, s: str, c: str) -> int:
        k = s.count(c)
        return k * (k + 1) // 2
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
- [1638. Count Substrings That Differ by One Character](../../1501-2000/1638-count-substrings-that-differ-by-one-character/)
- [828. Count Unique Characters of All Substrings of a Given String](../../0501-1000/0828-count-unique-characters-of-all-substrings-of-a-given-string/)
- [3393. Count Paths With the Given XOR Value](../../3001-3500/3393-count-paths-with-the-given-xor-value/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-substrings-starting-and-ending-with-given-character/)
