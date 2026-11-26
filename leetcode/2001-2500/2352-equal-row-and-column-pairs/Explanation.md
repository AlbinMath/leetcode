# LeetCode 2352: Equal Row and Column Pairs

**LeetCode Problem #2352 — Equal Row and Column Pairs**
Solve LeetCode Equal Row and Column Pairs using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Equal Row and Column Pairs |
| LeetCode | #2352 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a **0-indexed** `n x n` integer matrix `grid`, *return the number of pairs *`(r_i, c_j)`* such that row *`r_i`* and column *`c_j`* are equal*.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

## Constraints
- `n == grid.length == grid[i].length`
- `1 <= n <= 200`
- `1 <= grid[i][j] <= 10^5`

## Examples
### Example 1
- **Input:** `grid = [[3,2,1],[1,7,6],[2,7,7]]`
- **Output:** `1`
- **Explanation:** There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]

### Example 2
- **Input:** `grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]`
- **Output:** `3`
- **Explanation:** There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Equal Row and Column Pairs**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[3,2,1],[1,7,6],[2,7,7]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]

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
var equalPairs = function(grid) {
    const n = grid.length;
    const rowMap = new Map();
    let count = 0;

    // Store each row and its frequency
    for (let i = 0; i < n; i++) {
        const key = grid[i].join(",");
        rowMap.set(key, (rowMap.get(key) || 0) + 1);
    }

    // Build each column and check matching rows
    for (let j = 0; j < n; j++) {
        const column = [];

        for (let i = 0; i < n; i++) {
            column.push(grid[i][j]);
        }

        const key = column.join(",");
        count += rowMap.get(key) || 0;
    }

    return count;
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
- [2023. Number of Pairs of Strings With Concatenation Equal to Target](../../2001-2500/2023-number-of-pairs-of-strings-with-concatenation-equal-to-target/)
- [2206. Divide Array Into Equal Pairs](../../2001-2500/2206-divide-array-into-equal-pairs/)
- [3265. Count Almost Equal Pairs I](../../3001-3500/3265-count-almost-equal-pairs-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/equal-row-and-column-pairs/)
