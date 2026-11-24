# LeetCode 3925: Concatenate Array With Reverse

**LeetCode Problem #3925 — Concatenate Array With Reverse**
Solve LeetCode Concatenate Array With Reverse using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Concatenate Array With Reverse |
| LeetCode | #3925 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` of length `n`.

Construct a new array `ans` of length `2 * n` such that the first `n` elements are the same as `nums`, and the next `n` elements are the elements of `nums` in reverse order.

Formally, for `0 <= i <= n - 1`:

`ans[i] = nums[i]` 
 `ans[i + n] = nums[n - i - 1]`

Return an integer array `ans`.

## Constraints
- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`

## Examples
### Example 1
- **Input:** `nums = [1,2,3]`
- **Output:** `[1,2,3,3,2,1]`
- **Explanation:** The first `n` elements of `ans` are the same as `nums`. 

 For the next `n = 3` elements, each element is taken from `nums` in reverse order: 

 
 `ans[3] = nums[2] = 3` 
 `ans[4] = nums[1] = 2` 
 `ans[5] = nums[0] = 1` 
 

 Thus, `ans = [1, 2, 3, 3, 2, 1]`.

### Example 2
- **Input:** `nums = [1]`
- **Output:** `[1,1]`
- **Explanation:** The array remains the same when reversed. Thus, `ans = [1, 1]`.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Concatenate Array With Reverse**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,2,3,3,2,1]`.
4. **Verification:** The first `n` elements of `ans` are the same as `nums`. 

 For the next `n = 3` elements, each element is taken from `nums` in reverse order: 

 
 `ans[3] = nums[2] = 3` 
 `ans[4] = nums[1] = 2` 
 `ans[5] = nums[0] = 1` 
 

 Thus, `ans = [1, 2, 3, 3, 2, 1]`.

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
class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        return nums + nums[::-1]
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
- [7. Reverse Integer](../../0001-0500/0007-reverse-integer/)
- [25. Reverse Nodes in k-Group](../../0001-0500/0025-reverse-nodes-in-k-group/)
- [92. Reverse Linked List II](../../0001-0500/0092-reverse-linked-list-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/concatenate-array-with-reverse/)
