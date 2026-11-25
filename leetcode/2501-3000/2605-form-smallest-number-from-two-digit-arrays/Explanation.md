# LeetCode 2605: Form Smallest Number From Two Digit Arrays

**LeetCode Problem #2605 — Form Smallest Number From Two Digit Arrays**
Solve LeetCode Form Smallest Number From Two Digit Arrays using Python and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Form Smallest Number From Two Digit Arrays |
| LeetCode | #2605 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given two arrays of **unique** digits `nums1` and `nums2`, return *the **smallest** number that contains **at least** one digit from each array*.

## Constraints
- `1 <= nums1.length, nums2.length <= 9`
- `1 <= nums1[i], nums2[i] <= 9`
- All digits in each array are **unique**.

## Examples
### Example 1
- **Input:** `nums1 = [4,1,3], nums2 = [5,7]`
- **Output:** `15`
- **Explanation:** The number 15 contains the digit 1 from nums1 and the digit 5 from nums2. It can be proven that 15 is the smallest number we can have.

### Example 2
- **Input:** `nums1 = [3,5,2,6], nums2 = [3,1,7]`
- **Output:** `3`
- **Explanation:** The number 3 contains the digit 3 which exists in both arrays.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Form Smallest Number From Two Digit Arrays**, we observe the problem requirements and utilize the **Math & Logic** technique. We iterate through the inputs using **Mathematical Simulation & Modular Arithmetic**, leveraging a **Primitive Types** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Primitive Types**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums1 = [4,1,3], nums2 = [5,7]`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `15`.
4. **Verification:** The number 15 contains the digit 1 from nums1 and the digit 5 from nums2. It can be proven that 15 is the smallest number we can have.

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
class Solution(object):
    def minNumber(self, nums1, nums2):
        common = set(nums1) & set(nums2)
        if common:
            return min(common)
            
        a, b = min(nums1), min(nums2)
        return min(a, b) * 10 + max(a, b)
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
- [2040. Kth Smallest Product of Two Sorted Arrays](../../2001-2500/2040-kth-smallest-product-of-two-sorted-arrays/)
- [2375. Construct Smallest Number From DI String](../../2001-2500/2375-construct-smallest-number-from-di-string/)
- [1442. Count Triplets That Can Form Two Arrays of Equal XOR](../../1001-1500/1442-count-triplets-that-can-form-two-arrays-of-equal-xor/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/)
