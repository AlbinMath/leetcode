# LeetCode 2826: Sorting Three Groups

**LeetCode Problem #2826 — Sorting Three Groups**
Solve LeetCode Sorting Three Groups using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sorting Three Groups |
| LeetCode | #2826 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`. Each element in `nums` is 1, 2 or 3. In each operation, you can remove an element from `nums`. Return the **minimum** number of operations to make `nums` **non-decreasing**.

## Constraints
- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 3`

## Examples
### Example 1
- **Input:** `nums = [2,1,3,2,1]`
- **Output:** `3`
- **Explanation:** One of the optimal solutions is to remove `nums[0]`, `nums[2]` and `nums[3]`.

### Example 2
- **Input:** `nums = [1,3,2,1,3,3]`
- **Output:** `2`
- **Explanation:** One of the optimal solutions is to remove `nums[1]` and `nums[2]`.

### Example 3
- **Input:** `nums = [2,2,2,2,3,3]`
- **Output:** `0`
- **Explanation:** `nums` is already non-decreasing.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Sorting Three Groups**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,1,3,2,1]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** One of the optimal solutions is to remove `nums[0]`, `nums[2]` and `nums[3]`.

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
from bisect import bisect_right

class Solution:
    def minimumOperations(self, nums):
        tails = []
        for x in nums:
            pos = bisect_right(tails, x)
            if pos == len(tails):
                tails.append(x)
            else:
                tails[pos] = x
        return len(nums) - len(tails)
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
- [1859. Sorting the Sentence](../../1501-2000/1859-sorting-the-sentence/)
- [2089. Find Target Indices After Sorting Array](../../2001-2500/2089-find-target-indices-after-sorting-array/)
- [185. Department Top Three Salaries](../../0001-0500/0185-department-top-three-salaries/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sorting-three-groups/)
