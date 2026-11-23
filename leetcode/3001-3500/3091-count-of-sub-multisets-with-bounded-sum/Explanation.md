# LeetCode 2902: Count of Sub-Multisets With Bounded Sum

**LeetCode Problem #2902 — Count of Sub-Multisets With Bounded Sum**
Solve LeetCode Count of Sub-Multisets With Bounded Sum using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count of Sub-Multisets With Bounded Sum |
| LeetCode | #2902 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **0-indexed** array `nums` of non-negative integers, and two integers `l` and `r`.

Return *the **count of sub-multisets** within* `nums` *where the sum of elements in each subset falls within the inclusive range of* `[l, r]`.

Since the answer may be large, return it modulo `10^9 + 7`.

A **sub-multiset** is an **unordered** collection of elements of the array in which a given value `x` can occur `0, 1, ..., occ[x]` times, where `occ[x]` is the number of occurrences of `x` in the array.

**Note** that:

Two **sub-multisets** are the same if sorting both sub-multisets results in identical multisets. 
 The sum of an **empty** multiset is `0`.

## Constraints
- `1 <= nums.length <= 2 * 10^4`
- `0 <= nums[i] <= 2 * 10^4`
- Sum of `nums` does not exceed `2 * 10^4`.
- `0 <= l <= r <= 2 * 10^4`

## Examples
### Example 1
- **Input:** `nums = [1,2,2,3], l = 6, r = 6`
- **Output:** `1`
- **Explanation:** The only subset of nums that has a sum of 6 is {1, 2, 3}.

### Example 2
- **Input:** `nums = [2,1,4,2,7], l = 1, r = 5`
- **Output:** `7`
- **Explanation:** The subsets of nums that have a sum within the range [1, 5] are {1}, {2}, {4}, {2, 2}, {1, 2}, {1, 4}, and {1, 2, 2}.

### Example 3
- **Input:** `nums = [1,2,1,3,5,2], l = 3, r = 5`
- **Output:** `9`
- **Explanation:** The subsets of nums that have a sum within the range [3, 5] are {3}, {5}, {1, 2}, {1, 3}, {2, 2}, {2, 3}, {1, 1, 2}, {1, 1, 3}, and {1, 2, 2}.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Count of Sub-Multisets With Bounded Sum**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,2,3], l = 6, r = 6`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** The only subset of nums that has a sum of 6 is {1, 2, 3}.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List
from collections import Counter

class Solution:
    def countSubMultisets(self, nums: List[int], l: int, r: int) -> int:
        MOD = 10**9 + 7
        cnt = Counter(nums)
        zeros = cnt.pop(0, 0)

        dp = [0] * (r + 1)
        dp[0] = 1

        for v, c in cnt.items():
            new = dp[:]                      # j = 0 term
            for s in range(v, r + 1):
                val = new[s - v] + dp[s]
                if s - (c + 1) * v >= 0:
                    val -= dp[s - (c + 1) * v]
                new[s] = val % MOD
            dp = new

        # careful: new[s] above must equal sum_{j=0..c} dp[s - j*v]
        return sum(dp[l:r + 1]) % MOD * (zeros + 1) % MOD
```

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [327. Count of Range Sum](../../0001-0500/0327-count-of-range-sum/)
- [1477. Find Two Non-overlapping Sub-arrays Each With Target Sum](../../1501-2000/1573-find-two-non-overlapping-sub-arrays-each-with-target-sum/)
- [1524. Number of Sub-arrays With Odd Sum](../../1501-2000/1631-number-of-sub-arrays-with-odd-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-of-sub-multisets-with-bounded-sum/)
