# LeetCode 1248: Count Number of Nice Subarrays

**LeetCode Problem #1248 — Count Number of Nice Subarrays**
Solve LeetCode Count Number of Nice Subarrays using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Number of Nice Subarrays |
| LeetCode | #1248 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array of integers `nums` and an integer `k`. A continuous subarray is called **nice** if there are `k` odd numbers on it.

Return *the number of **nice** sub-arrays*.

## Constraints
- `1 <= nums.length <= 50000`
- `1 <= nums[i] <= 10^5`
- `1 <= k <= nums.length`

## Examples
### Example 1
- **Input:** `nums = [1,1,2,1,1], k = 3`
- **Output:** `2`
- **Explanation:** The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

### Example 2
- **Input:** `nums = [2,4,6], k = 1`
- **Output:** `0`
- **Explanation:** There are no odd numbers in the array.

### Example 3
- **Input:** `nums = [2,2,2,1,2,2,1,2,2,2], k = 2`
- **Output:** `16`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Number of Nice Subarrays**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,1,2,1,1], k = 3`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left = odd_count = valid_prefixes = total = 0
        
        for val in nums:
            if val & 1:
                odd_count += 1
                valid_prefixes = 0
                
            while odd_count == k:
                odd_count -= nums[left] & 1
                left += 1
                valid_prefixes += 1
                
            total += valid_prefixes
            
        return total
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
- [2537. Count the Number of Good Subarrays](../../2501-3000/2626-count-the-number-of-good-subarrays/)
- [2588. Count the Number of Beautiful Subarrays](../../2501-3000/2656-count-the-number-of-beautiful-subarrays/)
- [2970. Count the Number of Incremovable Subarrays I](../../3001-3500/3252-count-the-number-of-incremovable-subarrays-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-number-of-nice-subarrays/)
