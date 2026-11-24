# LeetCode 3736: Minimum Moves to Equal Array Elements III

**LeetCode Problem #3736 — Minimum Moves to Equal Array Elements III**
Solve LeetCode Minimum Moves to Equal Array Elements III using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Moves to Equal Array Elements III |
| LeetCode | #3736 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`.

In one move, you may **increase** the value of any single element `nums[i]` by 1.

Return the **minimum total** number of **moves** required so that all elements in `nums` become **equal**.

## Constraints
- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`

## Examples
### Example 1
- **Input:** `nums = [2,1,3]`
- **Output:** `3`
- **Explanation:** To make all elements equal: 

 
 Increase `nums[0] = 2` by 1 to make it 3. 
 Increase `nums[1] = 1` by 1 to make it 2. 
 Increase the updated `nums[1] = 2` by 1 to make it 3. 
 

 Now, all elements of `nums` are equal to 3. The minimum total moves is 3.

### Example 2
- **Input:** `nums = [4,4,5]`
- **Output:** `2`
- **Explanation:** To make all elements equal: 

 
 Increase `nums[0] = 4` by 1 to make it 5. 
 Increase `nums[1] = 4` by 1 to make it 5. 
 

 Now, all elements of `nums` are equal to 5. The minimum total moves is 2.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Moves to Equal Array Elements III**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,1,3]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** To make all elements equal: 

 
 Increase `nums[0] = 2` by 1 to make it 3. 
 Increase `nums[1] = 1` by 1 to make it 2. 
 Increase the updated `nums[1] = 2` by 1 to make it 3. 
 

 Now, all elements of `nums` are equal to 3. The minimum total moves is 3.

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
    def minMoves(self, nums: List[int]) -> int:
        return len(nums) * max(nums) - sum(nums)
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
- [453. Minimum Moves to Equal Array Elements](../../0001-0500/0453-minimum-moves-to-equal-array-elements/)
- [462. Minimum Moves to Equal Array Elements II](../../0001-0500/0462-minimum-moves-to-equal-array-elements-ii/)
- [2602. Minimum Operations to Make All Array Elements Equal](../../2501-3000/2602-minimum-operations-to-make-all-array-elements-equal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/)
