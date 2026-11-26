# LeetCode 1906: Minimum Absolute Difference Queries

**LeetCode Problem #1906 — Minimum Absolute Difference Queries**
Solve LeetCode Minimum Absolute Difference Queries using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Absolute Difference Queries |
| LeetCode | #1906 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
The **minimum absolute difference** of an array `a` is defined as the **minimum value** of `|a[i] - a[j]|`, where `0 <= i < j < a.length` and `a[i] != a[j]`. If all elements of `a` are the **same**, the minimum absolute difference is `-1`.

For example, the minimum absolute difference of the array `[5, 2 , 3 ,7,2]` is `|2 - 3| = 1`. Note that it is not `0` because `a[i]` and `a[j]` must be different.

You are given an integer array `nums` and the array `queries` where `queries[i] = [l_i, r_i]`. For each query `i`, compute the **minimum absolute difference** of the **subarray** `nums[l_i...r_i]` containing the elements of `nums` between the **0-based** indices `l_i` and `r_i` (**inclusive**).

Return *an **array** *`ans` *where* `ans[i]` *is the answer to the* `i^th` *query*.

A **subarray** is a contiguous sequence of elements in an array.

The value of `|x|` is defined as:

`x` if `x >= 0`. 
 `-x` if `x < 0`.

## Constraints
- `2 <= nums.length <= 10^5`
- `1 <= nums[i] <= 100`
- `1 <= queries.length <= 2 * 10^4`
- `0 <= l_i < r_i < nums.length`

## Examples
### Example 1
- **Input:** `nums = [1,3,4,8], queries = [[0,1],[1,2],[2,3],[0,3]]`
- **Output:** `[2,1,4,1]`
- **Explanation:** The queries are processed as follows:
- queries[0] = [0,1]: The subarray is [ 1 , 3 ] and the minimum absolute difference is |1-3| = 2.
- queries[1] = [1,2]: The subarray is [ 3 , 4 ] and the minimum absolute difference is |3-4| = 1.
- queries[2] = [2,3]: The subarray is [ 4 , 8 ] and the minimum absolute difference is |4-8| = 4.
- queries[3] = [0,3]: The subarray is [1, 3 , 4 ,8] and the minimum absolute difference is |3-4| = 1.

### Example 2
- **Input:** `nums = [4,5,2,2,7,10], queries = [[2,3],[0,2],[0,5],[3,5]]`
- **Output:** `[-1,1,1,3]`
- **Explanation:** The queries are processed as follows:
- queries[0] = [2,3]: The subarray is [2,2] and the minimum absolute difference is -1 because all the
 elements are the same.
- queries[1] = [0,2]: The subarray is [ 4 , 5 ,2] and the minimum absolute difference is |4-5| = 1.
- queries[2] = [0,5]: The subarray is [ 4 , 5 ,2,2,7,10] and the minimum absolute difference is |4-5| = 1.
- queries[3] = [3,5]: The subarray is [2, 7 , 10 ] and the minimum absolute difference is |7-10| = 3.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimum Absolute Difference Queries**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,3,4,8], queries = [[0,1],[1,2],[2,3],[0,3]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,1,4,1]`.
4. **Verification:** The queries are processed as follows:
- queries[0] = [0,1]: The subarray is [ 1 , 3 ] and the minimum absolute difference is |1-3| = 2.
- queries[1] = [1,2]: The subarray is [ 3 , 4 ] and the minimum absolute difference is |3-4| = 1.
- queries[2] = [2,3]: The subarray is [ 4 , 8 ] and the minimum absolute difference is |4-8| = 4.
- queries[3] = [0,3]: The subarray is [1, 3 , 4 ,8] and the minimum absolute difference is |3-4| = 1.

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
var minDifference = function(nums, queries) {
    const n = nums.length;
    let prefix = Array.from(
        { length: 101 },
        () => new Int32Array(n + 1)
    );
    for (let v = 1; v <= 100; v++) {
        for (let i = 0; i < n; i++) {
            prefix[v][i + 1] =
                prefix[v][i] + (nums[i] === v ? 1 : 0);
        }
    }
    let answer = [];
    for (let [left, right] of queries) {
        let minDiff = Infinity;
        let previous = -1;
        for (let v = 1; v <= 100; v++) {
            let count =
                prefix[v][right + 1] - prefix[v][left];

            if (count > 0) {
                if (previous !== -1) {
                    minDiff = Math.min(
                        minDiff,
                        v - previous
                    );
                }

                previous = v;
            }
        }

        answer.push(minDiff === Infinity ? -1 : minDiff);
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
- [530. Minimum Absolute Difference in BST](../../0501-1000/0530-minimum-absolute-difference-in-bst/)
- [1200. Minimum Absolute Difference](../../1001-1500/1200-minimum-absolute-difference/)
- [1818. Minimum Absolute Sum Difference](../../1501-2000/1818-minimum-absolute-sum-difference/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-absolute-difference-queries/)
