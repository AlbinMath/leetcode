# LeetCode 3371: Identify the Largest Outlier in an Array

**LeetCode Problem #3371 — Identify the Largest Outlier in an Array**
Solve LeetCode Identify the Largest Outlier in an Array using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Identify the Largest Outlier in an Array |
| LeetCode | #3371 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums`. This array contains `n` elements, where **exactly** `n - 2` elements are **special**** numbers**. One of the remaining **two** elements is the *sum* of these **special numbers**, and the other is an **outlier**.

An **outlier** is defined as a number that is *neither* one of the original special numbers *nor* the element representing the sum of those numbers.

**Note** that special numbers, the sum element, and the outlier must have **distinct** indices, but *may *share the **same** value.

Return the **largest**** **potential** outlier** in `nums`.

## Constraints
- `3 <= nums.length <= 10^5`
- `-1000 <= nums[i] <= 1000`
- The input is generated such that at least **one** potential outlier exists in `nums`.

## Examples
### Example 1
- **Input:** `nums = [2,3,5,10]`
- **Output:** `10`
- **Explanation:** The special numbers could be 2 and 3, thus making their sum 5 and the outlier 10.

### Example 2
- **Input:** `nums = [-2,-1,-3,-6,4]`
- **Output:** `4`
- **Explanation:** The special numbers could be -2, -1, and -3, thus making their sum -6 and the outlier 4.

### Example 3
- **Input:** `nums = [1,1,1,1,1,5,5]`
- **Output:** `5`
- **Explanation:** The special numbers could be 1, 1, 1, 1, and 1, thus making their sum 5 and the other 5 as the outlier.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Identify the Largest Outlier in an Array**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,3,5,10]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `10`.
4. **Verification:** The special numbers could be 2 and 3, thus making their sum 5 and the outlier 10.

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
    def getLargestOutlier(self, nums: List[int]) -> int:
        S = sum(nums)
        cnt = Counter(nums)
        ans = float('-inf')

        for s in cnt:
            o = S - 2 * s
            if o in cnt and (o != s or cnt[s] >= 2):
                ans = max(ans, o)

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
- [215. Kth Largest Element in an Array](../../0001-0500/0215-kth-largest-element-in-an-array/)
- [410. Split Array Largest Sum](../../0001-0500/0410-split-array-largest-sum/)
- [1985. Find the Kth Largest Integer in the Array](../../2001-2500/2113-find-the-kth-largest-integer-in-the-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/identify-the-largest-outlier-in-an-array/)
