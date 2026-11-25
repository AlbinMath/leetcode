# LeetCode 31: Next Permutation

**LeetCode Problem #31 — Next Permutation**
Solve LeetCode Next Permutation using JavaScript, Python and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Next Permutation |
| LeetCode | #31 |
| Difficulty | Medium |
| Language | JavaScript, Python |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A **permutation** of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for `arr = [1, 2, 3]`, the following are all the permutations of `arr`: `[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]`.

The **next permutation** of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the **next permutation** of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

Examples:

The next permutation of `arr = [1, 2, 3]` is `[1, 3, 2]`. 
 The next permutation of `arr = [2, 3, 1]` is `[3, 1, 2]`. 
 The next permutation of `arr = [3, 2, 1]` is `[1, 2, 3]` because `[3, 2, 1]` does not have a lexicographical larger rearrangement.

Given an array of integers `nums`, *find the next permutation of* `nums`.

The replacement must be ** in place ** and use only constant extra memory.

## Constraints
- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 100`

## Examples
### Example 1
- **Input:** `nums = [1,2,3]`
- **Output:** `[1,3,2]`

### Example 2
- **Input:** `nums = [3,2,1]`
- **Output:** `[1,2,3]`

### Example 3
- **Input:** `nums = [1,1,5]`
- **Output:** `[1,5,1]`

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Next Permutation**, we observe the problem requirements and utilize the **Backtracking** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3]`.
2. **Processing Steps:** We apply **Backtracking Recursive Search** using our **Recursion Tree**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,3,2]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Recursion Tree.

## Pattern
**Backtracking**

## Topics
- Backtracking
- Recursion

## Language
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### JavaScript
```javascript
var nextPermutation = function(nums) {
    let n = nums.length;
    let i = n - 2;

    // Step 1: Find the first decreasing element from the right
    while (i >= 0 && nums[i] >= nums[i + 1]) {
        i--;
    }

    // Step 2: Find the next larger element from the right and swap
    if (i >= 0) {
        let j = n - 1;

        while (nums[j] <= nums[i]) {
            j--;
        }

        [nums[i], nums[j]] = [nums[j], nums[i]];
    }

    // Step 3: Reverse the suffix to get the smallest order
    let left = i + 1;
    let right = n - 1;

    while (left < right) {
        [nums[left], nums[right]] = [nums[right], nums[left]];
        left++;
        right--;
    }
};
```

### Python
```python
class Solution:
    def nextPermutation(self, nums):
        n = len(nums)

        # 1. Find the first decreasing element from the right
        i = n - 2

        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # 2. Find the element just larger than nums[i]
        if i >= 0:
            j = n - 1

            while nums[j] <= nums[i]:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]

        # 3. Reverse the suffix
        left = i + 1
        right = n - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
```

## Why This Works
By utilizing **Backtracking**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [60. Permutation Sequence](../../0001-0500/0060-permutation-sequence/)
- [567. Permutation in String](../../0501-1000/0567-permutation-in-string/)
- [784. Letter Case Permutation](../../0501-1000/0784-letter-case-permutation/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/next-permutation/)
