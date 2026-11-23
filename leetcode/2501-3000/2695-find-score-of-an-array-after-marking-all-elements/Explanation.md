# LeetCode 2593: Find Score of an Array After Marking All Elements

**LeetCode Problem #2593 — Find Score of an Array After Marking All Elements**
Solve LeetCode Find Score of an Array After Marking All Elements using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Score of an Array After Marking All Elements |
| LeetCode | #2593 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array `nums` consisting of positive integers.

Starting with `score = 0`, apply the following algorithm:

Choose the smallest integer of the array that is not marked. If there is a tie, choose the one with the smallest index. 
 Add the value of the chosen integer to `score`. 
 Mark **the chosen element and its two adjacent elements if they exist**. 
 Repeat until all the array elements are marked.

Return *the score you get after applying the above algorithm*.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^6`

## Examples
### Example 1
- **Input:** `nums = [2,1,3,4,5,2]`
- **Output:** `7`
- **Explanation:** We mark the elements as follows:
- 1 is the smallest unmarked element, so we mark it and its two adjacent elements: [ 2 , 1 , 3 ,4,5,2].
- 2 is the smallest unmarked element, so we mark it and its left adjacent element: [ 2 , 1 , 3 ,4, 5 , 2 ].
- 4 is the only remaining unmarked element, so we mark it: [ 2 , 1 , 3 , 4 , 5 , 2 ].
Our score is 1 + 2 + 4 = 7.

### Example 2
- **Input:** `nums = [2,3,5,1,3,2]`
- **Output:** `5`
- **Explanation:** We mark the elements as follows:
- 1 is the smallest unmarked element, so we mark it and its two adjacent elements: [2,3, 5 , 1 , 3 ,2].
- 2 is the smallest unmarked element, since there are two of them, we choose the left-most one, so we mark the one at index 0 and its right adjacent element: [ 2 , 3 , 5 , 1 , 3 ,2].
- 2 is the only remaining unmarked element, so we mark it: [ 2 , 3 , 5 , 1 , 3 , 2 ].
Our score is 1 + 2 + 2 = 5.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Find Score of an Array After Marking All Elements**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,1,3,4,5,2]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7`.
4. **Verification:** We mark the elements as follows:
- 1 is the smallest unmarked element, so we mark it and its two adjacent elements: [ 2 , 1 , 3 ,4,5,2].
- 2 is the smallest unmarked element, so we mark it and its left adjacent element: [ 2 , 1 , 3 ,4, 5 , 2 ].
- 4 is the only remaining unmarked element, so we mark it: [ 2 , 1 , 3 , 4 , 5 , 2 ].
Our score is 1 + 2 + 4 = 7.

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
var findScore = function(nums) {
    const n = nums.length;
    const indices = Array.from({ length: n }, (_, i) => i);

    // Sort indices by value ascending, breaking ties by smaller index
    indices.sort((a, b) => (nums[a] !== nums[b] ? nums[a] - nums[b] : a - b));

    const marked = new Uint8Array(n);
    let score = 0;

    for (const idx of indices) {
        if (!marked[idx]) {
            score += nums[idx];
            marked[idx] = 1;
            if (idx > 0) marked[idx - 1] = 1;
            if (idx + 1 < n) marked[idx + 1] = 1;
        }
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
- [448. Find All Numbers Disappeared in an Array](../../0001-0500/0448-find-all-numbers-disappeared-in-an-array/)
- [2089. Find Target Indices After Sorting Array](../../2001-2500/2210-find-target-indices-after-sorting-array/)
- [3145. Find Products of Elements of Big Array](../../3001-3500/3411-find-products-of-elements-of-big-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/)
