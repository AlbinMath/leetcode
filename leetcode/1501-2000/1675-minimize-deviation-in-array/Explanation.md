# LeetCode 1675: Minimize Deviation in Array

**LeetCode Problem #1675 — Minimize Deviation in Array**
Solve LeetCode Minimize Deviation in Array using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimize Deviation in Array |
| LeetCode | #1675 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array `nums` of `n` positive integers.

You can perform two types of operations on any element of the array any number of times:

If the element is **even**, **divide** it by `2`.

For example, if the array is `[1,2,3,4]`, then you can do this operation on the last element, and the array will be `[1,2,3, 2 ].` 
 
 
 If the element is **odd**, **multiply** it by `2`.
 
 For example, if the array is `[1,2,3,4]`, then you can do this operation on the first element, and the array will be `[ 2 ,2,3,4].`

The **deviation** of the array is the **maximum difference** between any two elements in the array.

Return *the **minimum deviation** the array can have after performing some number of operations.*

## Constraints
- `n == nums.length`
- `2 <= n <= 5 * 10^ 4 `
- `1 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [1,2,3,4]`
- **Output:** `1`
- **Explanation:** You can transform the array to [1,2,3, 2 ], then to [ 2 ,2,3,2], then the deviation will be 3 - 2 = 1.

### Example 2
- **Input:** `nums = [4,1,5,20,3]`
- **Output:** `3`
- **Explanation:** You can transform the array after two operations to [4, 2 ,5, 5 ,3], then the deviation will be 5 - 2 = 3.

### Example 3
- **Input:** `nums = [2,10,8]`
- **Output:** `3`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimize Deviation in Array**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,4]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** You can transform the array to [1,2,3, 2 ], then to [ 2 ,2,3,2], then the deviation will be 3 - 2 = 1.

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
import heapq
from typing import List

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap = []
        min_val = float('inf')
        for x in nums:
            if x % 2 == 1:
                x *= 2
            heap.append(-x)  # max-heap via negation
            min_val = min(min_val, x)
        heapq.heapify(heap)

        ans = float('inf')
        while True:
            m = -heapq.heappop(heap)
            ans = min(ans, m - min_val)
            if m % 2 == 1:
                break
            half = m // 2
            min_val = min(min_val, half)
            heapq.heappush(heap, -half)
        return ans
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
- [1877. Minimize Maximum Pair Sum in Array](../../1501-2000/1877-minimize-maximum-pair-sum-in-array/)
- [2035. Partition Array Into Two Arrays to Minimize Sum Difference](../../2001-2500/2035-partition-array-into-two-arrays-to-minimize-sum-difference/)
- [2439. Minimize Maximum of Array](../../2001-2500/2439-minimize-maximum-of-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimize-deviation-in-array/)
