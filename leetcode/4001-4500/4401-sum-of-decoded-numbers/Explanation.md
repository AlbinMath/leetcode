# LeetCode 4039: Sum of Decoded Numbers

**LeetCode Problem #4039 — Sum of Decoded Numbers**
Solve LeetCode Sum of Decoded Numbers using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sum of Decoded Numbers |
| LeetCode | #4039 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`.

Each `nums[i]` is an **encoded** integer representing two positive integers `x_i` and `y_i`. To decode `nums[i]`, define:

`width_i = nums[i] % 10`. 
 `d_i = floor(nums[i] / 10)`. 
 `x_i` as the integer formed by the first `width_i` digits of the decimal representation of `d_i`. 
 `y_i` as the integer formed by all remaining digits of the decimal representation of `d_i`.

It is guaranteed that the decimal representation of `d_i` contains more than `width_i` digits. Therefore, both `x_i` and `y_i` contain at least one digit.

The **decoded value** of `nums[i]` is `x_i^y_i`.

Return the sum of the decoded values of all elements in `nums`, modulo `10^9 + 7`.

The `floor()` function returns the integer part of the division.

## Constraints
- `1 <= nums.length <= 10^5`
- `100 < nums[i] < 10^15`
- `1 <= width_i <= 9`
- `1 <= x_i, y_i < 10^9`
- The digit sequences used to form `x_i` and `y_i` do not have leading zeros.
- It is guaranteed that every element in `nums` is a valid encoded integer.

## Examples
### Example 1
- **Input:** `nums = [231]`
- **Output:** `8`
- **Explanation:** For 231, we have `width = 1`, `d = 23`, `x = 2`, and `y = 3`. 
 The decoded value of 231 is `2^3 = 8`. 
 Since there is only one element in `nums`, the sum of the decoded values is 8.

### Example 2
- **Input:** `nums = [2522,2101]`
- **Output:** `1649`
- **Explanation:** For 2522, we have `width = 2`, `d = 252`, `x = 25`, and `y = 2`. 
 The decoded value of 2522 is `25^2 = 625`. 
 For 2101, we have `width = 1`, `d = 210`, `x = 2`, and `y = 10`. 
 The decoded value of 2101 is `2^10 = 1024`. 
 The sum of the decoded values is `625 + 1024 = 1649`.

### Example 3
- **Input:** `nums = [2301]`
- **Output:** `73741817`
- **Explanation:** For 2301, we have `width = 1`, `d = 230`, `x = 2`, and `y = 30`. 
 The decoded value is `2^30 = 1073741824`. 
 Therefore, the answer is `1073741824 modulo (10^9 + 7) = 73741817`.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Sum of Decoded Numbers**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [231]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `8`.
4. **Verification:** For 231, we have `width = 1`, `d = 23`, `x = 2`, and `y = 3`. 
 The decoded value of 231 is `2^3 = 8`. 
 Since there is only one element in `nums`, the sum of the decoded values is 8.

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
class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        ans = 0
        for v in nums:
            w = v % 10
            d = str(v // 10)
            x = int(d[:w])
            y = int(d[w:])
            ans = (ans + pow(x, y, MOD)) % MOD
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
- [129. Sum Root to Leaf Numbers](../../0001-0500/0129-sum-root-to-leaf-numbers/)
- [633. Sum of Square Numbers](../../0501-1000/0633-sum-of-square-numbers/)
- [829. Consecutive Numbers Sum](../../0501-1000/0856-consecutive-numbers-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sum-of-decoded-numbers/)
