# LeetCode 2513: Minimize the Maximum of Two Arrays

**LeetCode Problem #2513 — Minimize the Maximum of Two Arrays**
Solve LeetCode Minimize the Maximum of Two Arrays using Python and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimize the Maximum of Two Arrays |
| LeetCode | #2513 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
We have two arrays `arr1` and `arr2` which are initially empty. You need to add positive integers to them such that they satisfy all the following conditions:

`arr1` contains `uniqueCnt1` **distinct** positive integers, each of which is **not divisible** by `divisor1`. 
 `arr2` contains `uniqueCnt2` **distinct** positive integers, each of which is **not divisible** by `divisor2`. 
 **No** integer is present in both `arr1` and `arr2`.

Given `divisor1`, `divisor2`, `uniqueCnt1`, and `uniqueCnt2`, return *the **minimum possible maximum** integer that can be present in either array*.

## Constraints
- `2 <= divisor1, divisor2 <= 10^5`
- `1 <= uniqueCnt1, uniqueCnt2 < 10^9`
- `2 <= uniqueCnt1 + uniqueCnt2 <= 10^9`

## Examples
### Example 1
- **Input:** `divisor1 = 2, divisor2 = 7, uniqueCnt1 = 1, uniqueCnt2 = 3`
- **Output:** `4`
- **Explanation:** We can distribute the first 4 natural numbers into arr1 and arr2.
arr1 = [1] and arr2 = [2,3,4].
We can see that both arrays satisfy all the conditions.
Since the maximum value is 4, we return it.

### Example 2
- **Input:** `divisor1 = 3, divisor2 = 5, uniqueCnt1 = 2, uniqueCnt2 = 1`
- **Output:** `3`
- **Explanation:** Here arr1 = [1,2], and arr2 = [3] satisfy all conditions.
Since the maximum value is 3, we return it.

### Example 3
- **Input:** `divisor1 = 2, divisor2 = 4, uniqueCnt1 = 8, uniqueCnt2 = 2`
- **Output:** `15`
- **Explanation:** Here, the final possible arrays can be arr1 = [1,3,5,7,9,11,13,15], and arr2 = [2,6].
It can be shown that it is not possible to obtain a lower maximum satisfying all conditions.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimize the Maximum of Two Arrays**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `divisor1 = 2, divisor2 = 7, uniqueCnt1 = 1, uniqueCnt2 = 3`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** We can distribute the first 4 natural numbers into arr1 and arr2.
arr1 = [1] and arr2 = [2,3,4].
We can see that both arrays satisfy all the conditions.
Since the maximum value is 4, we return it.

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
from math import gcd

class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        lcm = divisor1 * divisor2 // gcd(divisor1, divisor2)
        lo, hi = 1, 2 * (uniqueCnt1 + uniqueCnt2)

        while lo < hi:
            mid = (lo + hi) // 2
            a = mid - mid // divisor1
            b = mid - mid // divisor2
            both = mid - mid // lcm
            if a >= uniqueCnt1 and b >= uniqueCnt2 and both >= uniqueCnt1 + uniqueCnt2:
                hi = mid
            else:
                lo = mid + 1
        return lo
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
- [2035. Partition Array Into Two Arrays to Minimize Sum Difference](../../2001-2500/2035-partition-array-into-two-arrays-to-minimize-sum-difference/)
- [421. Maximum XOR of Two Numbers in an Array](../../0001-0500/0421-maximum-xor-of-two-numbers-in-an-array/)
- [1031. Maximum Sum of Two Non-Overlapping Subarrays](../../1001-1500/1031-maximum-sum-of-two-non-overlapping-subarrays/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/)
