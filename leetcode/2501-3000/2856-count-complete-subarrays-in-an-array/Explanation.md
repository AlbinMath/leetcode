# LeetCode 2799: Count Complete Subarrays in an Array

**LeetCode Problem #2799 — Count Complete Subarrays in an Array**
Solve LeetCode Count Complete Subarrays in an Array using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Complete Subarrays in an Array |
| LeetCode | #2799 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an array `nums` consisting of **positive** integers.

We call a subarray of an array **complete** if the following condition is satisfied:

The number of **distinct** elements in the subarray is equal to the number of distinct elements in the whole array.

Return *the number of **complete** subarrays*.

A **subarray** is a contiguous non-empty part of an array.

## Constraints
- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 2000`

## Examples
### Example 1
- **Input:** `nums = [1,3,1,2,2]`
- **Output:** `4`
- **Explanation:** The complete subarrays are the following: [1,3,1,2], [1,3,1,2,2], [3,1,2] and [3,1,2,2].

### Example 2
- **Input:** `nums = [5,5,5,5]`
- **Output:** `10`
- **Explanation:** The array consists only of the integer 5, so any subarray is complete. The number of subarrays that we can choose is 10.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Count Complete Subarrays in an Array**, we observe the problem requirements and utilize the **Tree & Graph** technique. By maintaining a **Tree / Graph / Grid**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Tree / Graph / Grid** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,3,1,2,2]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The complete subarrays are the following: [1,3,1,2], [1,3,1,2,2], [3,1,2] and [3,1,2,2].

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
from collections import defaultdict

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        D = len(set(nums))
        cnt = defaultdict(int)
        distinct = 0
        l = 0
        ans = 0
        for x in nums:
            if cnt[x] == 0:
                distinct += 1
            cnt[x] += 1
            while distinct == D:
                y = nums[l]
                cnt[y] -= 1
                if cnt[y] == 0:
                    distinct -= 1
                l += 1
            ans += l
        return ans
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
- [1526. Minimum Number of Increments on Subarrays to Form a Target Array](../../1501-2000/1633-minimum-number-of-increments-on-subarrays-to-form-a-target-array/)
- [1735. Count Ways to Make Array With Product](../../1501-2000/1836-count-ways-to-make-array-with-product/)
- [2179. Count Good Triplets in an Array](../../2001-2500/2280-count-good-triplets-in-an-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-complete-subarrays-in-an-array/)
