# LeetCode 1184: Distance Between Bus Stops

**LeetCode Problem #1184 — Distance Between Bus Stops**
Solve LeetCode Distance Between Bus Stops using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Distance Between Bus Stops |
| LeetCode | #1184 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
A bus has `n` stops numbered from `0` to `n - 1` that form a circle. We know the distance between all pairs of neighboring stops where `distance[i]` is the distance between the stops number `i` and `(i + 1) % n`.

The bus goes along both directions i.e. clockwise and counterclockwise.

Return the shortest distance between the given `start` and `destination` stops.

## Constraints
- `1 <= n <= 10^4`
- `distance.length == n`
- `0 <= start, destination < n`
- `0 <= distance[i] <= 10^4`

## Examples
### Example 1
- **Input:** `distance = [1,2,3,4], start = 0, destination = 1`
- **Output:** `1`
- **Explanation:** Distance between 0 and 1 is 1 or 9, minimum is 1.

### Example 2
- **Input:** `distance = [1,2,3,4], start = 0, destination = 2`
- **Output:** `3`
- **Explanation:** Distance between 0 and 2 is 3 or 7, minimum is 3.

### Example 3
- **Input:** `distance = [1,2,3,4], start = 0, destination = 3`
- **Output:** `4`
- **Explanation:** Distance between 0 and 3 is 6 or 4, minimum is 4.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Distance Between Bus Stops**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `distance = [1,2,3,4], start = 0, destination = 1`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** Distance between 0 and 1 is 1 or 9, minimum is 1.

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
    def distanceBetweenBusStops(self, distance: list[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start
            
        clockwise_dist = sum(distance[start:destination])
        total_dist = sum(distance)
        
        return min(clockwise_dist, total_dist - clockwise_dist)
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
- [783. Minimum Distance Between BST Nodes](../../0501-1000/0783-minimum-distance-between-bst-nodes/)
- [1385. Find the Distance Value Between Two Arrays](../../1001-1500/1385-find-the-distance-value-between-two-arrays/)
- [1617. Count Subtrees With Max Distance Between Cities](../../1501-2000/1617-count-subtrees-with-max-distance-between-cities/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/distance-between-bus-stops/)
