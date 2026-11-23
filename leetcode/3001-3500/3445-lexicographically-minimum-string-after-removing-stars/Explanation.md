# LeetCode 3170: Lexicographically Minimum String After Removing Stars

**LeetCode Problem #3170 — Lexicographically Minimum String After Removing Stars**
Solve LeetCode Lexicographically Minimum String After Removing Stars using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Lexicographically Minimum String After Removing Stars |
| LeetCode | #3170 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s`. It may contain any number of `'*'` characters. Your task is to remove all `'*'` characters.

While there is a `'*'`, do the following operation:

Delete the leftmost `'*'` and the **smallest** non-`'*'` character to its *left*. If there are several smallest characters, you can delete any of them.

Return the lexicographically smallest resulting string after removing all `'*'` characters.

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists only of lowercase English letters and `'*'`.
- The input is generated such that it is possible to delete all `'*'` characters.

## Examples
### Example 1
- **Input:** `s = "aaba*"`
- **Output:** `"aab"`
- **Explanation:** We should delete one of the `'a'` characters with `'*'`. If we choose `s[3]`, `s` becomes the lexicographically smallest.

### Example 2
- **Input:** `s = "abc"`
- **Output:** `"abc"`
- **Explanation:** There is no `'*'` in the string.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Lexicographically Minimum String After Removing Stars**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "aaba*"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"aab"`.
4. **Verification:** We should delete one of the `'a'` characters with `'*'`. If we choose `s[3]`, `s` becomes the lexicographically smallest.

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
    def clearStars(self, s: str) -> str:
        chars = list(s)
        pos = [[] for _ in range(26)]
        
        for i, ch in enumerate(chars):
            if ch == '*':
                for c in range(26):
                    if pos[c]:
                        chars[pos[c].pop()] = '*'
                        break
            else:
                pos[ord(ch) - ord('a')].append(i)
                
        return "".join(ch for ch in chars if ch != '*')
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
- [2696. Minimum String Length After Removing Substrings](../../2501-3000/2800-minimum-string-length-after-removing-substrings/)
- [1750. Minimum Length of String After Deleting Similar Ends](../../1501-2000/1850-minimum-length-of-string-after-deleting-similar-ends/)
- [3746. Minimum String Length After Balanced Removals](../../4001-4500/4090-minimum-string-length-after-balanced-removals/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/)
