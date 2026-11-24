# LeetCode 75: Sort Colors

**LeetCode Problem #75 — Sort Colors**
Solve LeetCode Sort Colors using JavaScript, PHP and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sort Colors |
| LeetCode | #75 |
| Difficulty | Medium |
| Language | JavaScript, PHP |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array `nums` with `n` objects colored red, white, or blue, sort them ** in-place **so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

## Constraints
- `n == nums.length`
- `1 <= n <= 300`
- `nums[i]` is either 0, 1, or 2.

## Examples
### Example 1
- **Input:** `nums = [2,0,2,1,1,0]`
- **Output:** `[0,0,1,1,2,2]`
- **Explanation:** The array has two 0s, two 1s, and two 2s. Sorting them in-place places all 0s first, then all 1s, then all 2s.

### Example 2
- **Input:** `nums = [2,0,1]`
- **Output:** `[0,1,2]`
- **Explanation:** The array has one each of 0, 1, and 2, arranged in-place in the order 0, 1, 2.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Sort Colors**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,0,2,1,1,0]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[0,0,1,1,2,2]`.
4. **Verification:** The array has two 0s, two 1s, and two 2s. Sorting them in-place places all 0s first, then all 1s, then all 2s.

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
JavaScript, PHP

## Source Code
- [solution.js](./solution.js)
- [solution.php](./solution.php)


### JavaScript
```javascript
var sortColors = function(nums) {
    let low = 0;
    let mid = 0;
    let high = nums.length - 1;

    while (mid <= high) {
        if (nums[mid] === 0) {
            [nums[low], nums[mid]] = [nums[mid], nums[low]];
            low++;
            mid++;
        } else if (nums[mid] === 1) {
            mid++;
        } else {
            [nums[mid], nums[high]] = [nums[high], nums[mid]];
            high--;
        }
    }
};
```

### PHP
```php
class Solution {
    function sortColors(&$nums) {
        $low = 0;
        $mid = 0;
        $high = count($nums) - 1;

        while ($mid <= $high) {

            if ($nums[$mid] == 0) {
                // Swap 0 to the beginning
                $temp = $nums[$low];
                $nums[$low] = $nums[$mid];
                $nums[$mid] = $temp;

                $low++;
                $mid++;

            } elseif ($nums[$mid] == 1) {
                // 1 is already in the correct middle region
                $mid++;

            } else {
                // Swap 2 to the end
                $temp = $nums[$mid];
                $nums[$mid] = $nums[$high];
                $nums[$high] = $temp;

                $high--;
            }
        }
    }
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
- [1129. Shortest Path with Alternating Colors](../../1001-1500/1229-shortest-path-with-alternating-colors/)
- [3160. Find the Number of Distinct Colors Among the Balls](../../3001-3500/3434-find-the-number-of-distinct-colors-among-the-balls/)
- [147. Insertion Sort List](../../0001-0500/0147-insertion-sort-list/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sort-colors/)
