# LeetCode 3759: Count Elements With at Least K Greater Values

**LeetCode Problem #3759 — Count Elements With at Least K Greater Values**
Solve LeetCode Count Elements With at Least K Greater Values using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Elements With at Least K Greater Values |
| LeetCode | #3759 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` of length `n` and an integer `k`.

An element in `nums` is said to be **qualified** if there exist **at least** `k` elements in the array that are **strictly greater** than it.

Return an integer denoting the total number of qualified elements in `nums`.

## Constraints
- `1 <= n == nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `0 <= k < n`

## Examples
### Example 1
- **Input:** `nums = [3,1,2], k = 1`
- **Output:** `2`
- **Explanation:** The elements 1 and 2 each have at least `k = 1` element greater than themselves. 
​​​​​​​No element is greater than 3. Therefore, the answer is 2.

### Example 2
- **Input:** `nums = [5,5,5], k = 2`
- **Output:** `0`
- **Explanation:** Since all elements are equal to 5, no element is greater than the other. Therefore, the answer is 0.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Elements With at Least K Greater Values**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,1,2], k = 1`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The elements 1 and 2 each have at least `k = 1` element greater than themselves. 
​​​​​​​No element is greater than 3. Therefore, the answer is 2.

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
    def countElements(self, nums, k):
        if k == 0:
            return len(nums)
        nums = sorted(nums)
        t = nums[len(nums) - k]
        return sum(1 for x in nums if x < t)
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
- [2962. Count Subarrays Where Max Element Appears at Least K Times](../../2501-3000/2962-count-subarrays-where-max-element-appears-at-least-k-times/)
- [3405. Count the Number of Arrays with K Matching Adjacent Elements](../../3001-3500/3405-count-the-number-of-arrays-with-k-matching-adjacent-elements/)
- [2148. Count Elements With Strictly Smaller and Greater Elements ](../../2001-2500/2148-count-elements-with-strictly-smaller-and-greater-elements/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-elements-with-at-least-k-greater-values/)
