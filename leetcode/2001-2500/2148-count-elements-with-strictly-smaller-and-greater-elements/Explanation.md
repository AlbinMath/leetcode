# LeetCode 2148: Count Elements With Strictly Smaller and Greater Elements 

**LeetCode Problem #2148 — Count Elements With Strictly Smaller and Greater Elements **
Solve LeetCode Count Elements With Strictly Smaller and Greater Elements  using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Elements With Strictly Smaller and Greater Elements  |
| LeetCode | #2148 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `nums`, return *the number of elements that have **both** a strictly smaller and a strictly greater element appear in *`nums`.

## Constraints
- `1 <= nums.length <= 100`
- `-10^5 <= nums[i] <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [11,7,2,15]`
- **Output:** `2`
- **Explanation:** The element 7 has the element 2 strictly smaller than it and the element 11 strictly greater than it.
Element 11 has element 7 strictly smaller than it and element 15 strictly greater than it.
In total there are 2 elements having both a strictly smaller and a strictly greater element appear in `nums`.

### Example 2
- **Input:** `nums = [-3,3,3,90]`
- **Output:** `2`
- **Explanation:** The element 3 has the element -3 strictly smaller than it and the element 90 strictly greater than it.
Since there are two elements with the value 3, in total there are 2 elements having both a strictly smaller and a strictly greater element appear in `nums`.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Elements With Strictly Smaller and Greater Elements **, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [11,7,2,15]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The element 7 has the element 2 strictly smaller than it and the element 11 strictly greater than it.
Element 11 has element 7 strictly smaller than it and element 15 strictly greater than it.
In total there are 2 elements having both a strictly smaller and a strictly greater element appear in `nums`.

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
    def countElements(self, nums: list[int]) -> int:
        min_val = min(nums)
        max_val = max(nums)
        
        return sum(1 for num in nums if min_val < num < max_val)
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
- [3759. Count Elements With at Least K Greater Values](../../3501-4000/3759-count-elements-with-at-least-k-greater-values/)
- [315. Count of Smaller Numbers After Self](../../0001-0500/0315-count-of-smaller-numbers-after-self/)
- [3005. Count Elements With Maximum Frequency](../../3001-3500/3005-count-elements-with-maximum-frequency/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/)
