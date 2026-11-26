# LeetCode 2467: Most Profitable Path in a Tree

**LeetCode Problem #2467 — Most Profitable Path in a Tree**
Solve LeetCode Most Profitable Path in a Tree using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Most Profitable Path in a Tree |
| LeetCode | #2467 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
There is an undirected tree with `n` nodes labeled from `0` to `n - 1`, rooted at node `0`. You are given a 2D integer array `edges` of length `n - 1` where `edges[i] = [a_i, b_i]` indicates that there is an edge between nodes `a_i` and `b_i` in the tree.

At every node `i`, there is a gate. You are also given an array of even integers `amount`, where `amount[i]` represents:

the price needed to open the gate at node `i`, if `amount[i]` is negative, or, 
 the cash reward obtained on opening the gate at node `i`, otherwise.

The game goes on as follows:

Initially, Alice is at node `0` and Bob is at node `bob`. 
 At every second, Alice and Bob each move to an adjacent node. Alice moves towards some **leaf node**, while Bob moves towards node `0`. 
 For **every** node along their path, Alice and Bob either spend money to open the gate at that node, or accept the reward. Note that:
 
 If the gate is **already open**, no price will be required, nor will there be any cash reward. 
 If Alice and Bob reach the node **simultaneously**, they share the price/reward for opening the gate there. In other words, if the price to open the gate is `c`, then both Alice and Bob pay `c / 2` each. Similarly, if the reward at the gate is `c`, both of them receive `c / 2` each. 
 
 
 If Alice reaches a leaf node, she stops moving. Similarly, if Bob reaches node `0`, he stops moving. Note that these events are **independent** of each other.

Return* the **maximum** net income Alice can have if she travels towards the optimal leaf node.*

## Constraints
- `2 <= n <= 10^5`
- `edges.length == n - 1`
- `edges[i].length == 2`
- `0 <= a_i, b_i < n`
- `a_i != b_i`
- `edges` represents a valid tree.
- `1 <= bob < n`
- `amount.length == n`
- `amount[i]` is an **even** integer in the range `[-10^4, 10^4]`.

## Examples
### Example 1
- **Input:** `edges = [[0,1],[1,2],[1,3],[3,4]], bob = 3, amount = [-2,4,2,-4,6]`
- **Output:** `6`
- **Explanation:** The above diagram represents the given tree. The game goes as follows:
- Alice is initially on node 0, Bob on node 3. They open the gates of their respective nodes.
 Alice's net income is now -2.
- Both Alice and Bob move to node 1. 
 Since they reach here simultaneously, they open the gate together and share the reward.
 Alice's net income becomes -2 + (4 / 2) = 0.
- Alice moves on to node 3. Since Bob already opened its gate, Alice's income remains unchanged.
 Bob moves on to node 0, and stops moving.
- Alice moves on to node 4 and opens the gate there. Her net income becomes 0 + 6 = 6.
Now, neither Alice nor Bob can make any further moves, and the game ends.
It is not possible for Alice to get a higher net income.

### Example 2
- **Input:** `edges = [[0,1]], bob = 1, amount = [-7280,2350]`
- **Output:** `-7280`
- **Explanation:** Alice follows the path 0->1 whereas Bob follows the path 1->0.
Thus, Alice opens the gate at node 0 only. Hence, her net income is -7280.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Most Profitable Path in a Tree**, we observe the problem requirements and utilize the **Tree & Graph** technique. We decompose the problem into overlapping subproblems using a **Tree / Graph / Grid**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `edges = [[0,1],[1,2],[1,3],[3,4]], bob = 3, amount = [-2,4,2,-4,6]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** The above diagram represents the given tree. The game goes as follows:
- Alice is initially on node 0, Bob on node 3. They open the gates of their respective nodes.
 Alice's net income is now -2.
- Both Alice and Bob move to node 1. 
 Since they reach here simultaneously, they open the gate together and share the reward.
 Alice's net income becomes -2 + (4 / 2) = 0.
- Alice moves on to node 3. Since Bob already opened its gate, Alice's income remains unchanged.
 Bob moves on to node 0, and stops moving.
- Alice moves on to node 4 and opens the gate there. Her net income becomes 0 + 6 = 6.
Now, neither Alice nor Bob can make any further moves, and the game ends.
It is not possible for Alice to get a higher net income.

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
var mostProfitablePath = function(edges, bob, amount) {
    const n = amount.length;

    // Build undirected graph.
    const graph = Array.from({ length: n }, () => []);

    for (const [u, v] of edges) {
        graph[u].push(v);
        graph[v].push(u);
    }

    // Step 1: Find parent and depth of every node.
    const parent = new Array(n).fill(-1);
    const depth = new Array(n).fill(0);
    const order = [0];

    parent[0] = -2;

    for (let i = 0; i < order.length; i++) {
        const u = order[i];

        for (const v of graph[u]) {
            if (v === parent[u]) continue;

            parent[v] = u;
            depth[v] = depth[u] + 1;
            order.push(v);
        }
    }

    // Step 2: Calculate Bob's arrival time.
    const bobTime = new Array(n).fill(Infinity);

    let node = bob;
    let time = 0;

    while (node !== -2) {
        bobTime[node] = time++;
        node = parent[node];
    }

    // Step 3: DFS all Alice paths.
    let answer = -Infinity;

    const stack = [[0, -1, 0, 0]];
    // [node, parent, Alice time, current income]

    while (stack.length > 0) {
        const [u, p, aliceTime, income] = stack.pop();

        let gain = 0;

        if (aliceTime < bobTime[u]) {
            gain = amount[u];
        } else if (aliceTime === bobTime[u]) {
            gain = amount[u] / 2;
        }

        const currentIncome = income + gain;

        // A leaf is a node with no children.
        if (u !== 0 && graph[u].length === 1) {
            answer = Math.max(answer, currentIncome);
            continue;
        }

        for (const v of graph[u]) {
            if (v === p) continue;

            stack.push([
                v,
                u,
                aliceTime + 1,
                currentIncome
            ]);
        }
    }

    return answer;
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
- [124. Binary Tree Maximum Path Sum](../../0001-0500/0124-binary-tree-maximum-path-sum/)
- [1104. Path In Zigzag Labelled Binary Tree](../../1001-1500/1104-path-in-zigzag-labelled-binary-tree/)
- [1372. Longest ZigZag Path in a Binary Tree](../../1001-1500/1372-longest-zigzag-path-in-a-binary-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/most-profitable-path-in-a-tree/)
