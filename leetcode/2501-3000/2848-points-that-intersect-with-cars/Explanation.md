# LeetCode 2848: Points That Intersect With Cars

**LeetCode Problem #2848 — Points That Intersect With Cars**
Solve LeetCode Points That Intersect With Cars using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Points That Intersect With Cars |
| LeetCode | #2848 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** 2D integer array `nums` representing the coordinates of the cars parking on a number line. For any index `i`, `nums[i] = [start_i, end_i]` where `start_i` is the starting point of the `i^th` car and `end_i` is the ending point of the `i^th` car.

Return *the number of integer points on the line that are covered with **any part** of a car.*

## Constraints
- `1 <= nums.length <= 100`
- `nums[i].length == 2`
- ` 1 <= start_i <= end_i <= 100 `

## Examples
### Example 1
- **Input:** `nums = [[3,6],[1,5],[4,7]]`
- **Output:** `7`
- **Explanation:** All the points from 1 to 7 intersect at least one car, therefore the answer would be 7.

### Example 2
- **Input:** `nums = [[1,3],[5,8]]`
- **Output:** `7`
- **Explanation:** Points intersecting at least one car are 1, 2, 3, 5, 6, 7, 8. There are a total of 7 points, therefore the answer would be 7.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Points That Intersect With Cars**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [[3,6],[1,5],[4,7]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7`.
4. **Verification:** All the points from 1 to 7 intersect at least one car, therefore the answer would be 7.

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
var numberOfPoints = function(nums) {
    const covered = new Array(101).fill(false);
    for (let [start, end] of nums) {
        for (let i = start; i <= end; i++) {
            covered[i] = true;
        }
    }
    let ans = 0;

    for (let i = 1; i <= 100; i++) {
        if (covered[i]) {
            ans++;
        }
    }

    return ans;
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
- [149. Max Points on a Line](../../0001-0500/0149-max-points-on-a-line/)
- [780. Reaching Points](../../0501-1000/0780-reaching-points/)
- [973. K Closest Points to Origin](../../0501-1000/0973-k-closest-points-to-origin/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/points-that-intersect-with-cars/)
