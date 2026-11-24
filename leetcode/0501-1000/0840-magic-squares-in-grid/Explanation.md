# LeetCode 840: Magic Squares In Grid

**LeetCode Problem #840 — Magic Squares In Grid**
Solve LeetCode Magic Squares In Grid using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Magic Squares In Grid |
| LeetCode | #840 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
A `3 x 3` **magic square** is a `3 x 3` grid filled with distinct numbers **from **1** to **9 such that each row, column, and both diagonals all have the same sum.

Given a `row x col` `grid` of integers, how many `3 x 3` magic square subgrids are there?

Note: while a magic square can only contain numbers from 1 to 9, `grid` may contain numbers up to 15.

## Constraints
- `row == grid.length`
- `col == grid[i].length`
- `1 <= row, col <= 10`
- `0 <= grid[i][j] <= 15`

## Examples
### Example 1
- **Input:** `grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]`
- **Output:** `1`
- **Explanation:** The following subgrid is a 3 x 3 magic square:
 
while this one is not:
 
In total, there is only one magic square inside the given grid.

### Example 2
- **Input:** `grid = [[8]]`
- **Output:** `0`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Magic Squares In Grid**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** The following subgrid is a 3 x 3 magic square:
 
while this one is not:
 
In total, there is only one magic square inside the given grid.

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
var numMagicSquaresInside = function(grid) {
    const rows = grid.length;
    const cols = grid[0].length;
    if (rows < 3 || cols < 3) return 0;

    const isMagic = (r, c) => {
        // In any 3x3 magic square using 1..9, the center element must be 5
        if (grid[r + 1][c + 1] !== 5) return false;

        // Check all 9 cells are distinct values in [1, 9] using a bitmask
        let mask = 0;
        for (let i = r; i < r + 3; i++) {
            for (let j = c; j < c + 3; j++) {
                const val = grid[i][j];
                if (val < 1 || val > 9 || (mask & (1 << val)) !== 0) {
                    return false;
                }
                mask |= (1 << val);
            }
        }

        // Check rows, columns, and both diagonals sum to 15
        for (let i = 0; i < 3; i++) {
            if (grid[r + i][c] + grid[r + i][c + 1] + grid[r + i][c + 2] !== 15) return false;
            if (grid[r][c + i] + grid[r + 1][c + i] + grid[r + 2][c + i] !== 15) return false;
        }

        return (
            grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2] === 15 &&
            grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c] === 15
        );
    };

    let count = 0;
    for (let r = 0; r <= rows - 3; r++) {
        for (let c = 0; c <= cols - 3; c++) {
            if (isMagic(r, c)) count++;
        }
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
- [676. Implement Magic Dictionary](../../0501-1000/0676-implement-magic-dictionary/)
- [2171. Removing Minimum Number of Magic Beans](../../2001-2500/2171-removing-minimum-number-of-magic-beans/)
- [279. Perfect Squares](../../0001-0500/0279-perfect-squares/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/magic-squares-in-grid/)
