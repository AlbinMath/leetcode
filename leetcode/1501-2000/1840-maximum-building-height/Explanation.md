# LeetCode 1840: Maximum Building Height

**LeetCode Problem #1840 — Maximum Building Height**
Solve LeetCode Maximum Building Height using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Building Height |
| LeetCode | #1840 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You want to build `n` new buildings in a city. The new buildings will be built in a line and are labeled from `1` to `n`.

However, there are city restrictions on the heights of the new buildings:

The height of each building must be a non-negative integer. 
 The height of the first building **must** be `0`. 
 The height difference between any two adjacent buildings **cannot exceed** `1`.

Additionally, there are city restrictions on the maximum height of specific buildings. These restrictions are given as a 2D integer array `restrictions` where `restrictions[i] = [id_i, maxHeight_i]` indicates that building `id_i` must have a height **less than or equal to** `maxHeight_i`.

It is guaranteed that each building will appear **at most once** in `restrictions`, and building `1` will **not** be in `restrictions`.

Return *the **maximum possible height** of the **tallest** building*.

## Constraints
- `2 <= n <= 10^9`
- `0 <= restrictions.length <= min(n - 1, 10^5)`
- `2 <= id_i <= n`
- `id_i` is **unique**.
- `0 <= maxHeight_i <= 10^9`

## Examples
### Example 1
- **Input:** `n = 5, restrictions = [[2,1],[4,1]]`
- **Output:** `2`
- **Explanation:** The green area in the image indicates the maximum allowed height for each building.
We can build the buildings with heights [0,1,2,1,2], and the tallest building has a height of 2.

### Example 2
- **Input:** `n = 6, restrictions = []`
- **Output:** `5`
- **Explanation:** The green area in the image indicates the maximum allowed height for each building.
We can build the buildings with heights [0,1,2,3,4,5], and the tallest building has a height of 5.

### Example 3
- **Input:** `n = 10, restrictions = [[5,3],[2,5],[7,4],[10,3]]`
- **Output:** `5`
- **Explanation:** The green area in the image indicates the maximum allowed height for each building.
We can build the buildings with heights [0,1,2,3,3,4,4,5,4,3], and the tallest building has a height of 5.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses **two-pass constraint propagation**.

1. Add restriction `[1, 0]` (building 1 must be height 0) and sort by building ID.
2. **Left-to-right pass:** Each restriction is tightened so it doesn't exceed the previous restriction's height + distance between them.
3. **Right-to-left pass:** Same tightening from the other direction.
4. **Calculate peaks:** Between each pair of consecutive restricted buildings, the maximum achievable peak is `(h1 + h2 + distance) / 2`.
5. Also check the height achievable after the last restriction (increases by 1 per building up to building `n`).

Time complexity is $O(M \log M)$ where $M$ is the number of restrictions, and space complexity is $O(M)$.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `n = 5, restrictions = [[2,1],[4,1]]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The green area in the image indicates the maximum allowed height for each building.
We can build the buildings with heights [0,1,2,1,2], and the tallest building has a height of 2.

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
class Solution(object):
    def maxBuilding(self, n, restrictions):
        """
        :type n: int
        :type restrictions: List[List[int]]
        :rtype: int
        """

        # Building 1 must have height 0
        restrictions.append([1, 0])

        # Sort restrictions by building ID
        restrictions.sort()

        m = len(restrictions)

        # Left to right:
        # A building cannot exceed the previous
        # restricted height + distance.
        for i in range(1, m):
            distance = restrictions[i][0] - restrictions[i - 1][0]

            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i - 1][1] + distance
            )

        # Right to left:
        # Apply restrictions from the right side.
        for i in range(m - 2, -1, -1):
            distance = restrictions[i + 1][0] - restrictions[i][0]

            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i + 1][1] + distance
            )

        answer = 0

        # Calculate maximum possible height between
        # consecutive restricted buildings.
        for i in range(1, m):
            x1, h1 = restrictions[i - 1]
            x2, h2 = restrictions[i]

            distance = x2 - x1

            # Highest possible peak between x1 and x2
            peak = (h1 + h2 + distance) // 2

            answer = max(answer, peak)

        # After the last restricted building,
        # heights can increase by 1 each step.
        last_id, last_height = restrictions[-1]

        answer = max(
            answer,
            last_height + (n - last_id)
        )

        return answer
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
- [3200. Maximum Height of a Triangle](../../3001-3500/3200-maximum-height-of-a-triangle/)
- [1117. Building H2O](../../1001-1500/1117-building-h2o/)
- [1739. Building Boxes](../../1501-2000/1739-building-boxes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-building-height/)
