# LeetCode 1411: Number of Ways to Paint N × 3 Grid

**LeetCode Problem #1411 — Number of Ways to Paint N × 3 Grid**
Solve LeetCode Number of Ways to Paint N × 3 Grid using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Ways to Paint N × 3 Grid |
| LeetCode | #1411 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You have a `grid` of size `n x 3` and you want to paint each cell of the grid with exactly one of the three colors: **Red**, **Yellow,** or **Green** while making sure that no two adjacent cells have the same color (i.e., no two cells that share vertical or horizontal sides have the same color).

Given `n` the number of rows of the grid, return *the number of ways* you can paint this `grid`. As the answer may grow large, the answer **must be** computed modulo `10^9 + 7`.

## Constraints
- `n == grid.length`
- `1 <= n <= 5000`

## Examples
### Example 1
- **Input:** `n = 1`
- **Output:** `12`
- **Explanation:** There are 12 possible way to paint the grid as shown.

### Example 2
- **Input:** `n = 5000`
- **Output:** `30228214`

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Number of Ways to Paint N × 3 Grid**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 1`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `12`.
4. **Verification:** There are 12 possible way to paint the grid as shown.

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
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        
        aba = 6
        abc = 6
        
        for _ in range(1, n):
            aba, abc = (
                (3 * aba + 2 * abc) % MOD,
                (2 * aba + 2 * abc) % MOD
            )
            
        return (aba + abc) % MOD
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
- [1269. Number of Ways to Stay in the Same Place After Some Steps](../../1001-1500/1269-number-of-ways-to-stay-in-the-same-place-after-some-steps/)
- [1434. Number of Ways to Wear Different Hats to Each Other](../../1001-1500/1434-number-of-ways-to-wear-different-hats-to-each-other/)
- [1444. Number of Ways of Cutting a Pizza](../../1001-1500/1444-number-of-ways-of-cutting-a-pizza/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/)
