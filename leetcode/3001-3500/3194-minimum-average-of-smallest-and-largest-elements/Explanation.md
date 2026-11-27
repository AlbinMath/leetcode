# LeetCode 3194: Minimum Average of Smallest and Largest Elements

**LeetCode Problem #3194 — Minimum Average of Smallest and Largest Elements**
Solve LeetCode Minimum Average of Smallest and Largest Elements using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Average of Smallest and Largest Elements |
| LeetCode | #3194 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
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
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Average of Smallest and Largest Elements**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [7,8,3,4,15,13,4,1]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
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
**Array / General**

## Topics
- Array

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
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1509. Minimum Difference Between Largest and Smallest Value in Three Moves](../../1501-2000/1509-minimum-difference-between-largest-and-smallest-value-in-three-moves/)
- [1491. Average Salary Excluding the Minimum and Maximum Salary](../../1001-1500/1491-average-salary-excluding-the-minimum-and-maximum-salary/)
- [1968. Array With Elements Not Equal to Average of Neighbors](../../1501-2000/1968-array-with-elements-not-equal-to-average-of-neighbors/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/)
