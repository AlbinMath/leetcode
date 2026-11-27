# LeetCode 775: Global and Local Inversions

**LeetCode Problem #775 — Global and Local Inversions**
Solve LeetCode Global and Local Inversions using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Global and Local Inversions |
| LeetCode | #775 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` of length `n` which represents a permutation of all the integers in the range `[0, n - 1]`.

The number of **global inversions** is the number of the different pairs `(i, j)` where:

`0 <= i < j < n` 
 `nums[i] > nums[j]`

The number of **local inversions** is the number of indices `i` where:

`0 <= i < n - 1` 
 `nums[i] > nums[i + 1]`

Return `true` *if the number of **global inversions** is equal to the number of **local inversions***.

## Constraints
- `n == nums.length`
- `1 <= n <= 10^5`
- `0 <= nums[i] < n`
- All the integers of `nums` are **unique**.
- `nums` is a permutation of all the numbers in the range `[0, n - 1]`.

## Examples
### Example 1
- **Input:** `nums = [1,0,2]`
- **Output:** `true`
- **Explanation:** There is 1 global inversion and 1 local inversion.

### Example 2
- **Input:** `nums = [1,2,0]`
- **Output:** `false`
- **Explanation:** There are 2 global inversions and 1 local inversion.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Global and Local Inversions**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,0,2]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** There is 1 global inversion and 1 local inversion.

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
    def isIdealPermutation(self, nums: list[int]) -> bool:
        for i, num in enumerate(nums):
            if abs(num - i) > 1:
                return False
        return True
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
- [2373. Largest Local Values in a Matrix](../../2001-2500/2373-largest-local-values-in-a-matrix/)
- [3933. Largest Local Values in a Matrix II](../../3501-4000/3933-largest-local-values-in-a-matrix-ii/)
- [5. Longest Palindromic Substring](../../0001-0500/0005-longest-palindromic-substring/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/global-and-local-inversions/)
