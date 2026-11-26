# LeetCode 1295: Find Numbers with Even Number of Digits

**LeetCode Problem #1295 — Find Numbers with Even Number of Digits**
Solve LeetCode Find Numbers with Even Number of Digits using Python and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Numbers with Even Number of Digits |
| LeetCode | #1295 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array `nums` of integers, return how many of them contain an **even number** of digits.

## Constraints
- `1 <= nums.length <= 500`
- `1 <= nums[i] <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [12,345,2,6,7896]`
- **Output:** `2`
- **Explanation:** 12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.

### Example 2
- **Input:** `nums = [555,901,482,1771]`
- **Output:** `1`
- **Explanation:** Only 1771 contains an even number of digits.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find Numbers with Even Number of Digits**, we observe the problem requirements and utilize the **Math & Logic** technique. We iterate through the inputs using **Mathematical Simulation & Modular Arithmetic**, leveraging a **Primitive Types** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Primitive Types**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [12,345,2,6,7896]`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** 12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.

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
class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count = 0

        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1

        return count
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
- [287. Find the Duplicate Number](../../0001-0500/0287-find-the-duplicate-number/)
- [1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance](../../1001-1500/1334-find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/)
- [1365. How Many Numbers Are Smaller Than the Current Number](../../1001-1500/1365-how-many-numbers-are-smaller-than-the-current-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-numbers-with-even-number-of-digits/)
