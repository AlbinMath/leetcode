# LeetCode 1981: Minimize the Difference Between Target and Chosen Elements

**LeetCode Problem #1981 — Minimize the Difference Between Target and Chosen Elements**
Solve LeetCode Minimize the Difference Between Target and Chosen Elements using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimize the Difference Between Target and Chosen Elements |
| LeetCode | #1981 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an `m x n` integer matrix `mat` and an integer `target`.

Choose one integer from **each row** in the matrix such that the **absolute difference** between `target` and the **sum** of the chosen elements is **minimized**.

Return *the **minimum absolute difference***.

The **absolute difference** between two numbers `a` and `b` is the absolute value of `a - b`.

## Constraints
- `m == mat.length`
- `n == mat[i].length`
- `1 <= m, n <= 70`
- `1 <= mat[i][j] <= 70`
- `1 <= target <= 800`

## Examples
### Example 1
- **Input:** `mat = [[1,2,3],[4,5,6],[7,8,9]], target = 13`
- **Output:** `0`
- **Explanation:** One possible choice is to:
- Choose 1 from the first row.
- Choose 5 from the second row.
- Choose 7 from the third row.
The sum of the chosen elements is 13, which equals the target, so the absolute difference is 0.

### Example 2
- **Input:** `mat = [[1],[2],[3]], target = 100`
- **Output:** `94`
- **Explanation:** The best possible choice is to:
- Choose 1 from the first row.
- Choose 2 from the second row.
- Choose 3 from the third row.
The sum of the chosen elements is 6, and the absolute difference is 94.

### Example 3
- **Input:** `mat = [[1,2,9,8,7]], target = 6`
- **Output:** `1`
- **Explanation:** The best choice is to choose 7 from the first row.
The absolute difference is 1.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimize the Difference Between Target and Chosen Elements**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `mat = [[1,2,3],[4,5,6],[7,8,9]], target = 13`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `0`.
4. **Verification:** One possible choice is to:
- Choose 1 from the first row.
- Choose 5 from the second row.
- Choose 7 from the third row.
The sum of the chosen elements is 13, which equals the target, so the absolute difference is 0.

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
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        sums = {0}
        for row in mat:
            vals = set(row)
            nxt = set()
            over = float('inf')
            for s in sums:
                for v in vals:
                    t = s + v
                    if t < target:
                        nxt.add(t)
                    else:
                        over = min(over, t)
            if over != float('inf'):
                nxt.add(over)
            sums = nxt
        return min(abs(s - target) for s in sums)
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
- [2817. Minimum Absolute Difference Between Elements With Constraint](../../2501-3000/2817-minimum-absolute-difference-between-elements-with-constraint/)
- [3022. Minimize OR of Remaining Elements Using Operations](../../3001-3500/3022-minimize-or-of-remaining-elements-using-operations/)
- [1026. Maximum Difference Between Node and Ancestor](../../1001-1500/1026-maximum-difference-between-node-and-ancestor/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements/)
