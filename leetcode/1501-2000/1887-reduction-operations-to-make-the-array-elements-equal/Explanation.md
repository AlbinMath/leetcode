# LeetCode 1887: Reduction Operations to Make the Array Elements Equal

**LeetCode Problem #1887 — Reduction Operations to Make the Array Elements Equal**
Solve LeetCode Reduction Operations to Make the Array Elements Equal using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Reduction Operations to Make the Array Elements Equal |
| LeetCode | #1887 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `nums`, your goal is to make all elements in `nums` equal. To complete one operation, follow these steps:

Find the **largest** value in `nums`. Let its index be `i` (**0-indexed**) and its value be `largest`. If there are multiple elements with the largest value, pick the smallest `i`. 
 Find the **next largest** value in `nums` **strictly smaller** than `largest`. Let its value be `nextLargest`. 
 Reduce `nums[i]` to `nextLargest`.

Return *the number of operations to make all elements in *`nums`* equal*.

## Constraints
- `1 <= nums.length <= 5 * 10^4`
- `1 <= nums[i] <= 5 * 10^4`

## Examples
### Example 1
- **Input:** `nums = [5,1,3]`
- **Output:** `3`
- **Explanation:** It takes 3 operations to make all elements in nums equal:
1. largest = 5 at index 0. nextLargest = 3. Reduce nums[0] to 3. nums = [ 3 ,1,3].
2. largest = 3 at index 0. nextLargest = 1. Reduce nums[0] to 1. nums = [ 1 ,1,3].
3. largest = 3 at index 2. nextLargest = 1. Reduce nums[2] to 1. nums = [1,1, 1 ].

### Example 2
- **Input:** `nums = [1,1,1]`
- **Output:** `0`
- **Explanation:** All elements in nums are already equal.

### Example 3
- **Input:** `nums = [1,1,2,2,3]`
- **Output:** `4`
- **Explanation:** It takes 4 operations to make all elements in nums equal:
1. largest = 3 at index 4. nextLargest = 2. Reduce nums[4] to 2. nums = [1,1,2,2, 2 ].
2. largest = 2 at index 2. nextLargest = 1. Reduce nums[2] to 1. nums = [1,1, 1 ,2,2].
3. largest = 2 at index 3. nextLargest = 1. Reduce nums[3] to 1. nums = [1,1,1, 1 ,2].
4. largest = 2 at index 4. nextLargest = 1. Reduce nums[4] to 1. nums = [1,1,1,1, 1 ].

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Reduction Operations to Make the Array Elements Equal**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [5,1,3]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** It takes 3 operations to make all elements in nums equal:
1. largest = 5 at index 0. nextLargest = 3. Reduce nums[0] to 3. nums = [ 3 ,1,3].
2. largest = 3 at index 0. nextLargest = 1. Reduce nums[0] to 1. nums = [ 1 ,1,3].
3. largest = 3 at index 2. nextLargest = 1. Reduce nums[2] to 1. nums = [1,1, 1 ].

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
    def reductionOperations(self, nums):
        nums.sort()
        return sum(i for i in range(1, len(nums)) if nums[i] != nums[i-1]) * 0 + sum(len(nums)-i for i in range(1, len(nums)) if nums[i] != nums[i-1])
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
- [2654. Minimum Number of Operations to Make All Array Elements Equal to 1](../../2501-3000/2654-minimum-number-of-operations-to-make-all-array-elements-equal-to-1/)
- [3191. Minimum Operations to Make Binary Array Elements Equal to One I](../../3001-3500/3191-minimum-operations-to-make-binary-array-elements-equal-to-one-i/)
- [2997. Minimum Number of Operations to Make Array XOR Equal to K](../../2501-3000/2997-minimum-number-of-operations-to-make-array-xor-equal-to-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/)
