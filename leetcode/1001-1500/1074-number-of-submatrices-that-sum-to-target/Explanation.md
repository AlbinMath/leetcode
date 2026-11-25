# LeetCode 1074: Number of Submatrices That Sum to Target

**LeetCode Problem #1074 — Number of Submatrices That Sum to Target**
Solve LeetCode Number of Submatrices That Sum to Target using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Submatrices That Sum to Target |
| LeetCode | #1074 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a `matrix` and a `target`, return the number of non-empty submatrices that sum to target .

A submatrix `x1, y1, x2, y2` is the set of all cells `matrix[x][y]` with `x1 <= x <= x2` and `y1 <= y <= y2`.

Two submatrices `(x1, y1, x2, y2)` and `(x1', y1', x2', y2')` are different if they have some coordinate that is different: for example, if `x1 != x1'`.

## Constraints
- `1 <= matrix.length <= 100`
- `1 <= matrix[0].length <= 100`
- `-1000 <= matrix[i][j] <= 1000`
- `-10^8 <= target <= 10^8`

## Examples
### Example 1
- **Input:** `matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0`
- **Output:** `4`
- **Explanation:** The four 1x1 submatrices that only contain 0.

### Example 2
- **Input:** `matrix = [[1,-1],[-1,1]], target = 0`
- **Output:** `5`
- **Explanation:** The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.

### Example 3
- **Input:** `matrix = [[904]], target = 0`
- **Output:** `0`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Number of Submatrices That Sum to Target**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The four 1x1 submatrices that only contain 0.

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
var numSubmatrixSumTarget = function(matrix, target) {
    const rows = matrix.length;
    const cols = matrix[0].length;
    let total = 0;

    for (let r1 = 0; r1 < rows; r1++) {
        const colSums = new Int32Array(cols);
        for (let r2 = r1; r2 < rows; r2++) {
            // Accumulate column sums for submatrices bounded by rows [r1, r2]
            for (let c = 0; c < cols; c++) {
                colSums[c] += matrix[r2][c];
            }

            // Count 1D subarrays in colSums that sum to target
            const prefixCounts = new Map();
            prefixCounts.set(0, 1);
            let currSum = 0;

            for (let c = 0; c < cols; c++) {
                currSum += colSums[c];
                total += prefixCounts.get(currSum - target) || 0;
                prefixCounts.set(currSum, (prefixCounts.get(currSum) || 0) + 1);
            }
        }
    }

    return total;
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
- [1498. Number of Subsequences That Satisfy the Given Sum Condition](../../1001-1500/1498-number-of-subsequences-that-satisfy-the-given-sum-condition/)
- [1546. Maximum Number of Non-Overlapping Subarrays With Sum Equals Target](../../1501-2000/1546-maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/)
- [2177. Find Three Consecutive Integers That Sum to a Given Number](../../2001-2500/2177-find-three-consecutive-integers-that-sum-to-a-given-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/)
