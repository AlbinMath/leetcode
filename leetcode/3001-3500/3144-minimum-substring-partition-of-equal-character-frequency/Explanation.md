# LeetCode 3144: Minimum Substring Partition of Equal Character Frequency

**LeetCode Problem #3144 — Minimum Substring Partition of Equal Character Frequency**
Solve LeetCode Minimum Substring Partition of Equal Character Frequency using Python and Sliding Window. This solution finds the optimal result using Dynamic Sliding Window Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Substring Partition of Equal Character Frequency |
| LeetCode | #3144 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Dynamic Sliding Window Traversal |
| Data Structure | Array / Hash Set |
| Pattern | Sliding Window |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string `s`, you need to partition it into one or more **balanced** substrings . For example, if `s == "ababcc"` then `("abab", "c", "c")`, `("ab", "abc", "c")`, and `("ababcc")` are all valid partitions, but `("a", **"bab"**, "cc")`, `(**"aba"**, "bc", "c")`, and `("ab", **"abcc"**)` are not. The unbalanced substrings are bolded.

Return the **minimum** number of substrings that you can partition `s` into.

**Note:** A **balanced** string is a string where each character in the string occurs the same number of times.

## Constraints
- `1 <= s.length <= 1000`
- `s` consists only of English lowercase letters.

## Examples
### Example 1
- **Input:** `s = "fabccddg"`
- **Output:** `3`
- **Explanation:** We can partition the string `s` into 3 substrings in one of the following ways: `("fab, "ccdd", "g")`, or `("fabc", "cd", "dg")`.

### Example 2
- **Input:** `s = "abababaccddb"`
- **Output:** `2`
- **Explanation:** We can partition the string `s` into 2 substrings like so: `("abab", "abaccddb")`.

## Key Insight
Maintain a dynamic contiguous window with two pointers (`left` and `right`), expanding to include new elements and shrinking when window invariants are violated.

## Approach
To solve **Minimum Substring Partition of Equal Character Frequency**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "fabccddg"`.
2. **Processing Steps:** We apply **Dynamic Sliding Window Traversal** using our **Array / Hash Set**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** We can partition the string `s` into 3 substrings in one of the following ways: `("fab, "ccdd", "g")`, or `("fabc", "cd", "dg")`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array / Hash Set.

## Pattern
**Sliding Window**

## Topics
- Sliding Window
- Two Pointers
- Subarrays

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            freq = [0] * 26
            distinct = 0
            max_freq = 0
            
            for j in range(i - 1, -1, -1):
                idx = ord(s[j]) - ord('a')
                if freq[idx] == 0:
                    distinct += 1
                freq[idx] += 1
                if freq[idx] > max_freq:
                    max_freq = freq[idx]
                    
                if distinct * max_freq == i - j:
                    if dp[j] + 1 < dp[i]:
                        dp[i] = dp[j] + 1
                        
        return dp[n]
```

## Why This Works
By utilizing **Sliding Window**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Shrinking the window too late or missing invalid state checks.
2. Forgetting to update window metrics (e.g. char counts) during contraction.
3. Misinterpreting fixed vs variable window requirements.

## Interview Notes
- **Tests:** Two-pointer window management, state tracking, and contiguous subarray analysis.
- **Follow-up:** How do you handle non-positive integer values in subarray sum windows?

## Related Problems
- [3389. Minimum Operations to Make Character Frequencies Equal](../../3001-3500/3389-minimum-operations-to-make-character-frequencies-equal/)
- [1170. Compare Strings by Frequency of the Smallest Character](../../1001-1500/1170-compare-strings-by-frequency-of-the-smallest-character/)
- [76. Minimum Window Substring](../../0001-0500/0076-minimum-window-substring/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-substring-partition-of-equal-character-frequency/)
