# LeetCode 167: Two Sum II - Input Array Is Sorted

**LeetCode Problem #167 — Two Sum II - Input Array Is Sorted**
Solve LeetCode Two Sum II - Input Array Is Sorted using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Two Sum II - Input Array Is Sorted |
| LeetCode | #167 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **1-indexed** array of integers `numbers` that is already **sorted in non-decreasing order**.

Find **two** numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index_1]` and `numbers[index_2]` where `1 <= index_1 < index_2 <= numbers.length`.

Return the indices of the two numbers `index_1` and `index_2` as an integer array `[index_1, index_2]` of length 2.

The tests are generated such that there is **exactly one solution**. You **may not** use the same element twice.

Your solution must use only constant extra space.

## Constraints
- `2 <= numbers.length <= 3 * 10^4`
- `-1000 <= numbers[i] <= 1000`
- `numbers` is sorted in **non-decreasing order**.
- `-1000 <= target <= 1000`
- The tests are generated such that there is **exactly one solution**.

## Examples
### Example 1
- **Input:** `numbers = [ 2 , 7 ,11,15], target = 9`
- **Output:** `[1,2]`
- **Explanation:** The sum of 2 and 7 is 9. Therefore, index_1 = 1, index_2 = 2. We return [1, 2].

### Example 2
- **Input:** `numbers = [ 2 ,3, 4 ], target = 6`
- **Output:** `[1,3]`
- **Explanation:** The sum of 2 and 4 is 6. Therefore index_1 = 1, index_2 = 3. We return [1, 3].

### Example 3
- **Input:** `numbers = [ -1 , 0 ], target = -1`
- **Output:** `[1,2]`
- **Explanation:** The sum of -1 and 0 is -1. Therefore index_1 = 1, index_2 = 2. We return [1, 2].

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Two Sum II - Input Array Is Sorted**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `numbers = [ 2 , 7 ,11,15], target = 9`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,2]`.
4. **Verification:** The sum of 2 and 7 is 9. Therefore, index_1 = 1, index_2 = 2. We return [1, 2].

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
var twoSum = function(numbers, target) {
    let left = 0;
    let right = numbers.length - 1;

    while (left < right) {
        const sum = numbers[left] + numbers[right];

        if (sum === target) {
            return [left + 1, right + 1];
        } else if (sum < target) {
            left++;
        } else {
            right--;
        }
    }

    return [];
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
- [653. Two Sum IV - Input is a BST](../../0501-1000/0653-two-sum-iv---input-is-a-bst/)
- [2035. Partition Array Into Two Arrays to Minimize Sum Difference](../../2001-2500/2162-partition-array-into-two-arrays-to-minimize-sum-difference/)
- [4. Median of Two Sorted Arrays](../../0001-0500/0004-median-of-two-sorted-arrays/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
