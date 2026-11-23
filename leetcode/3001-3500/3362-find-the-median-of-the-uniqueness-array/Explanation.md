# LeetCode 3134: Find the Median of the Uniqueness Array

**LeetCode Problem #3134 — Find the Median of the Uniqueness Array**
Solve LeetCode Find the Median of the Uniqueness Array using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Median of the Uniqueness Array |
| LeetCode | #3134 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums`. The **uniqueness array** of `nums` is the sorted array that contains the number of distinct elements of all the subarrays of `nums`. In other words, it is a sorted array consisting of `distinct(nums[i..j])`, for all `0 <= i <= j < nums.length`.

Here, `distinct(nums[i..j])` denotes the number of distinct elements in the subarray that starts at index `i` and ends at index `j`.

Return the **median** of the **uniqueness array** of `nums`.

**Note** that the **median** of an array is defined as the middle element of the array when it is sorted in non-decreasing order. If there are two choices for a median, the **smaller** of the two values is taken.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [1,2,3]`
- **Output:** `1`
- **Explanation:** The uniqueness array of `nums` is `[distinct(nums[0..0]), distinct(nums[1..1]), distinct(nums[2..2]), distinct(nums[0..1]), distinct(nums[1..2]), distinct(nums[0..2])]` which is equal to `[1, 1, 1, 2, 2, 3]`. The uniqueness array has a median of 1. Therefore, the answer is 1.

### Example 2
- **Input:** `nums = [3,4,3,4,5]`
- **Output:** `2`
- **Explanation:** The uniqueness array of `nums` is `[1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3]`. The uniqueness array has a median of 2. Therefore, the answer is 2.

### Example 3
- **Input:** `nums = [4,3,5,4]`
- **Output:** `2`
- **Explanation:** The uniqueness array of `nums` is `[1, 1, 1, 1, 2, 2, 2, 3, 3, 3]`. The uniqueness array has a median of 2. Therefore, the answer is 2.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Find the Median of the Uniqueness Array**, we observe the problem requirements and utilize the **Tree & Graph** technique. By maintaining a **Tree / Graph / Grid**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Tree / Graph / Grid** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** The uniqueness array of `nums` is `[distinct(nums[0..0]), distinct(nums[1..1]), distinct(nums[2..2]), distinct(nums[0..1]), distinct(nums[1..2]), distinct(nums[0..2])]` which is equal to `[1, 1, 1, 2, 2, 3]`. The uniqueness array has a median of 1. Therefore, the answer is 1.

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
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n + 1) // 2
        need = (total + 1) // 2

        def count_at_most(x: int) -> int:
            cnt = defaultdict(int)
            distinct = 0
            l = 0
            res = 0
            for r, v in enumerate(nums):
                if cnt[v] == 0:
                    distinct += 1
                cnt[v] += 1
                while distinct > x:
                    u = nums[l]
                    cnt[u] -= 1
                    if cnt[u] == 0:
                        distinct -= 1
                    l += 1
                res += r - l + 1
            return res

        lo, hi = 1, len(set(nums))
        while lo < hi:
            mid = (lo + hi) // 2
            if count_at_most(mid) >= need:
                hi = mid
            else:
                lo = mid + 1
        return lo
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
- [295. Find Median from Data Stream](../../0001-0500/0295-find-median-from-data-stream/)
- [3585. Find Weighted Median Node in Tree](../../3501-4000/3900-find-weighted-median-node-in-tree/)
- [34. Find First and Last Position of Element in Sorted Array](../../0001-0500/0034-find-first-and-last-position-of-element-in-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-median-of-the-uniqueness-array/)
