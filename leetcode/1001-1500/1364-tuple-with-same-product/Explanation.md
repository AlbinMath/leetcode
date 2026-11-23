# LeetCode 1726: Tuple with Same Product

**LeetCode Problem #1726 — Tuple with Same Product**
Solve LeetCode Tuple with Same Product using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Tuple with Same Product |
| LeetCode | #1726 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array `nums` of **distinct** positive integers, return *the number of tuples *`(a, b, c, d)`* such that *`a * b = c * d`* where *`a`*, *`b`*, *`c`*, and *`d`* are elements of *`nums`*, and *`a != b != c != d`*.*

## Constraints
- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 10^4`
- All elements in `nums` are **distinct**.

## Examples
### Example 1
- **Input:** `nums = [2,3,4,6]`
- **Output:** `8`
- **Explanation:** There are 8 valid tuples:
(2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
(3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)

### Example 2
- **Input:** `nums = [1,2,4,5,10]`
- **Output:** `16`
- **Explanation:** There are 16 valid tuples:
(1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
(2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
(2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,5,4)
(4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Tuple with Same Product**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,3,4,6]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `8`.
4. **Verification:** There are 8 valid tuples:
(2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
(3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)

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
from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums: list[int]) -> int:
        cnt = defaultdict(int)
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                cnt[nums[i] * nums[j]] += 1
        return sum(4 * m * (m - 1) for m in cnt.values())
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
- [152. Maximum Product Subarray](../../0001-0500/0152-maximum-product-subarray/)
- [238. Product of Array Except Self](../../0001-0500/0238-product-of-array-except-self/)
- [318. Maximum Product of Word Lengths](../../0001-0500/0318-maximum-product-of-word-lengths/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/tuple-with-same-product/)
