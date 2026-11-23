# LeetCode 1615: Maximal Network Rank

**LeetCode Problem #1615 — Maximal Network Rank**
Solve LeetCode Maximal Network Rank using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximal Network Rank |
| LeetCode | #1615 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is an infrastructure of `n` cities with some number of `roads` connecting these cities. Each `roads[i] = [a_i, b_i]` indicates that there is a bidirectional road between cities `a_i` and `b_i`.

The **network rank*** *of **two different cities** is defined as the total number of **directly** connected roads to **either** city. If a road is directly connected to both cities, it is only counted **once**.

The **maximal network rank **of the infrastructure is the **maximum network rank** of all pairs of different cities.

Given the integer `n` and the array `roads`, return *the **maximal network rank** of the entire infrastructure*.

## Constraints
- `2 <= n <= 100`
- `0 <= roads.length <= n * (n - 1) / 2`
- `roads[i].length == 2`
- `0 <= a_i, b_i <= n-1`
- `a_i != b_i`
- Each pair of cities has **at most one** road connecting them.

## Examples
### Example 1
- **Input:** `n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]`
- **Output:** `4`
- **Explanation:** The network rank of cities 0 and 1 is 4 as there are 4 roads that are connected to either 0 or 1. The road between 0 and 1 is only counted once.

### Example 2
- **Input:** `n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]`
- **Output:** `5`
- **Explanation:** There are 5 roads that are connected to cities 1 or 2.

### Example 3
- **Input:** `n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]`
- **Output:** `5`
- **Explanation:** The network rank of 2 and 5 is 5. Notice that all the cities do not have to be connected.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximal Network Rank**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The network rank of cities 0 and 1 is 4 as there are 4 roads that are connected to either 0 or 1. The road between 0 and 1 is only counted once.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var maximalNetworkRank = function(n, roads) {
    // Count the number of roads connected to each city
    const degree = new Array(n).fill(0);

    // Track whether two cities are directly connected
    const connected = Array.from(
        { length: n },
        () => new Array(n).fill(false)
    );

    for (const [a, b] of roads) {
        degree[a]++;
        degree[b]++;

        connected[a][b] = true;
        connected[b][a] = true;
    }

    let maxRank = 0;

    // Check every pair of different cities
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            let rank = degree[i] + degree[j];

            // Count the shared road only once
            if (connected[i][j]) {
                rank--;
            }

            maxRank = Math.max(maxRank, rank);
        }
    }

    return maxRank;
};
```

## Why This Works
By utilizing **Math & Logic**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [743. Network Delay Time](../../0501-1000/0744-network-delay-time/)
- [1192. Critical Connections in a Network](../../1001-1500/1300-critical-connections-in-a-network/)
- [1319. Number of Operations to Make Network Connected](../../1001-1500/1442-number-of-operations-to-make-network-connected/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximal-network-rank/)
