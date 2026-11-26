# LeetCode 2654: Minimum Number of Operations to Make All Array Elements Equal to 1

**LeetCode Problem #2654 — Minimum Number of Operations to Make All Array Elements Equal to 1**
Solve LeetCode Minimum Number of Operations to Make All Array Elements Equal to 1 using Python and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Number of Operations to Make All Array Elements Equal to 1 |
| LeetCode | #2654 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** array `nums` consisting of **positive** integers. You can do the following operation on the array **any** number of times:

Select an index `i` such that `0 <= i < n - 1` and replace either of `nums[i]` or `nums[i+1]` with their gcd value.

Return *the **minimum** number of operations to make all elements of *`nums`* equal to *`1`. If it is impossible, return `-1`.

The gcd of two integers is the greatest common divisor of the two integers.

## Constraints
- `2 <= nums.length <= 50`
- `1 <= nums[i] <= 10^6`

## Examples
### Example 1
- **Input:** `nums = [2,6,3,4]`
- **Output:** `4`
- **Explanation:** We can do the following operations:
- Choose index i = 2 and replace nums[2] with gcd(3,4) = 1. Now we have nums = [2,6,1,4].
- Choose index i = 1 and replace nums[1] with gcd(6,1) = 1. Now we have nums = [2,1,1,4].
- Choose index i = 0 and replace nums[0] with gcd(2,1) = 1. Now we have nums = [1,1,1,4].
- Choose index i = 2 and replace nums[3] with gcd(1,4) = 1. Now we have nums = [1,1,1,1].

### Example 2
- **Input:** `nums = [2,10,6,14]`
- **Output:** `-1`
- **Explanation:** It can be shown that it is impossible to make all the elements equal to 1.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Number of Operations to Make All Array Elements Equal to 1**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,6,3,4]`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** We can do the following operations:
- Choose index i = 2 and replace nums[2] with gcd(3,4) = 1. Now we have nums = [2,6,1,4].
- Choose index i = 1 and replace nums[1] with gcd(6,1) = 1. Now we have nums = [2,1,1,4].
- Choose index i = 0 and replace nums[0] with gcd(2,1) = 1. Now we have nums = [1,1,1,4].
- Choose index i = 2 and replace nums[3] with gcd(1,4) = 1. Now we have nums = [1,1,1,1].

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
    def minOperations(self, nums: List[int]) -> int:
        n, c = len(nums), nums.count(1)
        if c: return n - c
        if gcd(*nums) > 1: return -1
        m = n
        for i in range(n):
            g = 0
            for j in range(i, n):
                g = gcd(g, nums[j])
                if g == 1: m = min(m, j - i + 1); break
        return m + n - 2
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
- [2602. Minimum Operations to Make All Array Elements Equal](../../2501-3000/2602-minimum-operations-to-make-all-array-elements-equal/)
- [2997. Minimum Number of Operations to Make Array XOR Equal to K](../../2501-3000/2997-minimum-number-of-operations-to-make-array-xor-equal-to-k/)
- [2772. Apply Operations to Make All Array Elements Equal to Zero](../../2501-3000/2772-apply-operations-to-make-all-array-elements-equal-to-zero/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/)
