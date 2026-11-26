# LeetCode 228: Summary Ranges

**LeetCode Problem #228 — Summary Ranges**
Solve LeetCode Summary Ranges using PHP and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Summary Ranges |
| LeetCode | #228 |
| Difficulty | Easy |
| Language | PHP |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **sorted unique** integer array `nums`.

A **range** `[a,b]` is the set of all integers from `a` to `b` (inclusive).

Return *the **smallest sorted** list of ranges that **cover all the numbers in the array exactly***. That is, each element of `nums` is covered by exactly one of the ranges, and there is no integer `x` such that `x` is in one of the ranges but not in `nums`.

Each range `[a,b]` in the list should be output as:

`"a->b"` if `a != b` 
 `"a"` if `a == b`

## Constraints
- `0 <= nums.length <= 20`
- `-2^31 <= nums[i] <= 2^31 - 1`
- All the values of `nums` are **unique**.
- `nums` is sorted in ascending order.

## Examples
### Example 1
- **Input:** `nums = [0,1,2,4,5,7]`
- **Output:** `["0->2","4->5","7"]`
- **Explanation:** The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

### Example 2
- **Input:** `nums = [0,2,3,4,6,8,9]`
- **Output:** `["0","2->4","6","8->9"]`
- **Explanation:** The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Summary Ranges**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [0,1,2,4,5,7]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `["0->2","4->5","7"]`.
4. **Verification:** The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

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
PHP

## Source Code
- [solution.php](./solution.php)


```php
class Solution {
    function summaryRanges($nums) {
        $result = [];
        $n = count($nums);

        if ($n == 0) {
            return $result;
        }

        $start = 0;

        for ($i = 1; $i <= $n; $i++) {
            // Range ends if we reach the end
            // or the numbers are no longer consecutive
            if ($i == $n || $nums[$i] != $nums[$i - 1] + 1) {
                if ($start == $i - 1) {
                    // Single number
                    $result[] = (string)$nums[$start];
                } else {
                    // Range
                    $result[] = $nums[$start] . "->" . $nums[$i - 1];
                }

                // Start a new range
                $start = $i;
            }
        }

        return $result;
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
- [1587. Bank Account Summary II](../../1501-2000/1587-bank-account-summary-ii/)
- [2104. Sum of Subarray Ranges](../../2001-2500/2104-sum-of-subarray-ranges/)
- [2559. Count Vowel Strings in Ranges](../../2501-3000/2559-count-vowel-strings-in-ranges/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/summary-ranges/)
