# LeetCode 2736: Maximum Sum Queries

**LeetCode Problem #2736 — Maximum Sum Queries**
Solve LeetCode Maximum Sum Queries using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Sum Queries |
| LeetCode | #2736 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two **0-indexed** integer arrays `nums1` and `nums2`, each of length `n`, and a **1-indexed 2D array** `queries` where `queries[i] = [x_i, y_i]`.

For the `i^th` query, find the **maximum value** of `nums1[j] + nums2[j]` among all indices `j` `(0 <= j < n)`, where `nums1[j] >= x_i` and `nums2[j] >= y_i`, or **-1** if there is no `j` satisfying the constraints.

Return *an array *`answer`* where *`answer[i]`* is the answer to the *`i^th`* query.*

## Constraints
- `nums1.length == nums2.length`
- `n == nums1.length `
- `1 <= n <= 10^5`
- `1 <= nums1[i], nums2[i] <= 10^9 `
- `1 <= queries.length <= 10^5`
- `queries[i].length == 2`
- `x_i == queries[i][1]`
- `y_i == queries[i][2]`
- `1 <= x_i, y_i <= 10^9`

## Examples
### Example 1
- **Input:** `nums1 = [4,3,1,2], nums2 = [2,4,9,5], queries = [[4,1],[1,3],[2,5]]`
- **Output:** `[6,10,7]`
- **Explanation:** For the 1st query x_i = 4 and y_i = 1 , we can select index j = 0 since nums1[j] >= 4 and nums2[j] >= 1 . The sum nums1[j] + nums2[j] is 6, and we can show that 6 is the maximum we can obtain.

For the 2nd query x_i = 1 and y_i = 3 , we can select index j = 2 since nums1[j] >= 1 and nums2[j] >= 3 . The sum nums1[j] + nums2[j] is 10, and we can show that 10 is the maximum we can obtain. 

For the 3rd query x_i = 2 and y_i = 5 , we can select index j = 3 since nums1[j] >= 2 and nums2[j] >= 5 . The sum nums1[j] + nums2[j] is 7, and we can show that 7 is the maximum we can obtain.

Therefore, we return [6,10,7] .

### Example 2
- **Input:** `nums1 = [3,2,5], nums2 = [2,3,4], queries = [[4,4],[3,2],[1,1]]`
- **Output:** `[9,9,9]`
- **Explanation:** For this example, we can use index j = 2 for all the queries since it satisfies the

### Example 3
- **Input:** `nums1 = [2,1], nums2 = [2,3], queries = [[3,3]]`
- **Output:** `[-1]`
- **Explanation:** There is one query in this example with x_i = 3 and y_i = 3. For every index, j, either nums1[j] < x_i or nums2[j] < y_i . Hence, there is no solution.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximum Sum Queries**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums1 = [4,3,1,2], nums2 = [2,4,9,5], queries = [[4,1],[1,3],[2,5]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[6,10,7]`.
4. **Verification:** For the 1st query x_i = 4 and y_i = 1 , we can select index j = 0 since nums1[j] >= 4 and nums2[j] >= 1 . The sum nums1[j] + nums2[j] is 6, and we can show that 6 is the maximum we can obtain.

For the 2nd query x_i = 1 and y_i = 3 , we can select index j = 2 since nums1[j] >= 1 and nums2[j] >= 3 . The sum nums1[j] + nums2[j] is 10, and we can show that 10 is the maximum we can obtain. 

For the 3rd query x_i = 2 and y_i = 5 , we can select index j = 3 since nums1[j] >= 2 and nums2[j] >= 5 . The sum nums1[j] + nums2[j] is 7, and we can show that 7 is the maximum we can obtain.

Therefore, we return [6,10,7] .

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
var maximumSumQueries = function(nums1, nums2, queries) {
    const n = nums1.length;

    // Store points as [x, y, sum]
    const points = [];
    const ys = [...nums2].sort((a, b) => a - b);

    for (let i = 0; i < n; i++) {
        points.push([nums1[i], nums2[i], nums1[i] + nums2[i]]);
    }

    // Sort points by x descending
    points.sort((a, b) => b[0] - a[0]);

    // Sort queries by x descending, retaining original indices
    const sortedQueries = queries
        .map(([x, y], i) => [x, y, i])
        .sort((a, b) => b[0] - a[0]);

    // Coordinate compression of nums2
    const uniqueY = [...new Set(ys)];
    const m = uniqueY.length;

    // Iterative segment tree storing maximum sums
    let size = 1;
    while (size < m) size *= 2;

    const tree = new Array(size * 2).fill(-1);

    function update(pos, value) {
        let i = pos + size;
        tree[i] = Math.max(tree[i], value);

        for (i >>= 1; i > 0; i >>= 1) {
            tree[i] = Math.max(tree[i * 2], tree[i * 2 + 1]);
        }
    }

    // Maximum sum over compressed indices [left, m - 1]
    function query(left) {
        let l = left + size;
        let r = m - 1 + size;
        let result = -1;

        while (l <= r) {
            if (l % 2 === 1) result = Math.max(result, tree[l++]);
            if (r % 2 === 0) result = Math.max(result, tree[r--]);

            l >>= 1;
            r >>= 1;
        }

        return result;
    }

    const answer = new Array(queries.length).fill(-1);
    let p = 0;

    for (const [x, y, index] of sortedQueries) {
        // Insert every point satisfying nums1 >= x
        while (p < n && points[p][0] >= x) {
            const [px, py, sum] = points[p++];

            const pos = lowerBound(uniqueY, py);
            update(pos, sum);
        }

        // Find the first compressed y >= the query's y
        const left = lowerBound(uniqueY, y);

        if (left < m) {
            answer[index] = query(left);
        }
    }

    return answer;
};

function lowerBound(arr, target) {
    let left = 0;
    let right = arr.length;

    while (left < right) {
        const mid = Math.floor((left + right) / 2);

        if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }

    return left;
}
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
- [124. Binary Tree Maximum Path Sum](../../0001-0500/0124-binary-tree-maximum-path-sum/)
- [689. Maximum Sum of 3 Non-Overlapping Subarrays](../../0501-1000/0689-maximum-sum-of-3-non-overlapping-subarrays/)
- [918. Maximum Sum Circular Subarray](../../0501-1000/0954-maximum-sum-circular-subarray/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-sum-queries/)
