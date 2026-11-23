# LeetCode 761: Special Binary String

**LeetCode Problem #761 — Special Binary String**
Solve LeetCode Special Binary String using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Special Binary String |
| LeetCode | #761 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
**Special binary strings** are binary strings with the following two properties:

The number of `0`'s is equal to the number of `1`'s. 
 Every prefix of the binary string has at least as many `1`'s as `0`'s.

You are given a **special binary** string `s`.

A move consists of choosing two consecutive, non-empty, special substrings of `s`, and swapping them. Two strings are consecutive if the last character of the first string is exactly one index before the first character of the second string.

Return *the lexicographically largest resulting string possible after applying the mentioned operations on the string*.

## Constraints
- `1 <= s.length <= 50`
- `s[i]` is either `'0'` or `'1'`.
- `s` is a special binary string.

## Examples
### Example 1
- **Input:** `s = "11011000"`
- **Output:** `"11100100"`
- **Explanation:** The strings "10" [occuring at s[1]] and "1100" [at s[3]] are swapped.
This is the lexicographically largest string possible after some number of swaps.

### Example 2
- **Input:** `s = "10"`
- **Output:** `"10"`

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Special Binary String**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "11011000"`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"11100100"`.
4. **Verification:** The strings "10" [occuring at s[1]] and "1100" [at s[3]] are swapped.
This is the lexicographically largest string possible after some number of swaps.

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
    def makeLargestSpecial(self, s: str) -> str:
        parts = []
        balance = 0
        start = 0
        for i, ch in enumerate(s):
            balance += 1 if ch == '1' else -1
            if balance == 0:
                inner = self.makeLargestSpecial(s[start + 1:i])
                parts.append('1' + inner + '0')
                start = i + 1
        parts.sort(reverse=True)
        return ''.join(parts)
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
- [1582. Special Positions in a Binary Matrix](../../1501-2000/1704-special-positions-in-a-binary-matrix/)
- [3085. Minimum Deletions to Make String K-Special](../../3001-3500/3360-minimum-deletions-to-make-string-k-special/)
- [3612. Process String with Special Operations I](../../3501-4000/3931-process-string-with-special-operations-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/special-binary-string/)
