# LeetCode 3862: Find the Smallest Balanced Index

**LeetCode Problem #3862 — Find the Smallest Balanced Index**
Solve LeetCode Find the Smallest Balanced Index using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Smallest Balanced Index |
| LeetCode | #3862 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`.

An index `i` is **balanced** if the sum of elements **strictly** to the left of `i` equals the product of elements **strictly** to the right of `i`.

If there are no elements to the left, the sum is considered as 0. Similarly, if there are no elements to the right, the product is considered as 1.

Return an integer denoting the **smallest** balanced index. If no balanced index exists, return -1.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [2,1,2]`
- **Output:** `1`
- **Explanation:** For index `i = 1`: 

 
 Left sum = `nums[0] = 2` 
 Right product = `nums[2] = 2` 
 Since the left sum equals the right product, index 1 is balanced. 
 

 No smaller index satisfies the condition, so the answer is 1.

### Example 2
- **Input:** `nums = [2,8,2,2,5]`
- **Output:** `2`
- **Explanation:** For index `i = 2`: 

 
 Left sum = `2 + 8 = 10` 
 Right product = `2 * 5 = 10` 
 Since the left sum equals the right product, index 2 is balanced. 
 

 No smaller index satisfies the condition, so the answer is 2.

### Example 3
- **Input:** `nums = [1]`
- **Output:** `-1`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find the Smallest Balanced Index**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,1,2]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** For index `i = 1`: 

 
 Left sum = `nums[0] = 2` 
 Right product = `nums[2] = 2` 
 Since the left sum equals the right product, index 1 is balanced. 
 

 No smaller index satisfies the condition, so the answer is 1.

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
from typing import List

class Solution:
    def smallestBalancedIndex(self, nums: List[int]) -> int:
        n = len(nums)
        CAP = 10**15  
        prod = [1] * n
        for i in range(n - 2, -1, -1):
            prod[i] = min(CAP, prod[i + 1] * nums[i + 1])

        left = 0
        for i in range(n):
            if left == prod[i]:
                return i
            left += nums[i]
        return -1
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
- [28. Find the Index of the First Occurrence in a String](../../0001-0500/0028-find-the-index-of-the-first-occurrence-in-a-string/)
- [373. Find K Pairs with Smallest Sums](../../0001-0500/0373-find-k-pairs-with-smallest-sums/)
- [719. Find K-th Smallest Pair Distance](../../0501-1000/0719-find-k-th-smallest-pair-distance/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-smallest-balanced-index/)
