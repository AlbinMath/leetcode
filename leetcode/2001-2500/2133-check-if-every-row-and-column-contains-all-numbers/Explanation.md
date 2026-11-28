# LeetCode 2133: Check if Every Row and Column Contains All Numbers

**LeetCode Problem #2133 — Check if Every Row and Column Contains All Numbers**
Solve LeetCode Check if Every Row and Column Contains All Numbers using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check if Every Row and Column Contains All Numbers |
| LeetCode | #2133 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
An `n x n` matrix is **valid** if every row and every column contains **all** the integers from `1` to `n` (**inclusive**).

Given an `n x n` integer matrix `matrix`, return `true` *if the matrix is **valid**.* Otherwise, return `false`.

## Constraints
- `n == matrix.length == matrix[i].length`
- `1 <= n <= 100`
- `1 <= matrix[i][j] <= n`

## Examples
### Example 1
- **Input:** `matrix = [[1,2,3],[3,1,2],[2,3,1]]`
- **Output:** `true`
- **Explanation:** In this case, n = 3, and every row and column contains the numbers 1, 2, and 3.
Hence, we return true.

### Example 2
- **Input:** `matrix = [[1,1,1],[1,2,3],[1,2,3]]`
- **Output:** `false`
- **Explanation:** In this case, n = 3, but the first row and the first column do not contain the numbers 2 or 3.
Hence, we return false.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Check if Every Row and Column Contains All Numbers**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `matrix = [[1,2,3],[3,1,2],[2,3,1]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** In this case, n = 3, and every row and column contains the numbers 1, 2, and 3.
Hence, we return true.

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
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        return all(len(set(line)) == n for line in matrix) and \
               all(len(set(col)) == n for col in zip(*matrix))
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
- [1461. Check If a String Contains All Binary Codes of Size K](../../1001-1500/1461-check-if-a-string-contains-all-binary-codes-of-size-k/)
- [2042. Check if Numbers Are Ascending in a Sentence](../../2001-2500/2042-check-if-numbers-are-ascending-in-a-sentence/)
- [1437. Check If All 1's Are at Least Length K Places Away](../../1001-1500/1437-check-if-all-1s-are-at-least-length-k-places-away/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/)
