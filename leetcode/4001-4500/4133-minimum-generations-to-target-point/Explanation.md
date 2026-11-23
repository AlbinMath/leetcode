# LeetCode 3923: Minimum Generations to Target Point

**LeetCode Problem #3923 — Minimum Generations to Target Point**
Solve LeetCode Minimum Generations to Target Point using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Generations to Target Point |
| LeetCode | #3923 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a 2D integer array `points` where `points[i] = [x_i, y_i, z_i]` represents a point in 3D space, and an integer array `target` representing a target point.

Define **generation** 0 as the initial list of points. For each integer `k >= 1`, form generation `k` as follows:

Consider every pair of two **distinct** points `a = [x_1, y_1, z_1]` and `b = [x_2, y_2, z_2]` taken from all points produced in generations 0 through `k - 1`. 
 For each such pair, compute `c = [floor((x_1 + x_2) / 2), floor((y_1 + y_2) / 2), floor((z_1 + z_2) / 2)]` and collect every such `c` into a generation `k`. 
 All points in the generation `k` are produced **simultaneously** from points in generations 0 through​​​​​​​ `k - 1`. 
 After generation `k` is formed, the points in the generation `k` are considered available for forming later generations.

Return the **smallest** integer `k` such that the `target` appears in one of the generations 0 through `k`. If the `target` is already in the initial points, return 0. If it is impossible to obtain the `target`, return -1.

Notes:

**floor** denotes rounding **down** to the nearest integer. 
 "Two **distinct** points" means the two chosen points must have **different** `(x, y, z)` coordinates. A point cannot be paired with itself, and pairing two points with **identical** coordinates is not possible.

## Constraints
- `1 <= points.length <= 20`
- `points[i] = [x_i, y_i, z_i​​​​​​​]`
- `0 <= x_i, y_i, z_i <= 6`
- `target.length == 3`
- `​​​​​​​0 <= target[i] <= 6`
- The initial set of points contains no duplicates.

## Examples
### Example 1
- **Input:** `points = [[0,0,0],[6,6,6]], target = [3,3,3]`
- **Output:** `1`

### Example 2
- **Input:** `points = [[0,0,0],[5,5,5]], target = [1,1,1]`
- **Output:** `2`

### Example 3
- **Input:** `points = [[0,0,0],[2,2,2],[3,3,3]], target = [2,2,2]`
- **Output:** `0`

### Example 4
- **Input:** `points = [[1,2,3]], target = [5,5,5]`
- **Output:** `-1`
- **Explanation:** Only one initial point is available, so no new points can be generated. 
 Therefore, the target cannot be obtained, and the answer is -1.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Generations to Target Point**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `points = [[0,0,0],[6,6,6]], target = [3,3,3]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.

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
    def minGenerations(self, points: list[list[int]], target: list[int]) -> int:
        t = tuple(target)
        have = set(map(tuple, points))
        if t in have:
            return 0

        k = 0
        while True:
            k += 1
            pts = list(have)
            new = set()
            for i in range(len(pts)):
                a = pts[i]
                for j in range(i + 1, len(pts)):
                    b = pts[j]
                    c = ((a[0] + b[0]) // 2,
                         (a[1] + b[1]) // 2,
                         (a[2] + b[2]) // 2)
                    if c not in have:
                        new.add(c)
            if not new:
                return -1
            if t in new:
                return k
            have |= new
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
- [1210. Minimum Moves to Reach Target with Rotations](../../1001-1500/1322-minimum-moves-to-reach-target-with-rotations/)
- [1263. Minimum Moves to Move a Box to Their Target Location](../../1001-1500/1389-minimum-moves-to-move-a-box-to-their-target-location/)
- [1526. Minimum Number of Increments on Subarrays to Form a Target Array](../../1501-2000/1633-minimum-number-of-increments-on-subarrays-to-form-a-target-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-generations-to-target-point/)
