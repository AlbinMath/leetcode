# LeetCode 2588: Count the Number of Beautiful Subarrays

**LeetCode Problem #2588 — Count the Number of Beautiful Subarrays**
Solve LeetCode Count the Number of Beautiful Subarrays using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count the Number of Beautiful Subarrays |
| LeetCode | #2588 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** integer array `nums`. In one operation, you can:

Choose two different indices `i` and `j` such that `0 <= i, j < nums.length`. 
 Choose a non-negative integer `k` such that the `k^th` bit (**0-indexed**) in the binary representation of `nums[i]` and `nums[j]` is `1`. 
 Subtract `2^k` from `nums[i]` and `nums[j]`.

A subarray is **beautiful** if it is possible to make all of its elements equal to `0` after applying the above operation any number of times (including zero).

Return *the number of **beautiful subarrays** in the array* `nums`.

A subarray is a contiguous **non-empty** sequence of elements within an array.

**Note**: Subarrays where all elements are initially 0 are considered beautiful, as no operation is needed.

## Constraints
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^6`

## Examples
### Example 1
- **Input:** `nums = [4,3,1,2,4]`
- **Output:** `2`
- **Explanation:** There are 2 beautiful subarrays in nums: [4, 3,1,2 ,4] and [ 4,3,1,2,4 ].
- We can make all elements in the subarray [3,1,2] equal to 0 in the following way:
 - Choose [ 3 , 1, 2 ] and k = 1. Subtract 2^1 from both numbers. The subarray becomes [1, 1, 0].
 - Choose [ 1 , 1 , 0] and k = 0. Subtract 2^0 from both numbers. The subarray becomes [0, 0, 0].
- We can make all elements in the subarray [4,3,1,2,4] equal to 0 in the following way:
 - Choose [ 4 , 3, 1, 2, 4 ] and k = 2. Subtract 2^2 from both numbers. The subarray becomes [0, 3, 1, 2, 0].
 - Choose [0, 3 , 1 , 2, 0] and k = 0. Subtract 2^0 from both numbers. The subarray becomes [0, 2, 0, 2, 0].
 - Choose [0, 2 , 0, 2 , 0] and k = 1. Subtract 2^1 from both numbers. The subarray becomes [0, 0, 0, 0, 0].

### Example 2
- **Input:** `nums = [1,10,4]`
- **Output:** `0`
- **Explanation:** There are no beautiful subarrays in nums.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count the Number of Beautiful Subarrays**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [4,3,1,2,4]`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** There are 2 beautiful subarrays in nums: [4, 3,1,2 ,4] and [ 4,3,1,2,4 ].
- We can make all elements in the subarray [3,1,2] equal to 0 in the following way:
 - Choose [ 3 , 1, 2 ] and k = 1. Subtract 2^1 from both numbers. The subarray becomes [1, 1, 0].
 - Choose [ 1 , 1 , 0] and k = 0. Subtract 2^0 from both numbers. The subarray becomes [0, 0, 0].
- We can make all elements in the subarray [4,3,1,2,4] equal to 0 in the following way:
 - Choose [ 4 , 3, 1, 2, 4 ] and k = 2. Subtract 2^2 from both numbers. The subarray becomes [0, 3, 1, 2, 0].
 - Choose [0, 3 , 1 , 2, 0] and k = 0. Subtract 2^0 from both numbers. The subarray becomes [0, 2, 0, 2, 0].
 - Choose [0, 2 , 0, 2 , 0] and k = 1. Subtract 2^1 from both numbers. The subarray becomes [0, 0, 0, 0, 0].

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
class Solution(object):
    def beautifulSubarrays(self, nums):
        cnt = {0: 1}
        x = 0
        ans = 0
        for v in nums:
            x ^= v
            c = cnt.get(x, 0)
            ans += c
            cnt[x] = c + 1
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
- [1248. Count Number of Nice Subarrays](../../1001-1500/1370-count-number-of-nice-subarrays/)
- [2537. Count the Number of Good Subarrays](../../2501-3000/2626-count-the-number-of-good-subarrays/)
- [2970. Count the Number of Incremovable Subarrays I](../../3001-3500/3252-count-the-number-of-incremovable-subarrays-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-the-number-of-beautiful-subarrays/)
