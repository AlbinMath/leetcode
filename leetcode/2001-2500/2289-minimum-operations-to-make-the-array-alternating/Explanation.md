# LeetCode 2170: Minimum Operations to Make the Array Alternating

**LeetCode Problem #2170 — Minimum Operations to Make the Array Alternating**
Solve LeetCode Minimum Operations to Make the Array Alternating using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Operations to Make the Array Alternating |
| LeetCode | #2170 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** array `nums` consisting of `n` positive integers.

The array `nums` is called **alternating** if:

`nums[i - 2] == nums[i]`, where `2 <= i <= n - 1`. 
 `nums[i - 1] != nums[i]`, where `1 <= i <= n - 1`.

In one **operation**, you can choose an index `i` and **change** `nums[i]` into **any** positive integer.

Return *the **minimum number of operations** required to make the array alternating*.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [3,1,3,2,4,3]`
- **Output:** `3`
- **Explanation:** One way to make the array alternating is by converting it to [3,1,3,

### Example 2
- **Input:** `nums = [1,2,2,2,2]`
- **Output:** `2`
- **Explanation:** One way to make the array alternating is by converting it to [1,2,

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Operations to Make the Array Alternating**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,1,3,2,4,3]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** One way to make the array alternating is by converting it to [3,1,3,

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
from collections import Counter

class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
            
        even_counts = Counter(nums[0::2])
        odd_counts = Counter(nums[1::2])
        
        # Get top 2 (value, frequency) pairs, padded with (0, 0) for safety
        top_even = even_counts.most_common(2) + [(0, 0), (0, 0)]
        top_odd = odd_counts.most_common(2) + [(0, 0), (0, 0)]
        
        (e_val1, e_cnt1), (_, e_cnt2) = top_even[0], top_even[1]
        (o_val1, o_cnt1), (_, o_cnt2) = top_odd[0], top_odd[1]
        
        if e_val1 != o_val1:
            max_kept = e_cnt1 + o_cnt1
        else:
            max_kept = max(e_cnt1 + o_cnt2, e_cnt2 + o_cnt1)
            
        return n - max_kept
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
- [3937. Minimum Operations to Make Array Modulo Alternating I](../../4001-4500/4300-minimum-operations-to-make-array-modulo-alternating-i/)
- [1827. Minimum Operations to Make the Array Increasing](../../1501-2000/1938-minimum-operations-to-make-the-array-increasing/)
- [2009. Minimum Number of Operations to Make Array Continuous](../../2001-2500/2119-minimum-number-of-operations-to-make-array-continuous/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-operations-to-make-the-array-alternating/)
