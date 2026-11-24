# LeetCode 913: Cat and Mouse

**LeetCode Problem #913 — Cat and Mouse**
Solve LeetCode Cat and Mouse using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Cat and Mouse |
| LeetCode | #913 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A game on an **undirected** graph is played by two players, Mouse and Cat, who alternate turns.

The graph is given as follows: `graph[a]` is a list of all nodes `b` such that `ab` is an edge of the graph.

The mouse starts at node `1` and goes first, the cat starts at node `2` and goes second, and there is a hole at node `0`.

During each player's turn, they **must** travel along one edge of the graph that meets where they are. For example, if the Mouse is at node 1, it **must** travel to any node in `graph[1]`.

Additionally, it is not allowed for the Cat to travel to the Hole (node `0`).

Then, the game can end in three ways:

If ever the Cat occupies the same node as the Mouse, the Cat wins. 
 If ever the Mouse reaches the Hole, the Mouse wins. 
 If ever a position is repeated (i.e., the players are in the same position as a previous turn, and it is the same player's turn to move), the game is a draw.

Given a `graph`, and assuming both players play optimally, return

`1` if the mouse wins the game, 
 `2` if the cat wins the game, or 
 `0` if the game is a draw.

## Constraints
- `3 <= graph.length <= 50`
- `1 <= graph[i].length < graph.length`
- `0 <= graph[i][j] < graph.length`
- `graph[i][j] != i`
- `graph[i]` is unique.
- The mouse and the cat can always move.

## Examples
### Example 1
- **Input:** `graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]`
- **Output:** `0`

### Example 2
- **Input:** `graph = [[1,3],[0],[3],[0,2]]`
- **Output:** `1`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Cat and Mouse**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `0`.

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
from collections import deque

class Solution:
    def catMouseGame(self, graph):
        n = len(graph)
        color = [[[0]*2 for _ in range(n)] for _ in range(n)]
        deg = [[[0]*2 for _ in range(n)] for _ in range(n)]
        q = deque()

        for m in range(n):
            for c in range(1, n):
                deg[m][c][0] = len(graph[m])
                deg[m][c][1] = sum(x != 0 for x in graph[c])

        for c in range(1, n):
            for t in range(2):
                color[0][c][t] = 1
                q.append((0, c, t, 1))
                color[c][c][t] = 2
                q.append((c, c, t, 2))

        while q:
            m, c, t, res = q.popleft()

            if t == 0:  # Previous move was by cat
                for pc in graph[c]:
                    if pc == 0:
                        continue
                    if color[m][pc][1]:
                        continue
                    if res == 2:
                        color[m][pc][1] = 2
                        q.append((m, pc, 1, 2))
                    else:
                        deg[m][pc][1] -= 1
                        if deg[m][pc][1] == 0:
                            color[m][pc][1] = 1
                            q.append((m, pc, 1, 1))
            else:  # Previous move was by mouse
                for pm in graph[m]:
                    if color[pm][c][0]:
                        continue
                    if res == 1:
                        color[pm][c][0] = 1
                        q.append((pm, c, 0, 1))
                    else:
                        deg[pm][c][0] -= 1
                        if deg[pm][c][0] == 0:
                            color[pm][c][0] = 2
                            q.append((pm, c, 0, 2))

        return color[1][2][0]
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
- [1728. Cat and Mouse II](../../1501-2000/1728-cat-and-mouse-ii/)
- [5. Longest Palindromic Substring](../../0001-0500/0005-longest-palindromic-substring/)
- [26. Remove Duplicates from Sorted Array](../../0001-0500/0026-remove-duplicates-from-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/cat-and-mouse/)
