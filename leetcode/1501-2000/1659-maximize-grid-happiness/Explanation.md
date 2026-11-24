# LeetCode 1659: Maximize Grid Happiness

**LeetCode Problem #1659 — Maximize Grid Happiness**
Solve LeetCode Maximize Grid Happiness using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximize Grid Happiness |
| LeetCode | #1659 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given four integers, `m`, `n`, `introvertsCount`, and `extrovertsCount`. You have an `m x n` grid, and there are two types of people: introverts and extroverts. There are `introvertsCount` introverts and `extrovertsCount` extroverts.

You should decide how many people you want to live in the grid and assign each of them one grid cell. Note that you **do not** have to have all the people living in the grid.

The **happiness** of each person is calculated as follows:

Introverts **start** with `120` happiness and **lose** `30` happiness for each neighbor (introvert or extrovert). 
 Extroverts **start** with `40` happiness and **gain** `20` happiness for each neighbor (introvert or extrovert).

Neighbors live in the directly adjacent cells north, east, south, and west of a person's cell.

The **grid happiness** is the **sum** of each person's happiness. Return* the **maximum possible grid happiness**.*

## Constraints
- `1 <= m, n <= 5`
- `0 <= introvertsCount, extrovertsCount <= min(m * n, 6)`

## Examples
### Example 1
- **Input:** `m = 2, n = 3, introvertsCount = 1, extrovertsCount = 2`
- **Output:** `240`
- **Explanation:** Assume the grid is 1-indexed with coordinates (row, column).
We can put the introvert in cell (1,1) and put the extroverts in cells (1,3) and (2,3).
- Introvert at (1,1) happiness: 120 (starting happiness) - (0 * 30) (0 neighbors) = 120
- Extrovert at (1,3) happiness: 40 (starting happiness) + (1 * 20) (1 neighbor) = 60
- Extrovert at (2,3) happiness: 40 (starting happiness) + (1 * 20) (1 neighbor) = 60
The grid happiness is 120 + 60 + 60 = 240.
The above figure shows the grid in this example with each person's happiness. The introvert stays in the light green cell while the extroverts live on the light purple cells.

### Example 2
- **Input:** `m = 3, n = 1, introvertsCount = 2, extrovertsCount = 1`
- **Output:** `260`
- **Explanation:** Place the two introverts in (1,1) and (3,1) and the extrovert at (2,1).
- Introvert at (1,1) happiness: 120 (starting happiness) - (1 * 30) (1 neighbor) = 90
- Extrovert at (2,1) happiness: 40 (starting happiness) + (2 * 20) (2 neighbors) = 80
- Introvert at (3,1) happiness: 120 (starting happiness) - (1 * 30) (1 neighbor) = 90
The grid happiness is 90 + 80 + 90 = 260.

### Example 3
- **Input:** `m = 2, n = 2, introvertsCount = 4, extrovertsCount = 0`
- **Output:** `240`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Maximize Grid Happiness**, we observe the problem requirements and utilize the **Tree & Graph** technique. By maintaining a **Tree / Graph / Grid**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Tree / Graph / Grid** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `m = 2, n = 3, introvertsCount = 1, extrovertsCount = 2`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `240`.
4. **Verification:** Assume the grid is 1-indexed with coordinates (row, column).
We can put the introvert in cell (1,1) and put the extroverts in cells (1,3) and (2,3).
- Introvert at (1,1) happiness: 120 (starting happiness) - (0 * 30) (0 neighbors) = 120
- Extrovert at (1,3) happiness: 40 (starting happiness) + (1 * 20) (1 neighbor) = 60
- Extrovert at (2,3) happiness: 40 (starting happiness) + (1 * 20) (1 neighbor) = 60
The grid happiness is 120 + 60 + 60 = 240.
The above figure shows the grid in this example with each person's happiness. The introvert stays in the light green cell while the extroverts live on the light purple cells.

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
/**
 * @param {number} m
 * @param {number} n
 * @param {number} introvertsCount
 * @param {number} extrovertsCount
 * @return {number}
 */
var getMaxGridHappiness = function(
    m,
    n,
    introvertsCount,
    extrovertsCount
) {
    const BASE_INTRO = 120;
    const BASE_EXTRO = 40;

    // Combined happiness change caused by one adjacent pair.
    const interaction = [
        [0, 0, 0],
        [0, -60, -10],
        [0, -10, 40]
    ];

    const totalCells = m * n;
    const maskSize = 3 ** n;
    const highestPlace = 3 ** (n - 1);
    const memo = new Map();

    function dfs(pos, intro, extro, mask) {
        if (pos === totalCells) {
            return 0;
        }

        const key = `${pos},${intro},${extro},${mask}`;

        if (memo.has(key)) {
            return memo.get(key);
        }

        const col = pos % n;
        const row = Math.floor(pos / n);

        // The most significant base-3 digit is the cell above.
        const above = row > 0
            ? Math.floor(mask / highestPlace)
            : 0;

        // The least significant digit is the cell to the left.
        const left = col > 0 ? mask % 3 : 0;

        // Option 1: Leave this cell empty.
        const nextMaskEmpty = (mask * 3) % maskSize;
        let best = dfs(pos + 1, intro, extro, nextMaskEmpty);

        // Option 2: Place an introvert.
        if (intro > 0) {
            let happiness = BASE_INTRO;

            happiness += interaction[1][above];
            happiness += interaction[1][left];

            const nextMask = (mask * 3 + 1) % maskSize;

            best = Math.max(
                best,
                happiness + dfs(
                    pos + 1,
                    intro - 1,
                    extro,
                    nextMask
                )
            );
        }

        // Option 3: Place an extrovert.
        if (extro > 0) {
            let happiness = BASE_EXTRO;

            happiness += interaction[2][above];
            happiness += interaction[2][left];

            const nextMask = (mask * 3 + 2) % maskSize;

            best = Math.max(
                best,
                happiness + dfs(
                    pos + 1,
                    intro,
                    extro - 1,
                    nextMask
                )
            );
        }

        memo.set(key, best);
        return best;
    }

    return dfs(
        0,
        introvertsCount,
        extrovertsCount,
        0
    );
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
- [840. Magic Squares In Grid](../../0501-1000/0840-magic-squares-in-grid/)
- [1260. Shift 2D Grid](../../1001-1500/1260-shift-2d-grid/)
- [1293. Shortest Path in a Grid with Obstacles Elimination](../../1001-1500/1293-shortest-path-in-a-grid-with-obstacles-elimination/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximize-grid-happiness/)
