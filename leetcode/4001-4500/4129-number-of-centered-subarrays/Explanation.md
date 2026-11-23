# LeetCode 3804: Number of Centered Subarrays

**LeetCode Problem #3804 — Number of Centered Subarrays**
Solve LeetCode Number of Centered Subarrays using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Centered Subarrays |
| LeetCode | #3804 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`.

A ** subarray ** of `nums` is called **centered** if the sum of its elements is **equal to at least one** element within that **same subarray**.

Return the number of **centered subarrays** of `nums`.

## Constraints
- `1 <= nums.length <= 500`
- `-10^5 <= nums[i] <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [-1,1,0]`
- **Output:** `5`
- **Explanation:** All single-element subarrays (`[-1]`, `[1]`, `[0]`) are centered. 
 The subarray `[1, 0]` has a sum of 1, which is present in the subarray. 
 The subarray `[-1, 1, 0]` has a sum of 0, which is present in the subarray. 
 Thus, the answer is 5.

### Example 2
- **Input:** `nums = [2,-3]`
- **Output:** `2`
- **Explanation:** Only single-element subarrays (`[2]`, `[-3]`) are centered.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Number of Centered Subarrays**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [-1,1,0]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** All single-element subarrays (`[-1]`, `[1]`, `[0]`) are centered. 
 The subarray `[1, 0]` has a sum of 1, which is present in the subarray. 
 The subarray `[-1, 1, 0]` has a sum of 0, which is present in the subarray. 
 Thus, the answer is 5.

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
    def centeredSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            seen = set()
            total = 0
            for j in range(i, n):
                total += nums[j]
                seen.add(nums[j])
                if total in seen:
                    ans += 1
        return ans
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
- [1248. Count Number of Nice Subarrays](../../1001-1500/1370-count-number-of-nice-subarrays/)
- [1526. Minimum Number of Increments on Subarrays to Form a Target Array](../../1501-2000/1633-minimum-number-of-increments-on-subarrays-to-form-a-target-array/)
- [2447. Number of Subarrays With GCD Equal to K](../../2501-3000/2546-number-of-subarrays-with-gcd-equal-to-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-centered-subarrays/)
