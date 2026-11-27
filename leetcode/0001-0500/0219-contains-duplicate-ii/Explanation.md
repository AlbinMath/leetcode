# LeetCode 219: Contains Duplicate II

**LeetCode Problem #219 — Contains Duplicate II**
Solve LeetCode Contains Duplicate II using PHP, Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Contains Duplicate II |
| LeetCode | #219 |
| Difficulty | Easy |
| Language | PHP, Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `nums` and an integer `k`, return `true` *if there are two **distinct indices** *`i`* and *`j`* in the array such that *`nums[i] == nums[j]`* and *`abs(i - j) <= k`.

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `0 <= k <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [1,2,3,1], k = 3`
- **Output:** `true`

### Example 2
- **Input:** `nums = [1,0,1,1], k = 1`
- **Output:** `true`

### Example 3
- **Input:** `nums = [1,2,3,1,2,3], k = 2`
- **Output:** `false`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Contains Duplicate II**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,1], k = 3`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
PHP, Python

## Source Code
- [solution.php](./solution.php)
- [solution.py](./solution.py)


### PHP
```php
class Solution {
    function containsNearbyDuplicate($nums, $k) {
        $lastIndex = [];

        for ($i = 0; $i < count($nums); $i++) {
            $num = $nums[$i];

            // Number appeared before
            if (isset($lastIndex[$num])) {
                if ($i - $lastIndex[$num] <= $k) {
                    return true;
                }
            }

            // Store the latest index
            $lastIndex[$num] = $i;
        }

        return false;
    }
}
```

### Python
```python
from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}

        for i, x in enumerate(nums):
            if x in seen and i - seen[x] <= k:
                return True
            seen[x] = i

        return False
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
- [217. Contains Duplicate](../../0001-0500/0217-contains-duplicate/)
- [220. Contains Duplicate III](../../0001-0500/0220-contains-duplicate-iii/)
- [182. Duplicate Emails](../../0001-0500/0182-duplicate-emails/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/contains-duplicate-ii/)
