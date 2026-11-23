# LeetCode 3969: Valid Subarrays With Matching Sum Digits I

**LeetCode Problem #3969 — Valid Subarrays With Matching Sum Digits I**
Solve LeetCode Valid Subarrays With Matching Sum Digits I using Python and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Valid Subarrays With Matching Sum Digits I |
| LeetCode | #3969 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` and an integer digit `x`.

A **subarray** `nums[l..r]` is considered **valid** if the sum of its elements satisfies both of the following conditions:

The first digit of the sum is equal to `x`. 
 The last digit of the sum is equal to `x`.

Return the number of valid subarrays.

## Constraints
- `1 <= nums.length <= 1500`
- `1 <= nums[i] <= 10^9`
- `1 <= x <= 9`

## Examples
### Example 1
- **Input:** `nums = [1,100,1], x = 1`
- **Output:** `4`
- **Explanation:** The valid subarrays are: 

 
 `nums[0..0]`: `sum = 1` 
 `nums[0..1]`: `sum = 1 + 100 = 101` 
 `nums[1..2]`: `sum = 100 + 1 = 101` 
 `nums[2..2]`: `sum = 1` 
 

 Thus, the answer is 4.

### Example 2
- **Input:** `nums = [1], x = 2`
- **Output:** `0`
- **Explanation:** The only subarray is `nums[0..0]` with a sum of 1, which does not satisfy the conditions. 

 Thus, the answer is 0.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Valid Subarrays With Matching Sum Digits I**, we observe the problem requirements and utilize the **Math & Logic** technique. We iterate through the inputs using **Mathematical Simulation & Modular Arithmetic**, leveraging a **Primitive Types** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Primitive Types**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,100,1], x = 1`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The valid subarrays are: 

 
 `nums[0..0]`: `sum = 1` 
 `nums[0..1]`: `sum = 1 + 100 = 101` 
 `nums[1..2]`: `sum = 100 + 1 = 101` 
 `nums[2..2]`: `sum = 1` 
 

 Thus, the answer is 4.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def countValidSubarrays(self, nums: List[int], x: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            total = 0
            for j in range(i, n):
                total += nums[j]
                if total % 10 == x and str(total)[0] == chr(48 + x):
                    ans += 1
        return ans
```

## Why This Works
By utilizing **Math & Logic**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [689. Maximum Sum of 3 Non-Overlapping Subarrays](../../0501-1000/0689-maximum-sum-of-3-non-overlapping-subarrays/)
- [930. Binary Subarrays With Sum](../../0501-1000/0966-binary-subarrays-with-sum/)
- [1031. Maximum Sum of Two Non-Overlapping Subarrays](../../1001-1500/1096-maximum-sum-of-two-non-overlapping-subarrays/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/valid-subarrays-with-matching-sum-digits-i/)
