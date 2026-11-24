# LeetCode 1319: Number of Operations to Make Network Connected

**LeetCode Problem #1319 — Number of Operations to Make Network Connected**
Solve LeetCode Number of Operations to Make Network Connected using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Operations to Make Network Connected |
| LeetCode | #1319 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There are `n` computers numbered from `0` to `n - 1` connected by ethernet cables `connections` forming a network where `connections[i] = [a_i, b_i]` represents a connection between computers `a_i` and `b_i`. Any computer can reach any other computer directly or indirectly through the network.

You are given an initial computer network `connections`. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

Return *the minimum number of times you need to do this in order to make all the computers connected*. If it is not possible, return `-1`.

## Constraints
- `1 <= n <= 10^5`
- `1 <= connections.length <= min(n * (n - 1) / 2, 10^5)`
- `connections[i].length == 2`
- `0 <= a_i, b_i < n`
- `a_i != b_i`
- There are no repeated connections.
- No two computers are connected by more than one cable.

## Examples
### Example 1
- **Input:** `n = 4, connections = [[0,1],[0,2],[1,2]]`
- **Output:** `1`
- **Explanation:** Remove cable between computer 1 and 2 and place between computers 1 and 3.

### Example 2
- **Input:** `n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]`
- **Output:** `2`

### Example 3
- **Input:** `n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]`
- **Output:** `-1`
- **Explanation:** There are not enough cables.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Number of Operations to Make Network Connected**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 4, connections = [[0,1],[0,2],[1,2]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** Remove cable between computer 1 and 2 and place between computers 1 and 3.

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
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        parent = list(range(n))
        components = n

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: int, y: int):
            nonlocal components
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[rx] = ry
                components -= 1

        for u, v in connections:
            union(u, v)

        return components - 1
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
- [1830. Minimum Number of Operations to Make String Sorted](../../1501-2000/1830-minimum-number-of-operations-to-make-string-sorted/)
- [2009. Minimum Number of Operations to Make Array Continuous](../../2001-2500/2009-minimum-number-of-operations-to-make-array-continuous/)
- [2654. Minimum Number of Operations to Make All Array Elements Equal to 1](../../2501-3000/2654-minimum-number-of-operations-to-make-all-array-elements-equal-to-1/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-operations-to-make-network-connected/)
