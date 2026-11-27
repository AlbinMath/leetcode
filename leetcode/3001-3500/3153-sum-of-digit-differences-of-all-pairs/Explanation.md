# LeetCode 3153: Sum of Digit Differences of All Pairs

**LeetCode Problem #3153 — Sum of Digit Differences of All Pairs**
Solve LeetCode Sum of Digit Differences of All Pairs using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sum of Digit Differences of All Pairs |
| LeetCode | #3153 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array `nums` consisting of **positive** integers where all integers have the **same** number of digits.

The **digit difference** between two integers is the *count* of different digits that are in the **same** position in the two integers.

Return the **sum** of the **digit differences** between **all** pairs of integers in `nums`.

## Constraints
- `2 <= nums.length <= 10^5`
- `1 <= nums[i] < 10^9`
- All integers in `nums` have the same number of digits.

## Examples
### Example 1
- **Input:** `nums = [13,23,12]`
- **Output:** `4`
- **Explanation:** We have the following: 
- The digit difference between

### Example 2
- **Input:** `nums = [10,10,10,10]`
- **Output:** `0`
- **Explanation:** All the integers in the array are the same. So the total sum of digit differences between all pairs of integers will be 0.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Sum of Digit Differences of All Pairs**, we observe the problem requirements and utilize the **Math & Logic** technique. We iterate through the inputs using **Mathematical Simulation & Modular Arithmetic**, leveraging a **Primitive Types** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Primitive Types**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [13,23,12]`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** We have the following: 
- The digit difference between

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Integer Bitmask.

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def sumDigitDifferences(self, nums: list[int]) -> int:
        n = len(nums)
        total_diff = 0
        
        while nums[0] > 0:
            cnt = [0] * 10
            for i in range(n):
                cnt[nums[i] % 10] += 1
                nums[i] //= 10
                
            total_diff += sum(c * (n - c) for c in cnt) // 2
            
        return total_diff
```

## Why This Works
By utilizing **Bit Manipulation**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1835. Find XOR Sum of All Pairs Bitwise AND](../../1501-2000/1835-find-xor-sum-of-all-pairs-bitwise-and/)
- [2160. Minimum Sum of Four Digit Number After Splitting Digits](../../2001-2500/2160-minimum-sum-of-four-digit-number-after-splitting-digits/)
- [2180. Count Integers With Even Digit Sum](../../2001-2500/2180-count-integers-with-even-digit-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sum-of-digit-differences-of-all-pairs/)
