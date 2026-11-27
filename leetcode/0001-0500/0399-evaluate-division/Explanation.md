# LeetCode 399: Evaluate Division

**LeetCode Problem #399 — Evaluate Division**
Solve LeetCode Evaluate Division using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Evaluate Division |
| LeetCode | #399 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an array of variable pairs `equations` and an array of real numbers `values`, where `equations[i] = [A_i, B_i]` and `values[i]` represent the equation `A_i / B_i = values[i]`. Each `A_i` or `B_i` is a string that represents a single variable.

You are also given some `queries`, where `queries[j] = [C_j, D_j]` represents the `j^th` query where you must find the answer for `C_j / D_j = ?`.

Return *the answers to all queries*. If a single answer cannot be determined, return `-1.0`.

**Note:** The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

**Note: **The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

## Constraints
- `1 <= equations.length <= 20`
- `equations[i].length == 2`
- `1 <= A_i.length, B_i.length <= 5`
- `values.length == equations.length`
- `0.0 < values[i] <= 20.0`
- `1 <= queries.length <= 20`
- `queries[i].length == 2`
- `1 <= C_j.length, D_j.length <= 5`
- `A_i, B_i, C_j, D_j` consist of lower case English letters and digits.

## Examples
### Example 1
- **Input:** `equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]`
- **Output:** `[6.00000,0.50000,-1.00000,1.00000,-1.00000]`
- **Explanation:** Given: *a / b = 2.0*, *b / c = 3.0*
queries are: *a / c = ?*, *b / a = ?*, *a / e = ?*, *a / a = ?*, *x / x = ? *
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0

### Example 2
- **Input:** `equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]`
- **Output:** `[3.75000,0.40000,5.00000,0.20000]`

### Example 3
- **Input:** `equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]`
- **Output:** `[0.50000,2.00000,-1.00000,-1.00000]`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Evaluate Division**, we observe the problem requirements and utilize the **Stack & Queue** technique. By maintaining a **Stack**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Stack** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[6.00000,0.50000,-1.00000,1.00000,-1.00000]`.
4. **Verification:** Given: *a / b = 2.0*, *b / c = 3.0*
queries are: *a / c = ?*, *b / a = ?*, *a / e = ?*, *a / a = ?*, *x / x = ? *
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0

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
var calcEquation = function(equations, values, queries) {
    const graph = new Map();

    for (let i = 0; i < equations.length; i++) {
        const [a, b] = equations[i];
        const value = values[i];

        if (!graph.has(a)) graph.set(a, []);
        if (!graph.has(b)) graph.set(b, []);

        graph.get(a).push([b, value]);
        graph.get(b).push([a, 1 / value]);
    }

    function dfs(start, end, visited) {
        if (!graph.has(start) || !graph.has(end)) {
            return -1.0;
        }

        if (start === end) {
            return 1.0;
        }

        visited.add(start);

        for (const [neighbor, weight] of graph.get(start)) {
            if (!visited.has(neighbor)) {
                const result = dfs(neighbor, end, visited);

                if (result !== -1.0) {
                    return weight * result;
                }
            }
        }

        return -1.0;
    }

    return queries.map(([a, b]) => dfs(a, b, new Set()));
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
- [553. Optimal Division](../../0501-1000/0553-optimal-division/)
- [3326. Minimum Division Operations to Make Array Non Decreasing](../../3001-3500/3326-minimum-division-operations-to-make-array-non-decreasing/)
- [150. Evaluate Reverse Polish Notation](../../0001-0500/0150-evaluate-reverse-polish-notation/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/evaluate-division/)
