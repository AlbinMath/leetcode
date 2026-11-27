# LeetCode 1764: Form Array by Concatenating Subarrays of Another Array

**LeetCode Problem #1764 — Form Array by Concatenating Subarrays of Another Array**
Solve LeetCode Form Array by Concatenating Subarrays of Another Array using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Form Array by Concatenating Subarrays of Another Array |
| LeetCode | #1764 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a 2D integer array `groups` of length `n`. You are also given an integer array `nums`.

You are asked if you can choose `n` **disjoint **subarrays from the array `nums` such that the `i^th` subarray is equal to `groups[i]` ( 0-indexed ), and if `i > 0`, the `(i-1)^th` subarray appears **before** the `i^th` subarray in `nums` (i.e. the subarrays must be in the same order as `groups`).

Return `true` *if you can do this task, and* `false` *otherwise*.

Note that the subarrays are **disjoint** if and only if there is no index `k` such that `nums[k]` belongs to more than one subarray. A subarray is a contiguous sequence of elements within an array.

## Constraints
- `groups.length == n`
- `1 <= n <= 10^3`
- `1 <= groups[i].length, sum(groups[i].length) <= 10^ 3 `
- `1 <= nums.length <= 10^3`
- `-10^7 <= groups[i][j], nums[k] <= 10^7`

## Examples
### Example 1
- **Input:** `groups = [[1,-1,-1],[3,-2,0]], nums = [1,-1,0,1,-1,-1,3,-2,0]`
- **Output:** `true`
- **Explanation:** You can choose the 0^th subarray as [1,-1,0,

### Example 2
- **Input:** `groups = [[10,-2],[1,2,3,4]], nums = [1,2,3,4,10,-2]`
- **Output:** `false`
- **Explanation:** Note that choosing the subarrays [

### Example 3
- **Input:** `groups = [[1,2,3],[3,4]], nums = [7,7,1,2,3,4,7,7]`
- **Output:** `false`
- **Explanation:** Note that choosing the subarrays [7,7,

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Form Array by Concatenating Subarrays of Another Array**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `groups = [[1,-1,-1],[3,-2,0]], nums = [1,-1,0,1,-1,-1,3,-2,0]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** You can choose the 0^th subarray as [1,-1,0,

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
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        pos = 0
        n = len(nums)
        for g in groups:
            m = len(g)
            found = False
            while pos + m <= n:
                if nums[pos:pos + m] == g:
                    pos += m
                    found = True
                    break
                pos += 1
            if not found:
                return False
        return True
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
- [1526. Minimum Number of Increments on Subarrays to Form a Target Array](../../1501-2000/1526-minimum-number-of-increments-on-subarrays-to-form-a-target-array/)
- [989. Add to Array-Form of Integer](../../0501-1000/0989-add-to-array-form-of-integer/)
- [1712. Ways to Split Array Into Three Subarrays](../../1501-2000/1712-ways-to-split-array-into-three-subarrays/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/form-array-by-concatenating-subarrays-of-another-array/)
