# LeetCode 2924: Find Champion II

**LeetCode Problem #2924 — Find Champion II**
Solve LeetCode Find Champion II using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Champion II |
| LeetCode | #2924 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There are `n` teams numbered from `0` to `n - 1` in a tournament; each team is also a node in a **DAG**.

You are given the integer `n` and a **0-indexed** 2D integer array `edges` of length ` m ` representing the **DAG**, where `edges[i] = [u_i, v_i]` indicates that there is a directed edge from team `u_i` to team `v_i` in the graph.

A directed edge from `a` to `b` in the graph means that team `a` is **stronger** than team `b` and team `b` is **weaker** than team `a`.

Team `a` will be the **champion** of the tournament if there is no team `b` that is **stronger** than team `a`.

Return *the team that will be the **champion** of the tournament if there is a **unique** champion, otherwise, return *`-1`*.*

**Notes**

A **cycle** is a series of nodes `a_1, a_2, ..., a_n, a_n+1` such that node `a_1` is the same node as node `a_n+1`, the nodes `a_1, a_2, ..., a_n` are distinct, and there is a directed edge from the node `a_i` to node `a_i+1` for every `i` in the range `[1, n]`. 
 A **DAG** is a directed graph that does not have any **cycle**.

## Constraints
- `1 <= n <= 100`
- `m == edges.length`
- `0 <= m <= n * (n - 1) / 2`
- `edges[i].length == 2`
- `0 <= edge[i][j] <= n - 1`
- `edges[i][0] != edges[i][1]`
- The input is generated such that if team `a` is stronger than team `b`, team `b` is not stronger than team `a`.
- The input is generated such that if team `a` is stronger than team `b` and team `b` is stronger than team `c`, then team `a` is stronger than team `c`.

## Examples
### Example 1
- **Input:** `n = 3, edges = [[0,1],[1,2]]`
- **Output:** `0`
- **Explanation:** Team 1 is weaker than team 0. Team 2 is weaker than team 1. So the champion is team 0.

### Example 2
- **Input:** `n = 4, edges = [[0,2],[1,3],[1,2]]`
- **Output:** `-1`
- **Explanation:** Team 2 is weaker than team 0 and team 1. Team 3 is weaker than team 1. But team 1 and team 0 are not weaker than any other teams. So the answer is -1.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find Champion II**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3, edges = [[0,1],[1,2]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `0`.
4. **Verification:** Team 1 is weaker than team 0. Team 2 is weaker than team 1. So the champion is team 0.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var findChampion = function(n, edges) {
    const indegree = new Array(n).fill(0);

    // Count incoming edges for each team.
    for (const [u, v] of edges) {
        indegree[v]++;
    }

    let champion = -1;

    // Find the unique team with indegree 0.
    for (let i = 0; i < n; i++) {
        if (indegree[i] === 0) {
            if (champion !== -1) {
                return -1;
            }

            champion = i;
        }
    }

    return champion;
};
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
- [2923. Find Champion I](../../2501-3000/2923-find-champion-i/)
- [28. Find the Index of the First Occurrence in a String](../../0001-0500/0028-find-the-index-of-the-first-occurrence-in-a-string/)
- [34. Find First and Last Position of Element in Sorted Array](../../0001-0500/0034-find-first-and-last-position-of-element-in-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-champion-ii/)
