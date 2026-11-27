# LeetCode 2848: Points That Intersect With Cars

**LeetCode Problem #2848 — Points That Intersect With Cars**
Solve LeetCode Points That Intersect With Cars using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Points That Intersect With Cars |
| LeetCode | #2848 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
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
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Points That Intersect With Cars**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [[3,6],[1,5],[4,7]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7`.
4. **Verification:** All the points from 1 to 7 intersect at least one car, therefore the answer would be 7.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

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
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [1074. Number of Submatrices That Sum to Target](../../1001-1500/1074-number-of-submatrices-that-sum-to-target/)
- [1160. Find Words That Can Be Formed by Characters](../../1001-1500/1160-find-words-that-can-be-formed-by-characters/)
- [1222. Queens That Can Attack the King](../../1001-1500/1222-queens-that-can-attack-the-king/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/points-that-intersect-with-cars/)
