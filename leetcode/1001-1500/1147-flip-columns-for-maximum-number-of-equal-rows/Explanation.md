# LeetCode 1072: Flip Columns For Maximum Number of Equal Rows

**LeetCode Problem #1072 — Flip Columns For Maximum Number of Equal Rows**
Solve LeetCode Flip Columns For Maximum Number of Equal Rows using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Flip Columns For Maximum Number of Equal Rows |
| LeetCode | #1072 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an `m x n` binary matrix `matrix`.

You can choose any number of columns in the matrix and flip every cell in that column (i.e., Change the value of the cell from `0` to `1` or vice versa).

Return *the maximum number of rows that have all values equal after some number of flips*.

## Constraints
- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 300`
- `matrix[i][j]` is either `0` or `1`.

## Examples
### Example 1
- **Input:** `matrix = [[0,1],[1,1]]`
- **Output:** `1`
- **Explanation:** After flipping no values, 1 row has all values equal.

### Example 2
- **Input:** `matrix = [[0,1],[1,0]]`
- **Output:** `2`
- **Explanation:** After flipping values in the first column, both rows have equal values.

### Example 3
- **Input:** `matrix = [[0,0,0],[0,0,1],[1,1,0]]`
- **Output:** `2`
- **Explanation:** After flipping values in the first two columns, the last two rows have equal values.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Flip Columns For Maximum Number of Equal Rows**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `matrix = [[0,1],[1,1]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** After flipping no values, 1 row has all values equal.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var maxEqualRowsAfterFlips = function(matrix) {
    const patternCounts = new Map();
    let maxRows = 0;

    for (const row of matrix) {
        // Normalize row so its first bit is always 0 (XOR all bits with row[0])
        const first = row[0];
        let pattern = '';
        for (let c = 0; c < row.length; c++) {
            pattern += (row[c] ^ first);
        }

        const count = (patternCounts.get(pattern) || 0) + 1;
        patternCounts.set(pattern, count);
        if (count > maxRows) {
            maxRows = count;
        }
    }

    return maxRows;
};
```

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [2397. Maximum Rows Covered by Columns](../../2001-2500/2482-maximum-rows-covered-by-columns/)
- [3007. Maximum Number That Sum of the Prices Is Less Than or Equal to K](../../3001-3500/3240-maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/)
- [1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold](../../1001-1500/1413-maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/)
