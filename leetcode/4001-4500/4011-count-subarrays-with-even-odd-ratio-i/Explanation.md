# LeetCode 4011: Count Subarrays With Even Odd Ratio I

**LeetCode Problem #4011 — Count Subarrays With Even Odd Ratio I**
Solve LeetCode Count Subarrays With Even Odd Ratio I using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Subarrays With Even Odd Ratio I |
| LeetCode | #4011 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` and two integers `a` and `b`.

For a subarray , let:

`x` be the number of even elements. 
 `y` be the number of odd elements.

The ratio of even to odd elements in a subarray is defined as `x / y`, where ratios are compared by their exact rational values.

A subarray is considered **valid** if:

`y > 0`, and 
 `x / y <= a / b`.

Return the number of valid subarrays in `nums`.

## Constraints
- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 1000`
- `1 <= a, b <= 1000`

## Examples
### Example 1
- **Input:** `nums = [1,2,1,2], a = 3, b = 2`
- **Output:** `7`
- **Explanation:** The following are the valid subarrays: 

 
 
 
 Subarray 
 Values 
 Even Count 
 Odd Count 
 Ratio 
 
 
 `nums[0..0]` 
 `[1]` 
 0 
 1 
 `0 / 1` 
 
 
 `nums[0..1]` 
 `[1, 2]` 
 1 
 1 
 `1 / 1` 
 
 
 `nums[0..2]` 
 `[1, 2, 1]` 
 1 
 2 
 `1 / 2` 
 
 
 `nums[0..3]` 
 `[1, 2, 1, 2]` 
 2 
 2 
 `2 / 2` 
 
 
 `nums[1..2]` 
 `[2, 1]` 
 1 
 1 
 `1 / 1` 
 
 
 `nums[2..2]` 
 `[1]` 
 0 
 1 
 `0 / 1` 
 
 
 `nums[2..3]` 
 `[1, 2]` 
 1 
 1 
 `1 / 1` 
 
 
 

 Thus, the number of valid subarrays is 7.

### Example 2
- **Input:** `nums = [2,2,1], a = 2, b = 1`
- **Output:** `3`
- **Explanation:** The following are the valid subarrays: 

 
 
 
 Subarray 
 Values 
 Even Count 
 Odd Count 
 Ratio 
 
 
 `nums[0..2]` 
 `[2, 2, 1]` 
 2 
 1 
 `2 / 1` 
 
 
 `nums[1..2]` 
 `[2, 1]` 
 1 
 1 
 `1 / 1` 
 
 
 `nums[2..2]` 
 `[1]` 
 0 
 1 
 `0 / 1` 
 
 
 

 Thus, the number of valid subarrays is 3.

### Example 3
- **Input:** `nums = [2,2,2], a = 1, b = 1`
- **Output:** `0`
- **Explanation:** Every subarray contains 0 odd numbers, so no subarray is valid.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Count Subarrays With Even Odd Ratio I**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,1,2], a = 3, b = 2`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7`.
4. **Verification:** The following are the valid subarrays: 

 
 
 
 Subarray 
 Values 
 Even Count 
 Odd Count 
 Ratio 
 
 
 `nums[0..0]` 
 `[1]` 
 0 
 1 
 `0 / 1` 
 
 
 `nums[0..1]` 
 `[1, 2]` 
 1 
 1 
 `1 / 1` 
 
 
 `nums[0..2]` 
 `[1, 2, 1]` 
 1 
 2 
 `1 / 2` 
 
 
 `nums[0..3]` 
 `[1, 2, 1, 2]` 
 2 
 2 
 `2 / 2` 
 
 
 `nums[1..2]` 
 `[2, 1]` 
 1 
 1 
 `1 / 1` 
 
 
 `nums[2..2]` 
 `[1]` 
 0 
 1 
 `0 / 1` 
 
 
 `nums[2..3]` 
 `[1, 2]` 
 1 
 1 
 `1 / 1` 
 
 
 

 Thus, the number of valid subarrays is 7.

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
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def countRatioSubarrays(self, nums, a, b):
        n = len(nums)
        ans = 0

        for i in range(n):
            even = 0
            odd = 0

            for j in range(i, n):
                if nums[j] % 2 == 0:
                    even += 1
                else:
                    odd += 1

                if odd > 0 and even * b <= odd * a:
                    ans += 1

        return ans
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
- [4013. Count Subarrays With Even Odd Ratio II](../../4001-4500/4013-count-subarrays-with-even-odd-ratio-ii/)
- [1248. Count Number of Nice Subarrays](../../1001-1500/1248-count-number-of-nice-subarrays/)
- [1523. Count Odd Numbers in an Interval Range](../../1501-2000/1523-count-odd-numbers-in-an-interval-range/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-subarrays-with-even-odd-ratio-i/)
