# LeetCode 3194: Minimum Average of Smallest and Largest Elements

**LeetCode Problem #3194 — Minimum Average of Smallest and Largest Elements**
Solve LeetCode Minimum Average of Smallest and Largest Elements using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Average of Smallest and Largest Elements |
| LeetCode | #3194 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You have an array of floating point numbers `averages` which is initially empty. You are given an array `nums` of `n` integers where `n` is even.

You repeat the following procedure `n / 2` times:

Remove the **smallest** element, `minElement`, and the **largest** element `maxElement`, from `nums`. 
 Add `(minElement + maxElement) / 2` to `averages`.

Return the **minimum** element in `averages`.

## Constraints
- `2 <= n == nums.length <= 50`
- `n` is even.
- `1 <= nums[i] <= 50`

## Examples
### Example 1
- **Input:** `nums = [7,8,3,4,15,13,4,1]`
- **Output:** `5.5`
- **Explanation:** step 
 nums 
 averages 
 
 
 0 
 [7,8,3,4,15,13,4,1] 
 [] 
 
 
 1 
 [7,8,3,4,13,4] 
 [8] 
 
 
 2 
 [7,8,4,4] 
 [8,8] 
 
 
 3 
 [7,4] 
 [8,8,6] 
 
 
 4 
 [] 
 [8,8,6,5.5] 
 
 
 
The smallest element of averages, 5.5, is returned.

### Example 2
- **Input:** `nums = [1,9,8,3,10,5]`
- **Output:** `5.5`
- **Explanation:** step 
 nums 
 averages 
 
 
 0 
 [1,9,8,3,10,5] 
 [] 
 
 
 1 
 [9,8,3,5] 
 [5.5] 
 
 
 2 
 [8,5] 
 [5.5,6] 
 
 
 3 
 [] 
 [5.5,6,6.5]

### Example 3
- **Input:** `nums = [1,2,3,7,8,9]`
- **Output:** `5.0`
- **Explanation:** step 
 nums 
 averages 
 
 
 0 
 [1,2,3,7,8,9] 
 [] 
 
 
 1 
 [2,3,7,8] 
 [5] 
 
 
 2 
 [3,7] 
 [5,5] 
 
 
 3 
 [] 
 [5,5,5]

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimum Average of Smallest and Largest Elements**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [7,8,3,4,15,13,4,1]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5.5`.
4. **Verification:** step 
 nums 
 averages 
 
 
 0 
 [7,8,3,4,15,13,4,1] 
 [] 
 
 
 1 
 [7,8,3,4,13,4] 
 [8] 
 
 
 2 
 [7,8,4,4] 
 [8,8] 
 
 
 3 
 [7,4] 
 [8,8,6] 
 
 
 4 
 [] 
 [8,8,6,5.5] 
 
 
 
The smallest element of averages, 5.5, is returned.

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
var minimumAverage = function(nums) {
    nums.sort((a, b) => a - b);

    let left = 0;
    let right = nums.length - 1;

    let minAvg = Infinity;

    while (left < right) {
        const avg = (nums[left] + nums[right]) / 2;

        minAvg = Math.min(minAvg, avg);

        left++;
        right--;
    }

    return minAvg;
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
- [1509. Minimum Difference Between Largest and Smallest Value in Three Moves](../../1501-2000/1509-minimum-difference-between-largest-and-smallest-value-in-three-moves/)
- [632. Smallest Range Covering Elements from K Lists](../../0501-1000/0632-smallest-range-covering-elements-from-k-lists/)
- [1850. Minimum Adjacent Swaps to Reach the Kth Smallest Number](../../1501-2000/1850-minimum-adjacent-swaps-to-reach-the-kth-smallest-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/)
