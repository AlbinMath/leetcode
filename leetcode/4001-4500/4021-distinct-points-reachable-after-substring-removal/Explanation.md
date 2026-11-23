# LeetCode 3694: Distinct Points Reachable After Substring Removal

**LeetCode Problem #3694 — Distinct Points Reachable After Substring Removal**
Solve LeetCode Distinct Points Reachable After Substring Removal using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Distinct Points Reachable After Substring Removal |
| LeetCode | #3694 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string `s` consisting of characters `'U'`, `'D'`, `'L'`, and `'R'`, representing moves on an infinite 2D Cartesian grid.

`'U'`: Move from `(x, y)` to `(x, y + 1)`. 
 `'D'`: Move from `(x, y)` to `(x, y - 1)`. 
 `'L'`: Move from `(x, y)` to `(x - 1, y)`. 
 `'R'`: Move from `(x, y)` to `(x + 1, y)`.

You are also given a positive integer `k`.

You **must** choose and remove **exactly one** contiguous substring of length `k` from `s`. Then, start from coordinate `(0, 0)` and perform the remaining moves in order.

Return an integer denoting the number of **distinct** final coordinates reachable.

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists of only `'U'`, `'D'`, `'L'`, and `'R'`.
- `1 <= k <= s.length`

## Examples
### Example 1
- **Input:** `s = "LUL", k = 1`
- **Output:** `2`
- **Explanation:** After removing a substring of length 1, `s` can be `"UL"`, `"LL"` or `"LU"`. Following these moves, the final coordinates will be `(-1, 1)`, `(-2, 0)` and `(-1, 1)` respectively. There are two distinct points `(-1, 1)` and `(-2, 0)` so the answer is 2.

### Example 2
- **Input:** `s = "UDLR", k = 4`
- **Output:** `1`
- **Explanation:** After removing a substring of length 4, `s` can only be the empty string. The final coordinates will be `(0, 0)`. There is only one distinct point `(0, 0)` so the answer is 1.

### Example 3
- **Input:** `s = "UU", k = 1`
- **Output:** `1`
- **Explanation:** After removing a substring of length 1, `s` becomes `"U"`, which always ends at `(0, 1)`, so there is only one distinct final coordinate.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Distinct Points Reachable After Substring Removal**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "LUL", k = 1`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** After removing a substring of length 1, `s` can be `"UL"`, `"LL"` or `"LU"`. Following these moves, the final coordinates will be `(-1, 1)`, `(-2, 0)` and `(-1, 1)` respectively. There are two distinct points `(-1, 1)` and `(-2, 0)` so the answer is 2.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        n = len(s)
        d = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
        px = [0] * (n + 1)
        py = [0] * (n + 1)
        for i, ch in enumerate(s):
            dx, dy = d[ch]
            px[i + 1] = px[i] + dx
            py[i + 1] = py[i] + dy

        X, Y = px[n], py[n]
        seen = set()
        for i in range(n - k + 1):
            seen.add((X - (px[i + k] - px[i]), Y - (py[i + k] - py[i])))
        return len(seen)
```

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2458. Height of Binary Tree After Subtree Removal Queries](../../2501-3000/2545-height-of-binary-tree-after-subtree-removal-queries/)
- [3485. Longest Common Prefix of K Strings After Removal](../../3501-4000/3784-longest-common-prefix-of-k-strings-after-removal/)
- [1946. Largest Number After Mutating Substring](../../2001-2500/2077-largest-number-after-mutating-substring/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/distinct-points-reachable-after-substring-removal/)
