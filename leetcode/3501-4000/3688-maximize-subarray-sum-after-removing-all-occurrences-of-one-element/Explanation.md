# LeetCode 3410: Maximize Subarray Sum After Removing All Occurrences of One Element

**LeetCode Problem #3410 — Maximize Subarray Sum After Removing All Occurrences of One Element**
Solve LeetCode Maximize Subarray Sum After Removing All Occurrences of One Element using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximize Subarray Sum After Removing All Occurrences of One Element |
| LeetCode | #3410 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums`.

You can do the following operation on the array **at most** once:

Choose **any** integer `x` such that `nums` remains **non-empty** on removing all occurrences of `x`. 
 Remove **all** occurrences of `x` from the array.

Return the **maximum** subarray sum across **all** possible resulting arrays.

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^6 <= nums[i] <= 10^6`

## Examples
### Example 1
- **Input:** `nums = [-3,2,-2,-1,3,-2,3]`
- **Output:** `7`
- **Explanation:** We can have the following arrays after at most one operation: 

 
 The original array is nums = [ -3, 2, -2, -1,

### Example 2
- **Input:** `nums = [1,2,3,4]`
- **Output:** `10`
- **Explanation:** It is optimal to not perform any operations.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Maximize Subarray Sum After Removing All Occurrences of One Element**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [-3,2,-2,-1,3,-2,3]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7`.
4. **Verification:** We can have the following arrays after at most one operation: 

 
 The original array is nums = [ -3, 2, -2, -1,

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
    def maxSubarraySum(self, nums: List[int]) -> int:
        mx = max(nums)
        if mx <= 0:
            return mx

        n = len(nums)
        size = 1
        while size < n:
            size *= 2

        tree = [(0, 0, 0, 0)] * (2 * size)

        def merge(a, b):
            return (
                a[0] + b[0],
                max(a[1], a[0] + b[1]),
                max(b[2], b[0] + a[2]),
                max(a[3], b[3], a[2] + b[1]),
            )

        for i, v in enumerate(nums):
            tree[size + i] = (v, v, v, v)
        for i in range(size - 1, 0, -1):
            tree[i] = merge(tree[2 * i], tree[2 * i + 1])

        def update(pos, v):
            i = size + pos
            tree[i] = (v, v, v, v)
            i >>= 1
            while i:
                tree[i] = merge(tree[2 * i], tree[2 * i + 1])
                i >>= 1

        positions = defaultdict(list)
        for i, v in enumerate(nums):
            if v < 0:
                positions[v].append(i)

        ans = tree[1][3]
        for x, idxs in positions.items():
            for p in idxs:
                update(p, 0)
            ans = max(ans, tree[1][3])
            for p in idxs:
                update(p, x)

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
- [3830. Longest Alternating Subarray After Removing At Most One Element](../../4001-4500/4198-longest-alternating-subarray-after-removing-at-most-one-element/)
- [1493. Longest Subarray of 1's After Deleting One Element](../../1501-2000/1586-longest-subarray-of-1s-after-deleting-one-element/)
- [3480. Maximize Subarrays After Removing One Conflicting Pair](../../3501-4000/3789-maximize-subarrays-after-removing-one-conflicting-pair/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximize-subarray-sum-after-removing-all-occurrences-of-one-element/)
