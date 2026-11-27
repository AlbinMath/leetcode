# LeetCode 2965: Find Missing and Repeated Values

**LeetCode Problem #2965 — Find Missing and Repeated Values**
Solve LeetCode Find Missing and Repeated Values using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Missing and Repeated Values |
| LeetCode | #2965 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** 2D integer matrix ` grid ` of size `n * n` with values in the range `[1, n^2]`. Each integer appears **exactly once** except `a` which appears **twice** and `b` which is **missing**. The task is to find the repeating and missing numbers `a` and `b`.

Return *a **0-indexed **integer array *`ans`* of size *`2`* where *`ans[0]`* equals to *`a`* and *`ans[1]`* equals to *`b`*.*

## Constraints
- `2 <= n == grid.length == grid[i].length <= 50`
- `1 <= grid[i][j] <= n * n`
- For all `x` that `1 <= x <= n * n` there is exactly one `x` that is not equal to any of the grid members.
- For all `x` that `1 <= x <= n * n` there is exactly one `x` that is equal to exactly two of the grid members.
- For all `x` that `1 <= x <= n * n` except two of them there is exactly one pair of `i, j` that `0 <= i, j <= n - 1` and `grid[i][j] == x`.

## Examples
### Example 1
- **Input:** `grid = [[1,3],[2,2]]`
- **Output:** `[2,4]`
- **Explanation:** Number 2 is repeated and number 4 is missing so the answer is [2,4].

### Example 2
- **Input:** `grid = [[9,1,7],[8,9,2],[3,4,6]]`
- **Output:** `[9,5]`
- **Explanation:** Number 9 is repeated and number 5 is missing so the answer is [9,5].

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find Missing and Repeated Values**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[1,3],[2,2]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,4]`.
4. **Verification:** Number 2 is repeated and number 4 is missing so the answer is [2,4].

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
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        cnt = [0] * (n * n + 1)
        for row in grid:
            for v in row:
                cnt[v] += 1

        a = b = 0
        for x in range(1, n * n + 1):
            if cnt[x] == 2:
                a = x
            elif cnt[x] == 0:
                b = x
        return [a, b]
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
- [2028. Find Missing Observations](../../2001-2500/2028-find-missing-observations/)
- [3068. Find the Maximum Sum of Node Values](../../3001-3500/3068-find-the-maximum-sum-of-node-values/)
- [3471. Find the Largest Almost Missing Integer](../../3001-3500/3471-find-the-largest-almost-missing-integer/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-missing-and-repeated-values/)
