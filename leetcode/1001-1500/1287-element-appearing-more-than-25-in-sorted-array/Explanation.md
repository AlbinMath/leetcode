# LeetCode 1287: Element Appearing More Than 25% In Sorted Array

**LeetCode Problem #1287 — Element Appearing More Than 25% In Sorted Array**
Solve LeetCode Element Appearing More Than 25% In Sorted Array using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Element Appearing More Than 25% In Sorted Array |
| LeetCode | #1287 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array **sorted** in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

## Constraints
- `1 <= arr.length <= 10^4`
- `0 <= arr[i] <= 10^5`

## Examples
### Example 1
- **Input:** `arr = [1,2,2,6,6,6,6,7,10]`
- **Output:** `6`

### Example 2
- **Input:** `arr = [1,1]`
- **Output:** `1`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Element Appearing More Than 25% In Sorted Array**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [1,2,2,6,6,6,6,7,10]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.

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
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        count = 1

        for i in range(1, n):
            if arr[i] == arr[i - 1]:
                count += 1
            else:
                count = 1

            if count > n / 4:
                return arr[i]

        return arr[0]
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
- [34. Find First and Last Position of Element in Sorted Array](../../0001-0500/0034-find-first-and-last-position-of-element-in-sorted-array/)
- [540. Single Element in a Sorted Array](../../0501-1000/0540-single-element-in-a-sorted-array/)
- [215. Kth Largest Element in an Array](../../0001-0500/0215-kth-largest-element-in-an-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/)
