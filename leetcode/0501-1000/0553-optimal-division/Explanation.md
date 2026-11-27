# LeetCode 553: Optimal Division

**LeetCode Problem #553 — Optimal Division**
Solve LeetCode Optimal Division using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Optimal Division |
| LeetCode | #553 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`. The adjacent integers in `nums` will perform the float division.

For example, for `nums = [2,3,4]`, we will evaluate the expression `"2/3/4"`.

However, you can add any number of parenthesis at any position to change the priority of operations. You want to add these parentheses such the value of the expression after the evaluation is maximum.

Return *the corresponding expression that has the maximum value in string format*.

**Note:** your expression should not contain redundant parenthesis.

## Constraints
- `1 <= nums.length <= 10`
- `2 <= nums[i] <= 1000`
- There is only one optimal division for the given input.

## Examples
### Example 1
- **Input:** `nums = [1000,100,10,2]`
- **Output:** `"1000/(100/10/2)"`
- **Explanation:** 1000/(100/10/2) = 1000/((100/10)/2) = 200
However, the bold parenthesis in "1000/(

### Example 2
- **Input:** `nums = [2,3,4]`
- **Output:** `"2/(3/4)"`
- **Explanation:** (2/(3/4)) = 8/3 = 2.667
It can be shown that after trying all possibilities, we cannot get an expression with evaluation greater than 2.667

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Optimal Division**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1000,100,10,2]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"1000/(100/10/2)"`.
4. **Verification:** 1000/(100/10/2) = 1000/((100/10)/2) = 200
However, the bold parenthesis in "1000/(

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
    def optimalDivision(self, nums: List[int]) -> str:
        n = len(nums)
        if n == 1:
            return str(nums[0])
        if n == 2:
            return f"{nums[0]}/{nums[1]}"
        tail = '/'.join(map(str, nums[1:]))
        return f"{nums[0]}/({tail})"
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
- [2405. Optimal Partition of String](../../2001-2500/2405-optimal-partition-of-string/)
- [3645. Maximum Total from Optimal Activation Order](../../3501-4000/3645-maximum-total-from-optimal-activation-order/)
- [399. Evaluate Division](../../0001-0500/0399-evaluate-division/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/optimal-division/)
