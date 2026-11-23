# LeetCode 2392: Build a Matrix With Conditions

**LeetCode Problem #2392 — Build a Matrix With Conditions**
Solve LeetCode Build a Matrix With Conditions using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Build a Matrix With Conditions |
| LeetCode | #2392 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **positive** integer `k`. You are also given:

a 2D integer array `rowConditions` of size `n` where `rowConditions[i] = [above_i, below_i]`, and 
 a 2D integer array `colConditions` of size `m` where `colConditions[i] = [left_i, right_i]`.

The two arrays contain integers from `1` to `k`.

You have to build a `k x k` matrix that contains each of the numbers from `1` to `k` **exactly once**. The remaining cells should have the value `0`.

The matrix should also satisfy the following conditions:

The number `above_i` should appear in a **row** that is strictly **above** the row at which the number `below_i` appears for all `i` from `0` to `n - 1`. 
 The number `left_i` should appear in a **column** that is strictly **left** of the column at which the number `right_i` appears for all `i` from `0` to `m - 1`.

Return ***any** matrix that satisfies the conditions*. If no answer exists, return an empty matrix.

## Constraints
- `2 <= k <= 400`
- `1 <= rowConditions.length, colConditions.length <= 10^4`
- `rowConditions[i].length == colConditions[i].length == 2`
- `1 <= above_i, below_i, left_i, right_i <= k`
- `above_i != below_i`
- `left_i != right_i`

## Examples
### Example 1
- **Input:** `k = 3, rowConditions = [[1,2],[3,2]], colConditions = [[2,1],[3,2]]`
- **Output:** `[[3,0,0],[0,0,1],[0,2,0]]`
- **Explanation:** The diagram above shows a valid example of a matrix that satisfies all the conditions.
The row conditions are the following:
- Number 1 is in row 1 , and number 2 is in row 2 , so 1 is above 2 in the matrix.
- Number 3 is in row 0 , and number 2 is in row 2 , so 3 is above 2 in the matrix.
The column conditions are the following:
- Number 2 is in column 1 , and number 1 is in column 2 , so 2 is left of 1 in the matrix.
- Number 3 is in column 0 , and number 2 is in column 1 , so 3 is left of 2 in the matrix.
Note that there may be multiple correct answers.

### Example 2
- **Input:** `k = 3, rowConditions = [[1,2],[2,3],[3,1],[2,3]], colConditions = [[2,1]]`
- **Output:** `[]`
- **Explanation:** From the first two conditions, 3 has to be below 1 but the third conditions needs 3 to be above 1 to be satisfied.
No matrix can satisfy all the conditions, so we return the empty matrix.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Build a Matrix With Conditions**, we observe the problem requirements and utilize the **Stack & Queue** technique. We iterate through the inputs using **Stack Push / Pop Parsing**, leveraging a **Stack** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Stack**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `k = 3, rowConditions = [[1,2],[3,2]], colConditions = [[2,1],[3,2]]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[3,0,0],[0,0,1],[0,2,0]]`.
4. **Verification:** The diagram above shows a valid example of a matrix that satisfies all the conditions.
The row conditions are the following:
- Number 1 is in row 1 , and number 2 is in row 2 , so 1 is above 2 in the matrix.
- Number 3 is in row 0 , and number 2 is in row 2 , so 3 is above 2 in the matrix.
The column conditions are the following:
- Number 2 is in column 1 , and number 1 is in column 2 , so 2 is left of 1 in the matrix.
- Number 3 is in column 0 , and number 2 is in column 1 , so 3 is left of 2 in the matrix.
Note that there may be multiple correct answers.

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
/**
 * @param {number} k
 * @param {number[][]} rowConditions
 * @param {number[][]} colConditions
 * @return {number[][]}
 */
var buildMatrix = function (k, rowConditions, colConditions) {
    const topo = (conds) => {
        const adj = Array.from({ length: k + 1 }, () => []);
        const indeg = new Int32Array(k + 1);
        for (const [a, b] of conds) {
            adj[a].push(b);
            indeg[b]++;
        }
        const q = [];
        for (let i = 1; i <= k; i++) if (indeg[i] === 0) q.push(i);
        let head = 0;
        while (head < q.length) {
            const u = q[head++];
            for (const v of adj[u]) if (--indeg[v] === 0) q.push(v);
        }
        return q.length === k ? q : null;
    };

    const rows = topo(rowConditions);
    if (!rows) return [];
    const cols = topo(colConditions);
    if (!cols) return [];

    const colPos = new Int32Array(k + 1);
    for (let i = 0; i < k; i++) colPos[cols[i]] = i;

    const mat = Array.from({ length: k }, () => new Array(k).fill(0));
    for (let r = 0; r < k; r++) mat[r][colPos[rows[r]]] = rows[r];
    return mat;
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
- [1737. Change Minimum Characters to Satisfy One of Three Conditions](../../1501-2000/1859-change-minimum-characters-to-satisfy-one-of-three-conditions/)
- [1441. Build an Array With Stack Operations](../../1501-2000/1552-build-an-array-with-stack-operations/)
- [1916. Count Ways to Build Rooms in an Ant Colony](../../1001-1500/1313-count-ways-to-build-rooms-in-an-ant-colony/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/build-a-matrix-with-conditions/)
