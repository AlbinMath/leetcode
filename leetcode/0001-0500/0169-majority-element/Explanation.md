# LeetCode 169: Majority Element

**LeetCode Problem #169 — Majority Element**
Solve LeetCode Majority Element using JavaScript, PHP and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Majority Element |
| LeetCode | #169 |
| Difficulty | Easy |
| Language | JavaScript, PHP |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array `nums` of size `n`, return *the majority element*.

The majority element is the element that appears more than `&lfloor;n / 2&rfloor;` times. You may assume that the majority element always exists in the array.

## Constraints
- `n == nums.length`
- `1 <= n <= 5 * 10^4`
- `-10^9 <= nums[i] <= 10^9`
- The input is generated such that a majority element will exist in the array.

## Examples
### Example 1
- **Input:** `nums = [3,2,3]`
- **Output:** `3`

### Example 2
- **Input:** `nums = [2,2,1,1,1,2,2]`
- **Output:** `2`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Majority Element**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,2,3]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript, PHP

## Source Code
- [solution.js](./solution.js)
- [solution.php](./solution.php)


### JavaScript
```javascript
var majorityElement = function(nums) {
    let candidate = 0;
    let count = 0;

    for (const num of nums) {
        if (count === 0) {
            candidate = num;
        }

        if (num === candidate) {
            count++;
        } else {
            count--;
        }
    }

    return candidate;
};
```

### PHP
```php
class Solution {
    function majorityElement($nums) {
        $candidate = 0;
        $count = 0;

        foreach ($nums as $num) {
            // Choose a new candidate when count becomes 0
            if ($count == 0) {
                $candidate = $num;
            }

            // Vote for or against the candidate
            if ($num == $candidate) {
                $count++;
            } else {
                $count--;
            }
        }

        return $candidate;
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
- [229. Majority Element II](../../0001-0500/0229-majority-element-ii/)
- [1157. Online Majority Element In Subarray](../../1001-1500/1157-online-majority-element-in-subarray/)
- [3737. Count Subarrays With Majority Element I](../../3501-4000/3737-count-subarrays-with-majority-element-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/majority-element/)
