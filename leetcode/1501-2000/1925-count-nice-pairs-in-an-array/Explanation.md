# LeetCode 1814: Count Nice Pairs in an Array

**LeetCode Problem #1814 — Count Nice Pairs in an Array**
Solve LeetCode Count Nice Pairs in an Array using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Nice Pairs in an Array |
| LeetCode | #1814 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array `nums` that consists of non-negative integers. Let us define `rev(x)` as the reverse of the non-negative integer `x`. For example, `rev(123) = 321`, and `rev(120) = 21`. A pair of indices `(i, j)` is **nice** if it satisfies all of the following conditions:

`0 <= i < j < nums.length` 
 `nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])`

Return *the number of nice pairs of indices*. Since that number can be too large, return it **modulo** `10^9 + 7`.

## Constraints
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [42,11,1,97]`
- **Output:** `2`
- **Explanation:** The two pairs are:
 - (0,3) : 42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121.
 - (1,2) : 11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12.

### Example 2
- **Input:** `nums = [13,10,35,24,76]`
- **Output:** `4`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Nice Pairs in an Array**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [42,11,1,97]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The two pairs are:
 - (0,3) : 42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121.
 - (1,2) : 11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12.

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
    def countNicePairs(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        freq = {}
        nice_pairs = 0
        
        def rev(x: int) -> int:
            res = 0
            while x > 0:
                res = res * 10 + x % 10
                x //= 10
            return res
        
        for num in nums:
            diff = num - rev(num)
            count = freq.get(diff, 0)
            
            nice_pairs = (nice_pairs + count) % MOD
            freq[diff] = count + 1
            
        return nice_pairs
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
- [2183. Count Array Pairs Divisible by K](../../2001-2500/2301-count-array-pairs-divisible-by-k/)
- [1248. Count Number of Nice Subarrays](../../1001-1500/1370-count-number-of-nice-subarrays/)
- [1735. Count Ways to Make Array With Product](../../1501-2000/1836-count-ways-to-make-array-with-product/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-nice-pairs-in-an-array/)
