# LeetCode 3080: Mark Elements on Array by Performing Queries

**LeetCode Problem #3080 — Mark Elements on Array by Performing Queries**
Solve LeetCode Mark Elements on Array by Performing Queries using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Mark Elements on Array by Performing Queries |
| LeetCode | #3080 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** array `nums` of size `n` consisting of positive integers.

You are also given a 2D array `queries` of size `m` where `queries[i] = [index_i, k_i]`.

Initially all elements of the array are **unmarked**.

You need to apply `m` queries on the array in order, where on the `i^th` query you do the following:

Mark the element at index `index_i` if it is not already marked. 
 Then mark `k_i` unmarked elements in the array with the **smallest** values. If multiple such elements exist, mark the ones with the smallest indices. And if less than `k_i` unmarked elements exist, then mark all of them.

Return *an array answer of size *`m`* where *`answer[i]`* is the **sum** of unmarked elements in the array after the *`i^th`* query*.

## Constraints
- `n == nums.length`
- `m == queries.length`
- `1 <= m <= n <= 10^5`
- `1 <= nums[i] <= 10^5`
- `queries[i].length == 2`
- `0 <= index_i, k_i <= n - 1`

## Examples
### Example 1
- **Input:** `nums = [1,2,2,1,2,3,1], queries = [[1,2],[3,3],[4,2]]`
- **Output:** `[8,3,0]`
- **Explanation:** We do the following queries on the array: 

 
 Mark the element at index `1`, and `2` of the smallest unmarked elements with the smallest indices if they exist, the marked elements now are nums = [

### Example 2
- **Input:** `nums = [1,4,2,3], queries = [[0,1]]`
- **Output:** `[7]`
- **Explanation:** We do one query which is mark the element at index `0` and mark the smallest element among unmarked elements. The marked elements will be nums = [

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Mark Elements on Array by Performing Queries**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,2,1,2,3,1], queries = [[1,2],[3,3],[4,2]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[8,3,0]`.
4. **Verification:** We do the following queries on the array: 

 
 Mark the element at index `1`, and `2` of the smallest unmarked elements with the smallest indices if they exist, the marked elements now are nums = [

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
var unmarkedSumArray = function(nums, queries) {
    const n = nums.length;
    let totalSum = 0;
    for (const num of nums) totalSum += num;

    const marked = new Uint8Array(n);
    const sortedIndices = Array.from({ length: n }, (_, i) => i);
    sortedIndices.sort((a, b) => (nums[a] !== nums[b] ? nums[a] - nums[b] : a - b));

    let ptr = 0;
    const answer = new Array(queries.length);

    for (let q = 0; q < queries.length; q++) {
        let [idx, k] = queries[q];

        if (!marked[idx]) {
            marked[idx] = 1;
            totalSum -= nums[idx];
        }

        while (k > 0 && ptr < n) {
            const cand = sortedIndices[ptr++];
            if (!marked[cand]) {
                marked[cand] = 1;
                totalSum -= nums[cand];
                k--;
            }
        }

        answer[q] = totalSum;
    }

    return answer;
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
- [453. Minimum Moves to Equal Array Elements](../../0001-0500/0453-minimum-moves-to-equal-array-elements/)
- [462. Minimum Moves to Equal Array Elements II](../../0001-0500/0462-minimum-moves-to-equal-array-elements-ii/)
- [1464. Maximum Product of Two Elements in an Array](../../1001-1500/1464-maximum-product-of-two-elements-in-an-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/mark-elements-on-array-by-performing-queries/)
