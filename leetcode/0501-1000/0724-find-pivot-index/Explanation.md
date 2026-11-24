# LeetCode 724: Find Pivot Index

**LeetCode Problem #724 — Find Pivot Index**
Solve LeetCode Find Pivot Index using JavaScript, Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Pivot Index |
| LeetCode | #724 |
| Difficulty | Easy |
| Language | JavaScript, Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array of integers `nums`, calculate the **pivot index** of this array.

The **pivot index** is the index where the sum of all the numbers **strictly** to the left of the index is equal to the sum of all the numbers **strictly** to the index's right.

If the index is on the left edge of the array, then the left sum is `0` because there are no elements to the left. This also applies to the right edge of the array.

Return *the **leftmost pivot index***. If no such index exists, return `-1`.

## Constraints
- `1 <= nums.length <= 10^4`
- `-1000 <= nums[i] <= 1000`

## Examples
### Example 1
- **Input:** `nums = [1,7,3,6,5,6]`
- **Output:** `3`
- **Explanation:** The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11

### Example 2
- **Input:** `nums = [1,2,3]`
- **Output:** `-1`
- **Explanation:** There is no index that satisfies the conditions in the problem statement.

### Example 3
- **Input:** `nums = [2,1,-1]`
- **Output:** `0`
- **Explanation:** The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Find Pivot Index**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,7,3,6,5,6]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11

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
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### JavaScript
```javascript
var pivotIndex = function(nums) {
    let totalSum = nums.reduce((sum, num) => sum + num, 0);
    let leftSum = 0;

    for (let i = 0; i < nums.length; i++) {
        let rightSum = totalSum - leftSum - nums[i];

        if (leftSum === rightSum) {
            return i;
        }

        leftSum += nums[i];
    }

    return -1;
};
```

### Python
```python
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):
            right_sum = total - left_sum - num

            if left_sum == right_sum:
                return i

            left_sum += num

        return -1
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
- [28. Find the Index of the First Occurrence in a String](../../0001-0500/0028-find-the-index-of-the-first-occurrence-in-a-string/)
- [1991. Find the Middle Index in Array](../../1501-2000/1991-find-the-middle-index-in-array/)
- [2485. Find the Pivot Integer](../../2001-2500/2485-find-the-pivot-integer/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-pivot-index/)
