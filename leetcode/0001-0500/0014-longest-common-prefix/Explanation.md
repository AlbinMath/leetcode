# LeetCode 14: Longest Common Prefix

**LeetCode Problem #14 — Longest Common Prefix**
Solve LeetCode Longest Common Prefix using Python and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Common Prefix |
| LeetCode | #14 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

## Constraints
- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i]` consists of only lowercase English letters if it is non-empty.

## Examples
### Example 1
- **Input:** `strs = ["flower","flow","flight"]`
- **Output:** `"fl"`

### Example 2
- **Input:** `strs = ["dog","racecar","car"]`
- **Output:** `""`
- **Explanation:** There is no common prefix among the input strings.

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We assume the first string `strs[0]` is the longest common prefix.
Then, we iterate through the rest of the strings.
For each string, we check if it starts with the current `prefix`.
If it doesn't, we shorten the `prefix` by removing the last character (`prefix[:-1]`) until the string starts with the prefix.
If at any point the `prefix` becomes empty, it means there is no common prefix among the strings, and we can immediately return `""`.
If the loop finishes, we return the remaining `prefix`.

## Algorithm
1. Initialize state variables / data structure (**Prefix Array**).
2. Process elements sequentially using **Prefix Sum Precomputation**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `strs = ["flower","flow","flight"]`.
2. **Processing Steps:** We apply **Prefix Sum Precomputation** using our **Prefix Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"fl"`.

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
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        p = strs[0]
        for s in strs[1:]:
            while not s.startswith(p):
                p = p[:-1]
                if not p:
                    return ""
        return p
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
- [3043. Find the Length of the Longest Common Prefix](../../3001-3500/3329-find-the-length-of-the-longest-common-prefix/)
- [3485. Longest Common Prefix of K Strings After Removal](../../3501-4000/3784-longest-common-prefix-of-k-strings-after-removal/)
- [1143. Longest Common Subsequence](../../1001-1500/1250-longest-common-subsequence/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-common-prefix/)
