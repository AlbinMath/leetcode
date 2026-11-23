# LeetCode 3880: Minimum Absolute Difference Between Two Values

**LeetCode Problem #3880 — Minimum Absolute Difference Between Two Values**
Solve LeetCode Minimum Absolute Difference Between Two Values using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Absolute Difference Between Two Values |
| LeetCode | #3880 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` consisting only of 0, 1, and 2.

A pair of indices `(i, j)` is called **valid** if `nums[i] == 1` and `nums[j] == 2`.

Return the **minimum** absolute difference between `i` and `j` among all valid pairs. If no valid pair exists, return -1.

The absolute difference between indices `i` and `j` is defined as `abs(i - j)`.

## Constraints
- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 2`

## Examples
### Example 1
- **Input:** `nums = [1,0,0,2,0,1]`
- **Output:** `2`
- **Explanation:** The valid pairs are: 

 
 (0, 3) which has absolute difference of `abs(0 - 3) = 3`. 
 (5, 3) which has absolute difference of `abs(5 - 3) = 2`. 
 

 Thus, the answer is 2.

### Example 2
- **Input:** `nums = [1,0,1,0]`
- **Output:** `-1`
- **Explanation:** There are no valid pairs in the array, thus the answer is -1.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Absolute Difference Between Two Values**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,0,0,2,0,1]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The valid pairs are: 

 
 (0, 3) which has absolute difference of `abs(0 - 3) = 3`. 
 (5, 3) which has absolute difference of `abs(5 - 3) = 2`. 
 

 Thus, the answer is 2.

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
    def minAbsoluteDifference(self, nums: List[int]) -> int:
        last1 = last2 = -1
        ans = float('inf')
        for i, v in enumerate(nums):
            if v == 1:
                last1 = i
                if last2 != -1:
                    ans = min(ans, i - last2)
            elif v == 2:
                last2 = i
                if last1 != -1:
                    ans = min(ans, i - last1)
        return -1 if ans == float('inf') else ans
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
- [530. Minimum Absolute Difference in BST](../../0501-1000/0530-minimum-absolute-difference-in-bst/)
- [1200. Minimum Absolute Difference](../../1001-1500/1306-minimum-absolute-difference/)
- [1984. Minimum Difference Between Highest and Lowest of K Scores](../../2001-2500/2112-minimum-difference-between-highest-and-lowest-of-k-scores/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-absolute-difference-between-two-values/)
