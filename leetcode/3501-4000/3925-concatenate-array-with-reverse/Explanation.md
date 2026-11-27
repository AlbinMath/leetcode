# LeetCode 3925: Concatenate Array With Reverse

**LeetCode Problem #3925 — Concatenate Array With Reverse**
Solve LeetCode Concatenate Array With Reverse using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Concatenate Array With Reverse |
| LeetCode | #3925 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
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
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Concatenate Array With Reverse**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
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
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

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
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [1330. Reverse Subarray To Maximize Array Value](../../1001-1500/1330-reverse-subarray-to-maximize-array-value/)
- [7. Reverse Integer](../../0001-0500/0007-reverse-integer/)
- [25. Reverse Nodes in k-Group](../../0001-0500/0025-reverse-nodes-in-k-group/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/concatenate-array-with-reverse/)
