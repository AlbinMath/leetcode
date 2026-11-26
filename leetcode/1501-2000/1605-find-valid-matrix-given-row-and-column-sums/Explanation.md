# LeetCode 1605: Find Valid Matrix Given Row and Column Sums

**LeetCode Problem #1605 — Find Valid Matrix Given Row and Column Sums**
Solve LeetCode Find Valid Matrix Given Row and Column Sums using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Valid Matrix Given Row and Column Sums |
| LeetCode | #1605 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given two arrays `rowSum` and `colSum` of non-negative integers where `rowSum[i]` is the sum of the elements in the `i^th` row and `colSum[j]` is the sum of the elements of the `j^th` column of a 2D matrix. In other words, you do not know the elements of the matrix, but you do know the sums of each row and column.

Find any matrix of **non-negative** integers of size `rowSum.length x colSum.length` that satisfies the `rowSum` and `colSum` requirements.

Return *a 2D array representing **any** matrix that fulfills the requirements*. It's guaranteed that **at least one **matrix that fulfills the requirements exists.

## Constraints
- `1 <= rowSum.length, colSum.length <= 500`
- `0 <= rowSum[i], colSum[i] <= 10^8`
- `sum(rowSum) == sum(colSum)`

## Examples
### Example 1
- **Input:** `rowSum = [3,8], colSum = [4,7]`
- **Output:** `[[3,0],
 [1,7]]`
- **Explanation:** 0^th row: 3 + 0 = 3 == rowSum[0]
1^st row: 1 + 7 = 8 == rowSum[1]
0^th column: 3 + 1 = 4 == colSum[0]
1^st column: 0 + 7 = 7 == colSum[1]
The row and column sums match, and all matrix elements are non-negative.
Another possible matrix is: [[1,2],
 [3,5]]

### Example 2
- **Input:** `rowSum = [5,7,10], colSum = [8,6,8]`
- **Output:** `[[0,5,0],
 [6,1,0],
 [2,0,8]]`

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find Valid Matrix Given Row and Column Sums**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `rowSum = [3,8], colSum = [4,7]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[3,0],
 [1,7]]`.
4. **Verification:** 0^th row: 3 + 0 = 3 == rowSum[0]
1^st row: 1 + 7 = 8 == rowSum[1]
0^th column: 3 + 1 = 4 == colSum[0]
1^st column: 0 + 7 = 7 == colSum[1]
The row and column sums match, and all matrix elements are non-negative.
Another possible matrix is: [[1,2],
 [3,5]]

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
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m, n = len(rowSum), len(colSum)
        res = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                x = min(rowSum[i], colSum[j])
                res[i][j] = x
                rowSum[i] -= x
                colSum[j] -= x

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
- [1982. Find Array Given Subset Sums](../../1501-2000/1982-find-array-given-subset-sums/)
- [373. Find K Pairs with Smallest Sums](../../0001-0500/0373-find-k-pairs-with-smallest-sums/)
- [3883. Count Non Decreasing Arrays With Given Digit Sums](../../3501-4000/3883-count-non-decreasing-arrays-with-given-digit-sums/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/)
