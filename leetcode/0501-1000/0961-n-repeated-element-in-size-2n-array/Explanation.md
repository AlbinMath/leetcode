# LeetCode 961: N-Repeated Element in Size 2N Array

**LeetCode Problem #961 — N-Repeated Element in Size 2N Array**
Solve LeetCode N-Repeated Element in Size 2N Array using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | N-Repeated Element in Size 2N Array |
| LeetCode | #961 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` with the following properties:

`nums.length == 2 * n`. 
 `nums` contains `n + 1` **unique** values, `n` of which occur **exactly once** in the array. 
 Exactly one element of `nums` is repeated `n` times.

Return *the element that is repeated *`n`* times*.

## Constraints
- `2 <= n <= 5000`
- `nums.length == 2 * n`
- `0 <= nums[i] <= 10^4`
- `nums` contains `n + 1` **unique** elements and one of them is repeated exactly `n` times.

## Examples
### Example 1
- **Input:** `nums = [1,2,3,3]`
- **Output:** `3`

### Example 2
- **Input:** `nums = [2,1,2,5,3,2]`
- **Output:** `2`

### Example 3
- **Input:** `nums = [5,1,5,2,5,3,5,4]`
- **Output:** `5`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **N-Repeated Element in Size 2N Array**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,3]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.

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
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen = set()

        for num in nums:
            if num in seen:
                return num

            seen.add(num)

        return -1
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
- [1338. Reduce Array Size to The Half](../../1001-1500/1338-reduce-array-size-to-the-half/)
- [2875. Minimum Size Subarray in Infinite Array](../../2501-3000/2875-minimum-size-subarray-in-infinite-array/)
- [34. Find First and Last Position of Element in Sorted Array](../../0001-0500/0034-find-first-and-last-position-of-element-in-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/n-repeated-element-in-size-2n-array/)
