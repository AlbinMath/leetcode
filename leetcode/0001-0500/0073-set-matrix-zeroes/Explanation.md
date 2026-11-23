# LeetCode 73: Set Matrix Zeroes

**LeetCode Problem #73 — Set Matrix Zeroes**
Solve LeetCode Set Matrix Zeroes using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Set Matrix Zeroes |
| LeetCode | #73 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an `m x n` integer matrix `matrix`, if an element is `0`, set its entire row and column to `0`'s.

You must do it in place .

## Constraints
- `m == matrix.length`
- `n == matrix[0].length`
- `1 <= m, n <= 200`
- `-2^31 <= matrix[i][j] <= 2^31 - 1`
- A straightforward solution using `O(mn)` space is probably a bad idea.
- A simple improvement uses `O(m + n)` space, but still not the best solution.
- Could you devise a constant space solution?

## Examples
### Example 1
- **Input:** `matrix = [[1,1,1],[1,0,1],[1,1,1]]`
- **Output:** `[[1,0,1],[0,0,0],[1,0,1]]`

### Example 2
- **Input:** `matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]`
- **Output:** `[[0,0,0,0],[0,4,5,0],[0,3,1,0]]`

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Set Matrix Zeroes**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `matrix = [[1,1,1],[1,0,1],[1,1,1]]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[1,0,1],[0,0,0],[1,0,1]]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var setZeroes = function(matrix) {
    const rows = matrix.length;
    const cols = matrix[0].length;

    let firstRowZero = false;
    let firstColZero = false;

    // Check whether the first row contains zero
    for (let j = 0; j < cols; j++) {
        if (matrix[0][j] === 0) {
            firstRowZero = true;
            break;
        }
    }

    // Check whether the first column contains zero
    for (let i = 0; i < rows; i++) {
        if (matrix[i][0] === 0) {
            firstColZero = true;
            break;
        }
    }

    // Use the first row and column to mark zeroes
    for (let i = 1; i < rows; i++) {
        for (let j = 1; j < cols; j++) {
            if (matrix[i][j] === 0) {
                matrix[i][0] = 0;
                matrix[0][j] = 0;
            }
        }
    }

    // Set marked rows to zero
    for (let i = 1; i < rows; i++) {
        if (matrix[i][0] === 0) {
            for (let j = 1; j < cols; j++) {
                matrix[i][j] = 0;
            }
        }
    }

    // Set marked columns to zero
    for (let j = 1; j < cols; j++) {
        if (matrix[0][j] === 0) {
            for (let i = 1; i < rows; i++) {
                matrix[i][j] = 0;
            }
        }
    }

    // Handle the first row and column last
    if (firstRowZero) {
        for (let j = 0; j < cols; j++) {
            matrix[0][j] = 0;
        }
    }

    if (firstColZero) {
        for (let i = 0; i < rows; i++) {
            matrix[i][0] = 0;
        }
    }
};
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
- [645. Set Mismatch](../../0501-1000/0645-set-mismatch/)
- [762. Prime Number of Set Bits in Binary Representation](../../0501-1000/0767-prime-number-of-set-bits-in-binary-representation/)
- [902. Numbers At Most N Given Digit Set](../../0501-1000/0938-numbers-at-most-n-given-digit-set/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/set-matrix-zeroes/)
