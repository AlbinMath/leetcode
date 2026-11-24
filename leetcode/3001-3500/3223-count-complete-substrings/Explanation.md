# LeetCode 2953: Count Complete Substrings

**LeetCode Problem #2953 — Count Complete Substrings**
Solve LeetCode Count Complete Substrings using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Complete Substrings |
| LeetCode | #2953 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string `word` and an integer `k`.

A substring `s` of `word` is **complete** if:

Each character in `s` occurs **exactly** `k` times. 
 The difference between two adjacent characters is **at most** `2`. That is, for any two adjacent characters `c1` and `c2` in `s`, the absolute difference in their positions in the alphabet is **at most** `2`.

Return *the number of **complete **substrings of* `word`.

A **substring** is a **non-empty** contiguous sequence of characters in a string.

## Constraints
- `1 <= word.length <= 10^5`
- `word` consists only of lowercase English letters.
- `1 <= k <= word.length`

## Examples
### Example 1
- **Input:** `word = "igigee", k = 2`
- **Output:** `3`
- **Explanation:** The complete substrings where each character appears exactly twice and the difference between adjacent characters is at most 2 are:

### Example 2
- **Input:** `word = "aaabbbccc", k = 3`
- **Output:** `6`
- **Explanation:** The complete substrings where each character appears exactly three times and the difference between adjacent characters is at most 2 are:

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Complete Substrings**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `word = "igigee", k = 2`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The complete substrings where each character appears exactly twice and the difference between adjacent characters is at most 2 are:

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Tree / Graph / Grid.

## Pattern
**Tree & Graph**

## Topics
- Tree
- Graph
- DFS
- BFS

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        n = len(word)

        def count_segment(seg: str) -> int:
            m = len(seg)
            res = 0
            for d in range(1, 27):
                w = d * k
                if w > m:
                    break
                cnt = [0] * 26
                good = 0  # letters with count exactly k
                for i in range(m):
                    c = ord(seg[i]) - 97
                    cnt[c] += 1
                    if cnt[c] == k:
                        good += 1
                    elif cnt[c] == k + 1:
                        good -= 1
                    if i >= w:
                        o = ord(seg[i - w]) - 97
                        if cnt[o] == k:
                            good -= 1
                        elif cnt[o] == k + 1:
                            good += 1
                        cnt[o] -= 1
                    if i >= w - 1 and good == d:
                        res += 1
            return res

        ans = 0
        start = 0
        for i in range(1, n + 1):
            if i == n or abs(ord(word[i]) - ord(word[i - 1])) > 2:
                ans += count_segment(word[start:i])
                start = i
        return ans
```

## Why This Works
By utilizing **Tree & Graph**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [222. Count Complete Tree Nodes](../../0001-0500/0222-count-complete-tree-nodes/)
- [2685. Count the Number of Complete Components](../../2501-3000/2793-count-the-number-of-complete-components/)
- [2799. Count Complete Subarrays in an Array](../../2501-3000/2856-count-complete-subarrays-in-an-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-complete-substrings/)
