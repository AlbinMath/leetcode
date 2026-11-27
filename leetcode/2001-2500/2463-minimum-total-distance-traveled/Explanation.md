# LeetCode 2463: Minimum Total Distance Traveled

**LeetCode Problem #2463 — Minimum Total Distance Traveled**
Solve LeetCode Minimum Total Distance Traveled using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Total Distance Traveled |
| LeetCode | #2463 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There are some robots and factories on the X-axis. You are given an integer array `robot` where `robot[i]` is the position of the `i^th` robot. You are also given a 2D integer array `factory` where `factory[j] = [position_j, limit_j]` indicates that `position_j` is the position of the `j^th` factory and that the `j^th` factory can repair at most `limit_j` robots.

The positions of each robot are **unique**. The positions of each factory are also **unique**. Note that a robot can be **in the same position** as a factory initially.

All the robots are initially broken; they keep moving in one direction. The direction could be the negative or the positive direction of the X-axis. When a robot reaches a factory that did not reach its limit, the factory repairs the robot, and it stops moving.

**At any moment**, you can set the initial direction of moving for **some** robot. Your target is to minimize the total distance traveled by all the robots.

Return *the minimum total distance traveled by all the robots*. The test cases are generated such that all the robots can be repaired.

**Note that**

All robots move at the same speed. 
 If two robots move in the same direction, they will never collide. 
 If two robots move in opposite directions and they meet at some point, they do not collide. They cross each other. 
 If a robot passes by a factory that reached its limits, it crosses it as if it does not exist. 
 If the robot moved from a position `x` to a position `y`, the distance it moved is `|y - x|`.

## Constraints
- `1 <= robot.length, factory.length <= 100`
- `factory[j].length == 2`
- `-10^9 <= robot[i], position_j <= 10^9`
- `0 <= limit_j <= robot.length`
- The input will be generated such that it is always possible to repair every robot.

## Examples
### Example 1
- **Input:** `robot = [0,4,6], factory = [[2,2],[6,2]]`
- **Output:** `4`
- **Explanation:** As shown in the figure:
- The first robot at position 0 moves in the positive direction. It will be repaired at the first factory.
- The second robot at position 4 moves in the negative direction. It will be repaired at the first factory.
- The third robot at position 6 will be repaired at the second factory. It does not need to move.
The limit of the first factory is 2, and it fixed 2 robots.
The limit of the second factory is 2, and it fixed 1 robot.
The total distance is |2 - 0| + |2 - 4| + |6 - 6| = 4. It can be shown that we cannot achieve a better total distance than 4.

### Example 2
- **Input:** `robot = [1,-1], factory = [[-2,1],[2,1]]`
- **Output:** `2`
- **Explanation:** As shown in the figure:
- The first robot at position 1 moves in the positive direction. It will be repaired at the second factory.
- The second robot at position -1 moves in the negative direction. It will be repaired at the first factory.
The limit of the first factory is 1, and it fixed 1 robot.
The limit of the second factory is 1, and it fixed 1 robot.
The total distance is |2 - 1| + |(-2) - (-1)| = 2. It can be shown that we cannot achieve a better total distance than 2.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Total Distance Traveled**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `robot = [0,4,6], factory = [[2,2],[6,2]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** As shown in the figure:
- The first robot at position 0 moves in the positive direction. It will be repaired at the first factory.
- The second robot at position 4 moves in the negative direction. It will be repaired at the first factory.
- The third robot at position 6 will be repaired at the second factory. It does not need to move.
The limit of the first factory is 2, and it fixed 2 robots.
The limit of the second factory is 2, and it fixed 1 robot.
The total distance is |2 - 0| + |2 - 4| + |6 - 6| = 4. It can be shown that we cannot achieve a better total distance than 4.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var minimumTotalDistance = function(robot, factory) {
    robot.sort((a, b) => a - b);
    factory.sort((a, b) => a[0] - b[0]);

    const n = robot.length;

    let dp = new Array(n + 1).fill(Infinity);
    dp[0] = 0;

    for (const [position, limit] of factory) {
        const newDp = new Array(n + 1).fill(Infinity);

        for (let i = 0; i <= n; i++) {
            let distance = 0;

            for (let count = 0; count <= Math.min(i, limit); count++) {
                if (count > 0) {
                    distance += Math.abs(
                        robot[i - count] - position
                    );
                }

                newDp[i] = Math.min(
                    newDp[i],
                    dp[i - count] + distance
                );
            }
        }

        dp = newDp;
    }

    return dp[n];
};
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
- [2739. Total Distance Traveled](../../2501-3000/2739-total-distance-traveled/)
- [477. Total Hamming Distance](../../0001-0500/0477-total-hamming-distance/)
- [1959. Minimum Total Space Wasted With K Resizing Operations](../../1501-2000/1959-minimum-total-space-wasted-with-k-resizing-operations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-total-distance-traveled/)
