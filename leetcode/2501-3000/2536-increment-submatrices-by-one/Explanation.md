# LeetCode 2536: Increment Submatrices by One

**LeetCode Problem #2536 — Increment Submatrices by One**
Solve LeetCode Increment Submatrices by One using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Increment Submatrices by One |
| LeetCode | #2536 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a positive integer `n`, indicating that we initially have an `n x n` **0-indexed** integer matrix `mat` filled with zeroes.

You are also given a 2D integer array `query`. For each `query[i] = [row1_i, col1_i, row2_i, col2_i]`, you should do the following operation:

Add `1` to **every element** in the submatrix with the **top left** corner `(row1_i, col1_i)` and the **bottom right** corner `(row2_i, col2_i)`. That is, add `1` to `mat[x][y]` for all `row1_i <= x <= row2_i` and `col1_i <= y <= col2_i`.

Return* the matrix* `mat`* after performing every query.*

## Constraints
- `1 <= n <= 500`
- `1 <= queries.length <= 10^4`
- `0 <= row1_i <= row2_i < n`
- `0 <= col1_i <= col2_i < n`

## Examples
### Example 1
- **Input:** `n = 3, queries = [[1,1,2,2],[0,0,1,1]]`
- **Output:** `[[1,1,0],[1,2,1],[0,1,1]]`
- **Explanation:** The diagram above shows the initial matrix, the matrix after the first query, and the matrix after the second query.
- In the first query, we add 1 to every element in the submatrix with the top left corner (1, 1) and bottom right corner (2, 2).
- In the second query, we add 1 to every element in the submatrix with the top left corner (0, 0) and bottom right corner (1, 1).

### Example 2
- **Input:** `n = 2, queries = [[0,0,1,1]]`
- **Output:** `[[1,1],[1,1]]`
- **Explanation:** The diagram above shows the initial matrix and the matrix after the first query.
- In the first query we add 1 to every element in the matrix.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Increment Submatrices by One**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3, queries = [[1,1,2,2],[0,0,1,1]]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[1,1,0],[1,2,1],[0,1,1]]`.
4. **Verification:** The diagram above shows the initial matrix, the matrix after the first query, and the matrix after the second query.
- In the first query, we add 1 to every element in the submatrix with the top left corner (1, 1) and bottom right corner (2, 2).
- In the second query, we add 1 to every element in the submatrix with the top left corner (0, 0) and bottom right corner (1, 1).

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        diff = [[0] * (n + 1) for _ in range(n + 1)]

        for r1, c1, r2, c2 in queries:
            diff[r1][c1] += 1
            diff[r1][c2 + 1] -= 1
            diff[r2 + 1][c1] -= 1
            diff[r2 + 1][c2 + 1] += 1

        res = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                v = diff[i][j]
                if i > 0:
                    v += res[i - 1][j]
                if j > 0:
                    v += res[i][j - 1]
                if i > 0 and j > 0:
                    v -= res[i - 1][j - 1]
                res[i][j] = v

        return res
```

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1074. Number of Submatrices That Sum to Target](../../1001-1500/1074-number-of-submatrices-that-sum-to-target/)
- [1277. Count Square Submatrices with All Ones](../../1001-1500/1277-count-square-submatrices-with-all-ones/)
- [1504. Count Submatrices With All Ones](../../1501-2000/1504-count-submatrices-with-all-ones/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/increment-submatrices-by-one/)
