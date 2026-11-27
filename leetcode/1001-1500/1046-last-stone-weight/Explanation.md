# LeetCode 1046: Last Stone Weight

**LeetCode Problem #1046 — Last Stone Weight**
Solve LeetCode Last Stone Weight using JavaScript, Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Last Stone Weight |
| LeetCode | #1046 |
| Difficulty | Easy |
| Language | JavaScript, Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an array of integers `stones` where `stones[i]` is the weight of the `i^th` stone.

We are playing a game with the stones. On each turn, we choose the **heaviest two stones** and smash them together. Suppose the heaviest two stones have weights `x` and `y` with `x <= y`. The result of this smash is:

If `x == y`, both stones are destroyed, and 
 If `x != y`, the stone of weight `x` is destroyed, and the stone of weight `y` has new weight `y - x`.

At the end of the game, there is **at most one** stone left.

Return *the weight of the last remaining stone*. If there are no stones left, return `0`.

## Constraints
- `1 <= stones.length <= 30`
- `1 <= stones[i] <= 1000`

## Examples
### Example 1
- **Input:** `stones = [2,7,4,1,8,1]`
- **Output:** `1`
- **Explanation:** We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

### Example 2
- **Input:** `stones = [1]`
- **Output:** `1`

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Last Stone Weight**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `stones = [2,7,4,1,8,1]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### JavaScript
```javascript
var lastStoneWeight = function(stones) {
    while (stones.length > 1) {
        stones.sort((a, b) => b - a);

        let y = stones.shift(); // Heaviest stone
        let x = stones.shift(); // Second heaviest stone

        if (y !== x) {
            stones.push(y - x);
        }
    }

    return stones.length === 0 ? 0 : stones[0];
};
```

### Python
```python
import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)

            if y != x:
                heapq.heappush(stones, -(y - x))

        return -stones[0] if stones else 0
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
- [528. Random Pick with Weight](../../0501-1000/0528-random-pick-with-weight/)
- [2846. Minimum Edge Weight Equilibrium Queries in a Tree](../../2501-3000/2846-minimum-edge-weight-equilibrium-queries-in-a-tree/)
- [3419. Minimize the Maximum Edge Weight of Graph](../../3001-3500/3419-minimize-the-maximum-edge-weight-of-graph/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/last-stone-weight/)
