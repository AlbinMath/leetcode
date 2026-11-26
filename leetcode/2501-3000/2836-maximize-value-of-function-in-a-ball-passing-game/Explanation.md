# LeetCode 2836: Maximize Value of Function in a Ball Passing Game

**LeetCode Problem #2836 — Maximize Value of Function in a Ball Passing Game**
Solve LeetCode Maximize Value of Function in a Ball Passing Game using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximize Value of Function in a Ball Passing Game |
| LeetCode | #2836 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `receiver` of length `n` and an integer `k`. `n` players are playing a ball-passing game.

You choose the starting player, `i`. The game proceeds as follows: player `i` passes the ball to player `receiver[i]`, who then passes it to `receiver[receiver[i]]`, and so on, for `k` passes in total. The game's score is the sum of the indices of the players who touched the ball, including repetitions, i.e. `i + receiver[i] + receiver[receiver[i]] + ... + receiver^(k)[i]`.

Return the **maximum** possible score.

**Notes:**

`receiver` may contain duplicates. 
 `receiver[i]` may be equal to `i`.

## Constraints
- `1 <= receiver.length == n <= 10^5`
- `0 <= receiver[i] <= n - 1`
- `1 <= k <= 10^10`

## Examples
### Example 1
- **Input:** `receiver = [2,0,1], k = 4`
- **Output:** `6`
- **Explanation:** Starting with player `i = 2` the initial score is 2: 

 
 
 
 Pass 
 Sender Index 
 Receiver Index 
 Score 
 
 
 1 
 2 
 1 
 3 
 
 
 2 
 1 
 0 
 3 
 
 
 3 
 0 
 2 
 5 
 
 
 4 
 2 
 1 
 6

### Example 2
- **Input:** `receiver = [1,1,1,2,3], k = 3`
- **Output:** `10`
- **Explanation:** Starting with player `i = 4` the initial score is 4: 

 
 
 
 Pass 
 Sender Index 
 Receiver Index 
 Score 
 
 
 1 
 4 
 3 
 7 
 
 
 2 
 3 
 2 
 9 
 
 
 3 
 2 
 1 
 10

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximize Value of Function in a Ball Passing Game**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `receiver = [2,0,1], k = 4`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** Starting with player `i = 2` the initial score is 2: 

 
 
 
 Pass 
 Sender Index 
 Receiver Index 
 Score 
 
 
 1 
 2 
 1 
 3 
 
 
 2 
 1 
 0 
 3 
 
 
 3 
 0 
 2 
 5 
 
 
 4 
 2 
 1 
 6

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
import numpy as np

class Solution(object):
    def getMaxFunctionValue(self, receiver, k):
        n = len(receiver)
        LOG = k.bit_length()

        up = np.array(receiver, dtype=np.int64)
        sm = up.copy()                      # sum of the next 2^0 = 1 player
        cur = np.arange(n, dtype=np.int64)  # current position for every start
        score = cur.copy()                  # the starting index counts

        for j in range(LOG):
            if (k >> j) & 1:
                score += sm[cur]
                cur = up[cur]
            # build level j+1
            sm = sm + sm[up]
            up = up[up]

        return int(score.max())
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
- [1521. Find a Value of a Mysterious Function Closest to Target](../../1501-2000/1521-find-a-value-of-a-mysterious-function-closest-to-target/)
- [3449. Maximize the Minimum Game Score](../../3001-3500/3449-maximize-the-minimum-game-score/)
- [396. Rotate Function](../../0001-0500/0396-rotate-function/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximize-value-of-function-in-a-ball-passing-game/)
