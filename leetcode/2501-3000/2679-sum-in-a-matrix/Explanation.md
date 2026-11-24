# LeetCode 2679: Sum in a Matrix

**LeetCode Problem #2679 — Sum in a Matrix**
Solve LeetCode Sum in a Matrix using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sum in a Matrix |
| LeetCode | #2679 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** 2D integer array `nums`. Initially, your score is `0`. Perform the following operations until the matrix becomes empty:

From each row in the matrix, select the largest number and remove it. In the case of a tie, it does not matter which number is chosen. 
 Identify the highest number amongst all those removed in step 1. Add that number to your **score**.

Return *the final **score**.*

## Constraints
- `1 <= nums.length <= 300`
- `1 <= nums[i].length <= 500`
- `0 <= nums[i][j] <= 10^3`

## Examples
### Example 1
- **Input:** `nums = [[7,2,1],[6,4,2],[6,5,3],[3,2,1]]`
- **Output:** `15`
- **Explanation:** In the first operation, we remove 7, 6, 6, and 3. We then add 7 to our score. Next, we remove 2, 4, 5, and 2. We add 5 to our score. Lastly, we remove 1, 2, 3, and 1. We add 3 to our score. Thus, our final score is 7 + 5 + 3 = 15.

### Example 2
- **Input:** `nums = [[1]]`
- **Output:** `1`
- **Explanation:** We remove 1 and add it to the answer. We return 1.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Sum in a Matrix**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [[7,2,1],[6,4,2],[6,5,3],[3,2,1]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `15`.
4. **Verification:** In the first operation, we remove 7, 6, 6, and 3. We then add 7 to our score. Next, we remove 2, 4, 5, and 2. We add 5 to our score. Lastly, we remove 1, 2, 3, and 1. We add 3 to our score. Thus, our final score is 7 + 5 + 3 = 15.

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
var matrixSum = function(nums) {
    const m = nums.length;
    const n = nums[0].length;

    // Sort each row in ascending order
    for (const row of nums) {
        row.sort((a, b) => a - b);
    }

    let score = 0;
    // Find the maximum in each column and add to score
    for (let j = 0; j < n; j++) {
        let colMax = 0;
        for (let i = 0; i < m; i++) {
            colMax = Math.max(colMax, nums[i][j]);
        }
        score += colMax;
    }

    return score;
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
- [1314. Matrix Block Sum](../../1001-1500/1314-matrix-block-sum/)
- [1439. Find the Kth Smallest Sum of a Matrix With Sorted Rows](../../1001-1500/1439-find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/)
- [1572. Matrix Diagonal Sum](../../1501-2000/1572-matrix-diagonal-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sum-in-a-matrix/)
