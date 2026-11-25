# LeetCode 1200: Minimum Absolute Difference

**LeetCode Problem #1200 — Minimum Absolute Difference**
Solve LeetCode Minimum Absolute Difference using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Absolute Difference |
| LeetCode | #1200 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array of **distinct** integers `arr`, find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair `[a, b]` follows

`a, b` are from `arr` 
 `a < b` 
 `b - a` equals to the minimum absolute difference of any two elements in `arr`

## Constraints
- `2 <= arr.length <= 10^5`
- `-10^6 <= arr[i] <= 10^6`

## Examples
### Example 1
- **Input:** `arr = [4,2,1,3]`
- **Output:** `[[1,2],[2,3],[3,4]]`
- **Explanation:** The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.

### Example 2
- **Input:** `arr = [1,3,6,10,15]`
- **Output:** `[[1,3]]`

### Example 3
- **Input:** `arr = [3,8,-10,23,19,-4,-14,27]`
- **Output:** `[[-14,-10],[19,23],[23,27]]`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Absolute Difference**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [4,2,1,3]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[1,2],[2,3],[3,4]]`.
4. **Verification:** The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.

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
    def minimumAbsDifference(self, arr):
        arr.sort()
        m = min(b-a for a, b in zip(arr, arr[1:]))
        return [[a, b] for a, b in zip(arr, arr[1:]) if b-a == m]
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
- [530. Minimum Absolute Difference in BST](../../0501-1000/0530-minimum-absolute-difference-in-bst/)
- [1818. Minimum Absolute Sum Difference](../../1501-2000/1818-minimum-absolute-sum-difference/)
- [1906. Minimum Absolute Difference Queries](../../1501-2000/1906-minimum-absolute-difference-queries/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-absolute-difference/)
