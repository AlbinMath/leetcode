# LeetCode 3211: Generate Binary Strings Without Adjacent Zeros

**LeetCode Problem #3211 — Generate Binary Strings Without Adjacent Zeros**
Solve LeetCode Generate Binary Strings Without Adjacent Zeros using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Generate Binary Strings Without Adjacent Zeros |
| LeetCode | #3211 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a positive integer `n`.

A binary string `x` is **valid** if all substrings of `x` of length 2 contain **at least** one `"1"`.

Return all **valid** strings with length `n`**, **in *any* order.

## Constraints
- `1 <= n <= 18`

## Examples
### Example 1
- **Input:** `n = 3`
- **Output:** `["010","011","101","110","111"]`
- **Explanation:** The valid strings of length 3 are: `"010"`, `"011"`, `"101"`, `"110"`, and `"111"`.

### Example 2
- **Input:** `n = 1`
- **Output:** `["0","1"]`
- **Explanation:** The valid strings of length 1 are: `"0"` and `"1"`.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Generate Binary Strings Without Adjacent Zeros**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `["010","011","101","110","111"]`.
4. **Verification:** The valid strings of length 3 are: `"010"`, `"011"`, `"101"`, `"110"`, and `"111"`.

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
from typing import List

class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = []
        path = []

        def dfs(prev_zero: bool) -> None:
            if len(path) == n:
                res.append("".join(path))
                return
            path.append("1")
            dfs(False)
            path.pop()
            if not prev_zero:
                path.append("0")
                dfs(True)
                path.pop()

        dfs(False)
        return res
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
- [3800. Minimum Cost to Make Two Binary Strings Equal](../../3501-4000/3800-minimum-cost-to-make-two-binary-strings-equal/)
- [3955. Valid Binary Strings With Cost Limit](../../3501-4000/3955-valid-binary-strings-with-cost-limit/)
- [3. Longest Substring Without Repeating Characters](../../0001-0500/0003-longest-substring-without-repeating-characters/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/)
