# LeetCode 1186: Maximum Subarray Sum with One Deletion

**LeetCode Problem #1186 — Maximum Subarray Sum with One Deletion**
Solve LeetCode Maximum Subarray Sum with One Deletion using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Subarray Sum with One Deletion |
| LeetCode | #1186 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array of integers, return the maximum sum for a **non-empty** subarray (contiguous elements) with at most one element deletion. In other words, you want to choose a subarray and optionally delete one element from it so that there is still at least one element left and the sum of the remaining elements is maximum possible.

Note that the subarray needs to be **non-empty** after deleting one element.

## Constraints
- `1 <= arr.length <= 10^5`
- `-10^4 <= arr[i] <= 10^4`

## Examples
### Example 1
- **Input:** `arr = [1,-2,0,3]`
- **Output:** `4`
- **Explanation:** Because we can choose [1, -2, 0, 3] and drop -2, thus the subarray [1, 0, 3] becomes the maximum value.

### Example 2
- **Input:** `arr = [1,-2,-2,3]`
- **Output:** `3`
- **Explanation:** We just choose [3] and it's the maximum sum.

### Example 3
- **Input:** `arr = [-1,-1,-1,-1]`
- **Output:** `-1`
- **Explanation:** The final subarray needs to be non-empty. You can't choose [-1] and delete -1 from it, then get an empty subarray to make the sum equals to 0.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Subarray Sum with One Deletion**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [1,-2,0,3]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** Because we can choose [1, -2, 0, 3] and drop -2, thus the subarray [1, 0, 3] becomes the maximum value.

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
    def maximumSum(self, arr: list[int]) -> int:
        no_del = arr[0]
        one_del = float('-inf')
        ans = arr[0]
        
        for x in arr[1:]:
            one_del = max(one_del + x, no_del)
            no_del = max(x, no_del + x)
            ans = max(ans, no_del, one_del)
            
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
- [3487. Maximum Unique Subarray Sum After Deletion](../../3001-3500/3487-maximum-unique-subarray-sum-after-deletion/)
- [3410. Maximize Subarray Sum After Removing All Occurrences of One Element](../../3001-3500/3410-maximize-subarray-sum-after-removing-all-occurrences-of-one-element/)
- [4058. Maximum Pulse Value After One Subarray Rotation](../../4001-4500/4058-maximum-pulse-value-after-one-subarray-rotation/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/)
