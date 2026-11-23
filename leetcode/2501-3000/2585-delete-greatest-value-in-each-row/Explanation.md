# LeetCode 2500: Delete Greatest Value in Each Row

**LeetCode Problem #2500 — Delete Greatest Value in Each Row**
Solve LeetCode Delete Greatest Value in Each Row using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Delete Greatest Value in Each Row |
| LeetCode | #2500 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an `m x n` matrix `grid` consisting of positive integers.

Perform the following operation until `grid` becomes empty:

Delete the element with the greatest value from each row. If multiple such elements exist, delete any of them. 
 Add the maximum of deleted elements to the answer.

**Note** that the number of columns decreases by one after each operation.

Return *the answer after performing the operations described above*.

## Constraints
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 50`
- `1 <= grid[i][j] <= 100`

## Examples
### Example 1
- **Input:** `grid = [[1,2,4],[3,3,1]]`
- **Output:** `8`
- **Explanation:** The diagram above shows the removed values in each step.
- In the first operation, we remove 4 from the first row and 3 from the second row (notice that, there are two cells with value 3 and we can remove any of them). We add 4 to the answer.
- In the second operation, we remove 2 from the first row and 3 from the second row. We add 3 to the answer.
- In the third operation, we remove 1 from the first row and 1 from the second row. We add 1 to the answer.
The final answer = 4 + 3 + 1 = 8.

### Example 2
- **Input:** `grid = [[10]]`
- **Output:** `10`
- **Explanation:** The diagram above shows the removed values in each step.
- In the first operation, we remove 10 from the first row. We add 10 to the answer.
The final answer = 10.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Delete Greatest Value in Each Row**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[1,2,4],[3,3,1]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `8`.
4. **Verification:** The diagram above shows the removed values in each step.
- In the first operation, we remove 4 from the first row and 3 from the second row (notice that, there are two cells with value 3 and we can remove any of them). We add 4 to the answer.
- In the second operation, we remove 2 from the first row and 3 from the second row. We add 3 to the answer.
- In the third operation, we remove 1 from the first row and 1 from the second row. We add 1 to the answer.
The final answer = 4 + 3 + 1 = 8.

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
var deleteGreatestValue = function(grid) {
    const m = grid.length;
    const n = grid[0].length;

    // Sort each row in ascending order
    for (const row of grid) {
        row.sort((a, b) => a - b);
    }

    let answer = 0;
    // Sum the maximum value across all rows for each column
    for (let j = 0; j < n; j++) {
        let colMax = 0;
        for (let i = 0; i < m; i++) {
            colMax = Math.max(colMax, grid[i][j]);
        }
        answer += colMax;
    }

    return answer;
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
- [515. Find Largest Value in Each Tree Row](../../0501-1000/0515-find-largest-value-in-each-tree-row/)
- [1325. Delete Leaves With a Given Value](../../1001-1500/1450-delete-leaves-with-a-given-value/)
- [2003. Smallest Missing Genetic Value in Each Subtree](../../2001-2500/2131-smallest-missing-genetic-value-in-each-subtree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/delete-greatest-value-in-each-row/)
