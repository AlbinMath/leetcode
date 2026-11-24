# LeetCode 3834: Merge Adjacent Equal Elements

**LeetCode Problem #3834 — Merge Adjacent Equal Elements**
Solve LeetCode Merge Adjacent Equal Elements using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Merge Adjacent Equal Elements |
| LeetCode | #3834 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`.

You must **repeatedly** apply the following merge operation until no more changes can be made:

If any **two adjacent elements are equal**, choose the **leftmost** such adjacent pair in the current array and replace them with a single element equal to their **sum**.

After each merge operation, the array size **decreases** by 1. Repeat the process on the updated array until no more changes can be made.

Return the final array after all possible merge operations.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`​​​​​​​

## Examples
### Example 1
- **Input:** `nums = [3,1,1,2]`
- **Output:** `[3,4]`
- **Explanation:** The middle two elements are equal and merged into `1 + 1 = 2`, resulting in `[3, 2, 2]`. 
 The last two elements are equal and merged into `2 + 2 = 4`, resulting in `[3, 4]`. 
 No adjacent equal elements remain. Thus, the answer is `[3, 4]`.

### Example 2
- **Input:** `nums = [2,2,4]`
- **Output:** `[8]`
- **Explanation:** The first two elements are equal and merged into `2 + 2 = 4`, resulting in `[4, 4]`. 
 The first two elements are equal and merged into `4 + 4 = 8`, resulting in `[8]`.

### Example 3
- **Input:** `nums = [3,7,5]`
- **Output:** `[3,7,5]`
- **Explanation:** There are no adjacent equal elements in the array, so no operations are performed.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Merge Adjacent Equal Elements**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,1,1,2]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[3,4]`.
4. **Verification:** The middle two elements are equal and merged into `1 + 1 = 2`, resulting in `[3, 2, 2]`. 
 The last two elements are equal and merged into `2 + 2 = 4`, resulting in `[3, 4]`. 
 No adjacent equal elements remain. Thus, the answer is `[3, 4]`.

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
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        stk = []
        
        for x in nums:
            curr = x
            while stk and stk[-1] == curr:
                curr += stk.pop()
            stk.append(curr)
            
        return stk
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
- [3165. Maximum Sum of Subsequence With Non-adjacent Elements](../../3001-3500/3423-maximum-sum-of-subsequence-with-non-adjacent-elements/)
- [3405. Count the Number of Arrays with K Matching Adjacent Elements](../../3501-4000/3682-count-the-number-of-arrays-with-k-matching-adjacent-elements/)
- [4043. Count Rotations With Exactly K Equal Adjacent Pairs](../../4001-4500/4411-count-rotations-with-exactly-k-equal-adjacent-pairs/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/merge-adjacent-equal-elements/)
