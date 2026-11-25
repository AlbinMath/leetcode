# LeetCode 3362: Zero Array Transformation III

**LeetCode Problem #3362 — Zero Array Transformation III**
Solve LeetCode Zero Array Transformation III using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Zero Array Transformation III |
| LeetCode | #3362 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` of length `n` and a 2D array `queries` where `queries[i] = [l_i, r_i]`.

Each `queries[i]` represents the following action on `nums`:

Decrement the value at each index in the range `[l_i, r_i]` in `nums` by **at most**** **1. 
 The amount by which the value is decremented can be chosen **independently** for each index.

A **Zero Array** is an array with all its elements equal to 0.

Return the **maximum **number of elements that can be removed from `queries`, such that `nums` can still be converted to a **zero array** using the *remaining* queries. If it is not possible to convert `nums` to a **zero array**, return -1.

## Constraints
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^5`
- `1 <= queries.length <= 10^5`
- `queries[i].length == 2`
- `0 <= l_i <= r_i < nums.length`

## Examples
### Example 1
- **Input:** `nums = [2,0,2], queries = [[0,2],[0,2],[1,1]]`
- **Output:** `1`
- **Explanation:** After removing `queries[2]`, `nums` can still be converted to a zero array. 

 
 Using `queries[0]`, decrement `nums[0]` and `nums[2]` by 1 and `nums[1]` by 0. 
 Using `queries[1]`, decrement `nums[0]` and `nums[2]` by 1 and `nums[1]` by 0.

### Example 2
- **Input:** `nums = [1,1,1,1], queries = [[1,3],[0,2],[1,3],[1,2]]`
- **Output:** `2`
- **Explanation:** We can remove `queries[2]` and `queries[3]`.

### Example 3
- **Input:** `nums = [1,2,3,4], queries = [[0,3]]`
- **Output:** `-1`
- **Explanation:** `nums` cannot be converted to a zero array even after using all the queries.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Zero Array Transformation III**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,0,2], queries = [[0,2],[0,2],[1,1]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** After removing `queries[2]`, `nums` can still be converted to a zero array. 

 
 Using `queries[0]`, decrement `nums[0]` and `nums[2]` by 1 and `nums[1]` by 0. 
 Using `queries[1]`, decrement `nums[0]` and `nums[2]` by 1 and `nums[1]` by 0.

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
var maxRemoval = function(nums, queries) {
    const n = nums.length;
    const q = queries.length;
    queries.sort((a, b) => a[0] - b[0]);
    const heap = [];
    function push(val) {
        heap.push(val);
        let i = heap.length - 1;
        while (i > 0) {
            const parent = Math.floor((i - 1) / 2);
            if (heap[parent] >= heap[i]) break;
            [heap[parent], heap[i]] = [heap[i], heap[parent]];
            i = parent;
        }
    }
    function pop() {
        const result = heap[0];
        const last = heap.pop();
        if (heap.length > 0) {
            heap[0] = last;
            let i = 0;
            while (true) {
                let largest = i;
                const left = 2 * i + 1;
                const right = 2 * i + 2;

                if (left < heap.length && heap[left] > heap[largest]) {
                    largest = left;
                }
                if (right < heap.length && heap[right] > heap[largest]) {
                    largest = right;
                }
                if (largest === i) break;
                [heap[i], heap[largest]] = [heap[largest], heap[i]];
                i = largest;
            }
        }
        return result;
    }
    const diff = new Array(n + 1).fill(0);
    let active = 0;
    let j = 0;
    let selected = 0;
    for (let i = 0; i < n; i++) {
        active += diff[i];
        while (j < q && queries[j][0] <= i) {
            push(queries[j][1]);
            j++;
        }
        while (active < nums[i]) {
            while (heap.length > 0 && heap[0] < i) {
                pop();
            }
            if (heap.length === 0) {
                return -1;
            }
            const r = pop();
            active++;
            selected++;
            diff[r + 1]--;
        }
    }
    return q - selected;
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
- [3355. Zero Array Transformation I](../../3001-3500/3355-zero-array-transformation-i/)
- [3356. Zero Array Transformation II](../../3001-3500/3356-zero-array-transformation-ii/)
- [1969. Minimum Non-Zero Product of the Array Elements](../../1501-2000/1969-minimum-non-zero-product-of-the-array-elements/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/zero-array-transformation-iii/)
