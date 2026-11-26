# LeetCode 3152: Special Array II

**LeetCode Problem #3152 — Special Array II**
Solve LeetCode Special Array II using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Special Array II |
| LeetCode | #3152 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
An array is considered **special** if every pair of its adjacent elements contains two numbers with different parity.

You are given an array of integer `nums` and a 2D integer matrix `queries`, where for `queries[i] = [from_i, to_i]` your task is to check that subarray `nums[from_i..to_i]` is **special** or not.

Return an array of booleans `answer` such that `answer[i]` is `true` if `nums[from_i..to_i]` is special.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`
- `1 <= queries.length <= 10^5`
- `queries[i].length == 2`
- `0 <= queries[i][0] <= queries[i][1] <= nums.length - 1`

## Examples
### Example 1
- **Input:** `nums = [3,4,1,2,6], queries = [[0,4]]`
- **Output:** `[false]`
- **Explanation:** The subarray is `[3,4,1,2,6]`. 2 and 6 are both even.

### Example 2
- **Input:** `nums = [4,3,1,6], queries = [[0,2],[2,3]]`
- **Output:** `[false,true]`
- **Explanation:** The subarray is `[4,3,1]`. 3 and 1 are both odd. So the answer to this query is `false`. 
 The subarray is `[1,6]`. There is only one pair: `(1,6)` and it contains numbers with different parity. So the answer to this query is `true`.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Special Array II**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,4,1,2,6], queries = [[0,4]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[false]`.
4. **Verification:** The subarray is `[3,4,1,2,6]`. 2 and 6 are both even.

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
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        pre = [0] * n
        for i in range(1, n):
            pre[i] = pre[i - 1] + (nums[i - 1] % 2 == nums[i] % 2)

        return [pre[r] - pre[l] == 0 for l, r in queries]
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
- [1608. Special Array With X Elements Greater Than or Equal X](../../1501-2000/1608-special-array-with-x-elements-greater-than-or-equal-x/)
- [761. Special Binary String](../../0501-1000/0761-special-binary-string/)
- [893. Groups of Special-Equivalent Strings](../../0501-1000/0893-groups-of-special-equivalent-strings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/special-array-ii/)
