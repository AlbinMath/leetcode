# LeetCode 217: Contains Duplicate

**LeetCode Problem #217 — Contains Duplicate**
Solve LeetCode Contains Duplicate using PHP and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Contains Duplicate |
| LeetCode | #217 |
| Difficulty | Easy |
| Language | PHP |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [1,2,3,1]`
- **Output:** `true`
- **Explanation:** The element 1 occurs at the indices 0 and 3.

### Example 2
- **Input:** `nums = [1,2,3,4]`
- **Output:** `false`
- **Explanation:** All elements are distinct.

### Example 3
- **Input:** `nums = [1,1,1,3,3,4,3,2,4,2]`
- **Output:** `true`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Contains Duplicate**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,1]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** The element 1 occurs at the indices 0 and 3.

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
    function containsDuplicate($nums) {
        $seen = [];

        foreach ($nums as $num) {
            if (isset($seen[$num])) {
                return true;
            }

            $seen[$num] = true;
        }

        return false;
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
- [219. Contains Duplicate II](../../0001-0500/0219-contains-duplicate-ii/)
- [220. Contains Duplicate III](../../0001-0500/0220-contains-duplicate-iii/)
- [182. Duplicate Emails](../../0001-0500/0182-duplicate-emails/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/contains-duplicate/)
