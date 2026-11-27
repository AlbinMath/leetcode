# LeetCode 2097: Valid Arrangement of Pairs

**LeetCode Problem #2097 — Valid Arrangement of Pairs**
Solve LeetCode Valid Arrangement of Pairs using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Valid Arrangement of Pairs |
| LeetCode | #2097 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **0-indexed** 2D integer array `pairs` where `pairs[i] = [start_i, end_i]`. An arrangement of `pairs` is **valid** if for every index `i` where `1 <= i < pairs.length`, we have `end_i-1 == start_i`.

Return ***any** valid arrangement of *`pairs`.

**Note:** The inputs will be generated such that there exists a valid arrangement of `pairs`.

## Constraints
- `1 <= pairs.length <= 10^5`
- `pairs[i].length == 2`
- `0 <= start_i, end_i <= 10^9`
- `start_i != end_i`
- No two pairs are exactly the same.
- There **exists** a valid arrangement of `pairs`.

## Examples
### Example 1
- **Input:** `pairs = [[5,1],[4,5],[11,9],[9,4]]`
- **Output:** `[[11,9],[9,4],[4,5],[5,1]]`
- **Explanation:** This is a valid arrangement since end_i-1 always equals start_i.
end_0 = 9 == 9 = start_1 
end_1 = 4 == 4 = start_2
end_2 = 5 == 5 = start_3

### Example 2
- **Input:** `pairs = [[1,3],[3,2],[2,1]]`
- **Output:** `[[1,3],[3,2],[2,1]]`
- **Explanation:** This is a valid arrangement since end_i-1 always equals start_i.
end_0 = 3 == 3 = start_1
end_1 = 2 == 2 = start_2
The arrangements [[2,1],[1,3],[3,2]] and [[3,2],[2,1],[1,3]] are also valid.

### Example 3
- **Input:** `pairs = [[1,2],[1,3],[2,1]]`
- **Output:** `[[1,2],[2,1],[1,3]]`
- **Explanation:** This is a valid arrangement since end_i-1 always equals start_i.
end_0 = 2 == 2 = start_1
end_1 = 1 == 1 = start_2

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Valid Arrangement of Pairs**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `pairs = [[5,1],[4,5],[11,9],[9,4]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[11,9],[9,4],[4,5],[5,1]]`.
4. **Verification:** This is a valid arrangement since end_i-1 always equals start_i.
end_0 = 9 == 9 = start_1 
end_1 = 4 == 4 = start_2
end_2 = 5 == 5 = start_3

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
var validArrangement = function(pairs) {
    const graph = new Map();
    const inDegree = new Map();
    const outDegree = new Map();

    // Build directed graph and calculate degrees
    for (const [u, v] of pairs) {
        if (!graph.has(u)) graph.set(u, []);

        graph.get(u).push(v);

        outDegree.set(u, (outDegree.get(u) || 0) + 1);
        inDegree.set(v, (inDegree.get(v) || 0) + 1);

        // Ensure both nodes exist in degree maps
        if (!inDegree.has(u)) inDegree.set(u, 0);
        if (!outDegree.has(v)) outDegree.set(v, 0);
    }

    // Find Eulerian path starting node
    let start = pairs[0][0];

    for (const node of graph.keys()) {
        const out = outDegree.get(node) || 0;
        const incoming = inDegree.get(node) || 0;

        if (out - incoming === 1) {
            start = node;
            break;
        }
    }

    // Hierholzer's algorithm (iterative DFS)
    const stack = [start];
    const path = [];

    while (stack.length > 0) {
        const node = stack[stack.length - 1];
        const neighbors = graph.get(node);

        if (neighbors && neighbors.length > 0) {
            stack.push(neighbors.pop());
        } else {
            path.push(stack.pop());
        }
    }

    // Reverse the Eulerian path
    path.reverse();

    // Convert node sequence into pairs
    const result = [];

    for (let i = 0; i < path.length - 1; i++) {
        result.push([path[i], path[i + 1]]);
    }

    return result;
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
- [526. Beautiful Arrangement](../../0501-1000/0526-beautiful-arrangement/)
- [667. Beautiful Arrangement II](../../0501-1000/0667-beautiful-arrangement-ii/)
- [24. Swap Nodes in Pairs](../../0001-0500/0024-swap-nodes-in-pairs/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/valid-arrangement-of-pairs/)
