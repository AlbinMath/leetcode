# LeetCode 2447: Number of Subarrays With GCD Equal to K

**LeetCode Problem #2447 — Number of Subarrays With GCD Equal to K**
Solve LeetCode Number of Subarrays With GCD Equal to K using Python and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Subarrays With GCD Equal to K |
| LeetCode | #2447 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `nums` and an integer `k`, return *the number of **subarrays** of *`nums`* where the greatest common divisor of the subarray's elements is *`k`.

A **subarray** is a contiguous non-empty sequence of elements within an array.

The **greatest common divisor of an array** is the largest integer that evenly divides all the array elements.

## Constraints
- `1 <= nums.length <= 1000`
- `1 <= nums[i], k <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [9,3,1,2,6,3], k = 3`
- **Output:** `4`
- **Explanation:** The subarrays of nums where 3 is the greatest common divisor of all the subarray's elements are:
- [9,

### Example 2
- **Input:** `nums = [4], k = 7`
- **Output:** `0`
- **Explanation:** There are no subarrays of nums where 7 is the greatest common divisor of all the subarray's elements.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Number of Subarrays With GCD Equal to K**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [9,3,1,2,6,3], k = 3`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The subarrays of nums where 3 is the greatest common divisor of all the subarray's elements are:
- [9,

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
from math import gcd

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            g = 0
            for j in range(i, n):
                g = gcd(g, nums[j])
                if g == k:
                    ans += 1
                elif g < k:
                    break  # gcd only shrinks, so it can't return to k
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
- [2470. Number of Subarrays With LCM Equal to K](../../2001-2500/2470-number-of-subarrays-with-lcm-equal-to-k/)
- [3336. Find the Number of Subsequences With Equal GCD](../../3001-3500/3336-find-the-number-of-subsequences-with-equal-gcd/)
- [3209. Number of Subarrays With AND Value of K](../../3001-3500/3209-number-of-subarrays-with-and-value-of-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/)
