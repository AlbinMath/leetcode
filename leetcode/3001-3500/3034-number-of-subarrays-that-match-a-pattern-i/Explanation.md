# LeetCode 3034: Number of Subarrays That Match a Pattern I

**LeetCode Problem #3034 — Number of Subarrays That Match a Pattern I**
Solve LeetCode Number of Subarrays That Match a Pattern I using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Subarrays That Match a Pattern I |
| LeetCode | #3034 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** integer array `nums` of size `n`, and a **0-indexed** integer array `pattern` of size `m` consisting of integers `-1`, `0`, and `1`.

A subarray `nums[i..j]` of size `m + 1` is said to match the `pattern` if the following conditions hold for each element `pattern[k]`:

`nums[i + k + 1] > nums[i + k]` if `pattern[k] == 1`. 
 `nums[i + k + 1] == nums[i + k]` if `pattern[k] == 0`. 
 `nums[i + k + 1] < nums[i + k]` if `pattern[k] == -1`.

Return *the** count** of subarrays in* `nums` *that match the* `pattern`.

## Constraints
- `2 <= n == nums.length <= 100`
- `1 <= nums[i] <= 10^9`
- `1 <= m == pattern.length < n`
- `-1 <= pattern[i] <= 1`

## Examples
### Example 1
- **Input:** `nums = [1,2,3,4,5,6], pattern = [1,1]`
- **Output:** `4`
- **Explanation:** The pattern [1,1] indicates that we are looking for strictly increasing subarrays of size 3. In the array nums, the subarrays [1,2,3], [2,3,4], [3,4,5], and [4,5,6] match this pattern.
Hence, there are 4 subarrays in nums that match the pattern.

### Example 2
- **Input:** `nums = [1,4,4,1,3,5,5,3], pattern = [1,0,-1]`
- **Output:** `2`
- **Explanation:** Here, the pattern [1,0,-1] indicates that we are looking for a sequence where the first number is smaller than the second, the second is equal to the third, and the third is greater than the fourth. In the array nums, the subarrays [1,4,4,1], and [3,5,5,3] match this pattern.
Hence, there are 2 subarrays in nums that match the pattern.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Number of Subarrays That Match a Pattern I**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,4,5,6], pattern = [1,1]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The pattern [1,1] indicates that we are looking for strictly increasing subarrays of size 3. In the array nums, the subarrays [1,2,3], [2,3,4], [3,4,5], and [4,5,6] match this pattern.
Hence, there are 4 subarrays in nums that match the pattern.

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
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n, m = len(nums), len(pattern)
        count = 0
        for i in range(n - m):
            ok = True
            for k in range(m):
                a, b = nums[i + k], nums[i + k + 1]
                diff = (b > a) - (b < a)      # 1, 0, or -1
                if diff != pattern[k]:
                    ok = False
                    break
            if ok:
                count += 1
        return count
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
- [3036. Number of Subarrays That Match a Pattern II](../../3001-3500/3036-number-of-subarrays-that-match-a-pattern-ii/)
- [1074. Number of Submatrices That Sum to Target](../../1001-1500/1074-number-of-submatrices-that-sum-to-target/)
- [1248. Count Number of Nice Subarrays](../../1001-1500/1248-count-number-of-nice-subarrays/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-i/)
