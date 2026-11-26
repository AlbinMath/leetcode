# LeetCode 2039: The Time When the Network Becomes Idle

**LeetCode Problem #2039 — The Time When the Network Becomes Idle**
Solve LeetCode The Time When the Network Becomes Idle using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | The Time When the Network Becomes Idle |
| LeetCode | #2039 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is a network of `n` servers, labeled from `0` to `n - 1`. You are given a 2D integer array `edges`, where `edges[i] = [u_i, v_i]` indicates there is a message channel between servers `u_i` and `v_i`, and they can pass **any** number of messages to **each other** directly in **one** second. You are also given a **0-indexed** integer array `patience` of length `n`.

All servers are **connected**, i.e., a message can be passed from one server to any other server(s) directly or indirectly through the message channels.

The server labeled `0` is the **master** server. The rest are **data** servers. Each data server needs to send its message to the master server for processing and wait for a reply. Messages move between servers **optimally**, so every message takes the **least amount of time** to arrive at the master server. The master server will process all newly arrived messages **instantly** and send a reply to the originating server via the **reversed path** the message had gone through.

At the beginning of second `0`, each data server sends its message to be processed. Starting from second `1`, at the **beginning** of **every** second, each data server will check if it has received a reply to the message it sent (including any newly arrived replies) from the master server:

If it has not, it will **resend** the message periodically. The data server `i` will resend the message every `patience[i]` second(s), i.e., the data server `i` will resend the message if `patience[i]` second(s) have **elapsed** since the **last** time the message was sent from this server. 
 Otherwise, **no more resending** will occur from this server.

The network becomes **idle** when there are **no** messages passing between servers or arriving at servers.

Return *the **earliest second** starting from which the network becomes **idle***.

## Constraints
- `n == patience.length`
- `2 <= n <= 10^5`
- `patience[0] == 0`
- `1 <= patience[i] <= 10^5` for `1 <= i < n`
- `1 <= edges.length <= min(10^5, n * (n - 1) / 2)`
- `edges[i].length == 2`
- `0 <= u_i, v_i < n`
- `u_i != v_i`
- There are no duplicate edges.
- Each server can directly or indirectly reach another server.

## Examples
Consider the standard input for **The Time When the Network Becomes Idle**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **The Time When the Network Becomes Idle**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
Applying **Two Pointer Convergence & Scanning** step by step to the input yields the expected result.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var networkBecomesIdle = function(edges, patience) {
    const n = patience.length;

    // Build adjacency list
    const graph = Array.from({ length: n }, () => []);

    for (const [u, v] of edges) {
        graph[u].push(v);
        graph[v].push(u);
    }

    // BFS to calculate shortest distance from server 0
    const dist = new Array(n).fill(-1);
    const queue = [0];

    dist[0] = 0;

    let index = 0;

    while (index < queue.length) {
        const node = queue[index++];

        for (const neighbor of graph[node]) {
            if (dist[neighbor] === -1) {
                dist[neighbor] = dist[node] + 1;
                queue.push(neighbor);
            }
        }
    }

    let lastMessageTime = 0;

    // Calculate the last reply arrival time
    for (let i = 1; i < n; i++) {
        const roundTrip = dist[i] * 2;

        // Time when the last repeated message was sent
        const lastSend = Math.floor(
            (roundTrip - 1) / patience[i]
        ) * patience[i];

        // Last reply arrival time
        const lastReply = lastSend + roundTrip;

        lastMessageTime = Math.max(
            lastMessageTime,
            lastReply
        );
    }

    // Network becomes idle one second after the last reply
    return lastMessageTime + 1;
};
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [743. Network Delay Time](../../0501-1000/0743-network-delay-time/)
- [4068. Maximize Meeting Earnings with Idle Gaps](../../4001-4500/4068-maximize-meeting-earnings-with-idle-gaps/)
- [803. Bricks Falling When Hit](../../0501-1000/0803-bricks-falling-when-hit/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/the-time-when-the-network-becomes-idle/)
