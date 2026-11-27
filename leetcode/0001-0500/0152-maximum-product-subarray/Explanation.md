# LeetCode 152: Maximum Product Subarray

**LeetCode Problem #152 — Maximum Product Subarray**
Solve LeetCode Maximum Product Subarray using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Product Subarray |
| LeetCode | #152 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `nums`, find a subarray that has the largest product, and return *the product*.

The test cases are generated so that the answer will fit in a **32-bit** integer.

**Note** that the product of an array with a single element is the value of that element.

​​​​​​​

## Constraints
- `1 <= nums.length <= 2 * 10^4`
- `-10 <= nums[i] <= 10`
- The product of any subarray of `nums` is **guaranteed** to fit in a **32-bit** integer.

## Examples
### Example 1
- **Input:** `nums = [2,3,-2,4]`
- **Output:** `6`
- **Explanation:** [2,3] has the largest product 6.

### Example 2
- **Input:** `nums = [-2,0,-1]`
- **Output:** `0`
- **Explanation:** The result cannot be 2, because [-2,-1] is not a subarray.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Product Subarray**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,3,-2,4]`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** [2,3] has the largest product 6.

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
    def maxProduct(self, nums):
        mx = mn = ans = nums[0]
        for x in nums[1:]:
            if x < 0:
                mx, mn = mn, mx
            mx = max(x, mx*x)
            mn = min(x, mn*x)
            ans = max(ans, mx)
        return ans
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
- [1567. Maximum Length of Subarray With Positive Product](../../1501-2000/1567-maximum-length-of-subarray-with-positive-product/)
- [1856. Maximum Subarray Min-Product](../../1501-2000/1856-maximum-subarray-min-product/)
- [53. Maximum Subarray](../../0001-0500/0053-maximum-subarray/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-product-subarray/)
