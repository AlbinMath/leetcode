# LeetCode 1359: Count All Valid Pickup and Delivery Options

**LeetCode Problem #1359 — Count All Valid Pickup and Delivery Options**
Solve LeetCode Count All Valid Pickup and Delivery Options using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count All Valid Pickup and Delivery Options |
| LeetCode | #1359 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given `n` orders, each order consists of a pickup and a delivery service.

Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i).

Since the answer may be too large, return it modulo 10^9 + 7.

## Constraints
- `1 <= n <= 500`

## Examples
### Example 1
- **Input:** `n = 1`
- **Output:** `1`
- **Explanation:** Unique order (P1, D1), Delivery 1 always is after of Pickup 1.

### Example 2
- **Input:** `n = 2`
- **Output:** `6`
- **Explanation:** All possible orders: 
(P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1) and (P2,D2,P1,D1).
This is an invalid order (P1,D2,P2,D1) because Pickup 2 is after of Delivery 2.

### Example 3
- **Input:** `n = 3`
- **Output:** `90`

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count All Valid Pickup and Delivery Options**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 1`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** Unique order (P1, D1), Delivery 1 always is after of Pickup 1.

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
var countOrders = function(n) {
    const MOD = 1_000_000_007;
    let result = 1;

    for (let i = 2; i <= n; i++) {
        result = (result * (i * (2 * i - 1))) % MOD;
    }

    return result;
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
- [828. Count Unique Characters of All Substrings of a Given String](../../0501-1000/0855-count-unique-characters-of-all-substrings-of-a-given-string/)
- [1277. Count Square Submatrices with All Ones](../../1001-1500/1402-count-square-submatrices-with-all-ones/)
- [1504. Count Submatrices With All Ones](../../1501-2000/1628-count-submatrices-with-all-ones/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/)
