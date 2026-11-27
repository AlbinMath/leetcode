# LeetCode 268: Missing Number

**LeetCode Problem #268 — Missing Number**
Solve LeetCode Missing Number using PHP and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Missing Number |
| LeetCode | #268 |
| Difficulty | Easy |
| Language | PHP |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return *the only number in the range that is missing from the array.*

## Constraints
- `n == nums.length`
- `1 <= n <= 10^4`
- `0 <= nums[i] <= n`
- All the numbers of `nums` are **unique**.

## Examples
### Example 1
- **Input:** `nums = [3,0,1]`
- **Output:** `2`
- **Explanation:** `n = 3` since there are 3 numbers, so all numbers are in the range `[0,3]`. 2 is the missing number in the range since it does not appear in `nums`.

### Example 2
- **Input:** `nums = [0,1]`
- **Output:** `2`
- **Explanation:** `n = 2` since there are 2 numbers, so all numbers are in the range `[0,2]`. 2 is the missing number in the range since it does not appear in `nums`.

### Example 3
- **Input:** `nums = [9,6,4,2,3,5,7,0,1]`
- **Output:** `8`
- **Explanation:** `n = 9` since there are 9 numbers, so all numbers are in the range `[0,9]`. 8 is the missing number in the range since it does not appear in `nums`.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Missing Number**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,0,1]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** `n = 3` since there are 3 numbers, so all numbers are in the range `[0,3]`. 2 is the missing number in the range since it does not appear in `nums`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
PHP

## Source Code
- [solution.php](./solution.php)


```php
class Solution {
    function missingNumber($nums) {
        $n = count($nums);
        $missing = $n;

        for ($i = 0; $i < $n; $i++) {
            $missing ^= $i;
            $missing ^= $nums[$i];
        }

        return $missing;
    }
}
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
- [1539. Kth Missing Positive Number](../../1501-2000/1539-kth-missing-positive-number/)
- [9. Palindrome Number](../../0001-0500/0009-palindrome-number/)
- [17. Letter Combinations of a Phone Number](../../0001-0500/0017-letter-combinations-of-a-phone-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/missing-number/)
