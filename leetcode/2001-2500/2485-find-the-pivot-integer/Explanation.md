# LeetCode 2485: Find the Pivot Integer

**LeetCode Problem #2485 — Find the Pivot Integer**
Solve LeetCode Find the Pivot Integer using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Pivot Integer |
| LeetCode | #2485 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a positive integer `n`, find the **pivot integer** `x` such that:

The sum of all elements between `1` and `x` inclusively equals the sum of all elements between `x` and `n` inclusively.

Return *the pivot integer *`x`. If no such integer exists, return `-1`. It is guaranteed that there will be at most one pivot index for the given input.

## Constraints
- `1 <= n <= 1000`

## Examples
### Example 1
- **Input:** `n = 8`
- **Output:** `6`
- **Explanation:** 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.

### Example 2
- **Input:** `n = 1`
- **Output:** `1`
- **Explanation:** 1 is the pivot integer since: 1 = 1.

### Example 3
- **Input:** `n = 4`
- **Output:** `-1`
- **Explanation:** It can be proved that no such integer exist.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find the Pivot Integer**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 8`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.

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
    def pivotInteger(self, n):
        s = n * (n + 1) // 2
        x = int(s ** 0.5)
        return x if x * x == s else -1
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
- [1237. Find Positive Integer Solution for a Given Equation](../../1001-1500/1237-find-positive-integer-solution-for-a-given-equation/)
- [1394. Find Lucky Integer in an Array](../../1001-1500/1394-find-lucky-integer-in-an-array/)
- [1985. Find the Kth Largest Integer in the Array](../../1501-2000/1985-find-the-kth-largest-integer-in-the-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-pivot-integer/)
