# LeetCode 1691: Maximum Height by Stacking Cuboids 

**LeetCode Problem #1691 — Maximum Height by Stacking Cuboids **
Solve LeetCode Maximum Height by Stacking Cuboids  using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Height by Stacking Cuboids  |
| LeetCode | #1691 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given `n` `cuboids` where the dimensions of the `i^th` cuboid is `cuboids[i] = [width_i, length_i, height_i]` (**0-indexed**). Choose a **subset** of `cuboids` and place them on each other.

You can place cuboid `i` on cuboid `j` if `width_i <= width_j` and `length_i <= length_j` and `height_i <= height_j`. You can rearrange any cuboid's dimensions by rotating it to put it on another cuboid.

Return *the **maximum height** of the stacked* `cuboids`.

## Constraints
- `n == cuboids.length`
- `1 <= n <= 100`
- `1 <= width_i, length_i, height_i <= 100`

## Examples
### Example 1
- **Input:** `cuboids = [[50,45,20],[95,37,53],[45,23,12]]`
- **Output:** `190`
- **Explanation:** Cuboid 1 is placed on the bottom with the 53x37 side facing down with height 95.
Cuboid 0 is placed next with the 45x20 side facing down with height 50.
Cuboid 2 is placed next with the 23x12 side facing down with height 45.
The total height is 95 + 50 + 45 = 190.

### Example 2
- **Input:** `cuboids = [[38,25,45],[76,35,3]]`
- **Output:** `76`
- **Explanation:** You can't place any of the cuboids on the other.
We choose cuboid 1 and rotate it so that the 35x3 side is facing down and its height is 76.

### Example 3
- **Input:** `cuboids = [[7,11,17],[7,17,11],[11,7,17],[11,17,7],[17,7,11],[17,11,7]]`
- **Output:** `102`
- **Explanation:** After rearranging the cuboids, you can see that all cuboids have the same dimension.
You can place the 11x7 side down on all cuboids so their heights are 17.
The maximum height of stacked cuboids is 6 * 17 = 102.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Height by Stacking Cuboids **, we observe the problem requirements and utilize the **Stack & Queue** technique. We decompose the problem into overlapping subproblems using a **Stack**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `cuboids = [[50,45,20],[95,37,53],[45,23,12]]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `190`.
4. **Verification:** Cuboid 1 is placed on the bottom with the 53x37 side facing down with height 95.
Cuboid 0 is placed next with the 45x20 side facing down with height 50.
Cuboid 2 is placed next with the 23x12 side facing down with height 45.
The total height is 95 + 50 + 45 = 190.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var maxHeight = function(cuboids) {
    const n = cuboids.length;
    for (const cuboid of cuboids) {
        cuboid.sort((a, b) => a - b);
    }
    cuboids.sort((a, b) => {
        if (a[0] !== b[0]) return a[0] - b[0];
        if (a[1] !== b[1]) return a[1] - b[1];
        return a[2] - b[2];
    });
    const dp = new Array(n);
    let result = 0;
    for (let i = 0; i < n; i++) {
        dp[i] = cuboids[i][2];
        for (let j = 0; j < i; j++) {
            if (
                cuboids[j][0] <= cuboids[i][0] &&
                cuboids[j][1] <= cuboids[i][1] &&
                cuboids[j][2] <= cuboids[i][2]
            ) {
                dp[i] = Math.max(
                    dp[i],
                    dp[j] + cuboids[i][2]
                );
            }
        }
        result = Math.max(result, dp[i]);
    }
    return result;
};
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
- [1840. Maximum Building Height](../../1501-2000/1840-maximum-building-height/)
- [3200. Maximum Height of a Triangle](../../3001-3500/3200-maximum-height-of-a-triangle/)
- [310. Minimum Height Trees](../../0001-0500/0310-minimum-height-trees/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-height-by-stacking-cuboids/)
