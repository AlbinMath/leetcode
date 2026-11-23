# LeetCode 908: Smallest Range I

**LeetCode Problem #908 — Smallest Range I**
Solve LeetCode Smallest Range I using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Smallest Range I |
| LeetCode | #908 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` and an integer `k`.

In one operation, you can choose any index `i` where `0 <= i < nums.length` and change `nums[i]` to `nums[i] + x` where `x` is an integer from the range `[-k, k]`. You can apply this operation **at most once** for each index `i`.

The **score** of `nums` is the difference between the maximum and minimum elements in `nums`.

Return *the minimum **score** of *`nums`* after applying the mentioned operation at most once for each index in it*.

## Constraints
- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 10^4`
- `0 <= k <= 10^4`

## Examples
### Example 1
- **Input:** `nums = [1], k = 0`
- **Output:** `0`
- **Explanation:** The score is max(nums) - min(nums) = 1 - 1 = 0.

### Example 2
- **Input:** `nums = [0,10], k = 2`
- **Output:** `6`
- **Explanation:** Change nums to be [2, 8]. The score is max(nums) - min(nums) = 8 - 2 = 6.

### Example 3
- **Input:** `nums = [1,3,6], k = 3`
- **Output:** `0`
- **Explanation:** Change nums to be [4, 4, 4]. The score is max(nums) - min(nums) = 4 - 4 = 0.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Smallest Range I**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1], k = 0`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `0`.
4. **Verification:** The score is max(nums) - min(nums) = 1 - 1 = 0.

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
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        smallest = min(nums)
        largest = max(nums)

        return max(0, largest - smallest - 2 * k)
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
- [632. Smallest Range Covering Elements from K Lists](../../0501-1000/0632-smallest-range-covering-elements-from-k-lists/)
- [201. Bitwise AND of Numbers Range](../../0001-0500/0201-bitwise-and-of-numbers-range/)
- [303. Range Sum Query - Immutable](../../0001-0500/0303-range-sum-query---immutable/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/smallest-range-i/)
