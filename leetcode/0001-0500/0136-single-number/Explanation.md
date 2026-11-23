# LeetCode 136: Single Number

**LeetCode Problem #136 — Single Number**
Solve LeetCode Single Number using JavaScript, PHP, Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Single Number |
| LeetCode | #136 |
| Difficulty | Easy |
| Language | JavaScript, PHP, Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a **non-empty** array of integers `nums`, every element appears *twice* except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

## Constraints
- `1 <= nums.length <= 3 * 10^4`
- `-3 * 10^4 <= nums[i] <= 3 * 10^4`
- Each element in the array appears twice except for one element which appears only once.

## Examples
### Example 1
- **Input:** `nums = [2,2,1]`
- **Output:** `1`

### Example 2
- **Input:** `nums = [4,1,2,1,2]`
- **Output:** `4`

### Example 3
- **Input:** `nums = [1]`
- **Output:** `1`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Single Number**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,2,1]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript, PHP, Python

## Source Code
- [solution.js](./solution.js)
- [solution.php](./solution.php)
- [solution.py](./solution.py)


### JavaScript
```javascript
var singleNumber = function(nums) {
    let result = 0;

    for (const num of nums) {
        result ^= num;
    }

    return result;
};
```

### PHP
```php
class Solution {
    function singleNumber($nums) {
        $result = 0;

        foreach ($nums as $num) {
            $result ^= $num;
        }

        return $result;
    }
}
```

### Python
```python
from functools import reduce
from operator import xor

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        return reduce(xor, nums)
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
- [137. Single Number II](../../0001-0500/0137-single-number-ii/)
- [260. Single Number III](../../0001-0500/0260-single-number-iii/)
- [619. Biggest Single Number](../../0501-1000/0619-biggest-single-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/single-number/)
