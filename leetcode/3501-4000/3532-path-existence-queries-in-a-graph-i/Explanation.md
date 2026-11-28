# LeetCode 3532: Path Existence Queries in a Graph I

**LeetCode Problem #3532 — Path Existence Queries in a Graph I**
Solve LeetCode Path Existence Queries in a Graph I using Java and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Path Existence Queries in a Graph I |
| LeetCode | #3532 |
| Difficulty | Medium |
| Language | Java |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer `n` representing the number of nodes in a graph, labeled from 0 to `n - 1`.

You are also given an integer array `nums` of length `n` sorted in **non-decreasing** order, and an integer `maxDiff`.

An **undirected **edge exists between nodes `i` and `j` if the **absolute** difference between `nums[i]` and `nums[j]` is **at most** `maxDiff` (i.e., `|nums[i] - nums[j]| <= maxDiff`).

You are also given a 2D integer array `queries`. For each `queries[i] = [u_i, v_i]`, determine whether there exists a path between nodes `u_i` and `v_i`.

Return a boolean array `answer`, where `answer[i]` is `true` if there exists a path between `u_i` and `v_i` in the `i^th` query and `false` otherwise.

## Constraints
- `1 <= n == nums.length <= 10^5`
- `0 <= nums[i] <= 10^5`
- `nums` is sorted in **non-decreasing** order.
- `0 <= maxDiff <= 10^5`
- `1 <= queries.length <= 10^5`
- `queries[i] == [u_i, v_i]`
- `0 <= u_i, v_i < n`

## Examples
### Example 1
- **Input:** `n = 2, nums = [1,3], maxDiff = 1, queries = [[0,0],[0,1]]`
- **Output:** `[true,false]`
- **Explanation:** Query `[0,0]`: Node 0 has a trivial path to itself. 
 Query `[0,1]`: There is no edge between Node 0 and Node 1 because `|nums[0] - nums[1]| = |1 - 3| = 2`, which is greater than `maxDiff`. 
 Thus, the final answer after processing all the queries is `[true, false]`.

### Example 2
- **Input:** `n = 4, nums = [2,5,6,8], maxDiff = 2, queries = [[0,1],[0,2],[1,3],[2,3]]`
- **Output:** `[false,false,true,true]`
- **Explanation:** The resulting graph is: 

 

 
 Query `[0,1]`: There is no edge between Node 0 and Node 1 because `|nums[0] - nums[1]| = |2 - 5| = 3`, which is greater than `maxDiff`. 
 Query `[0,2]`: There is no edge between Node 0 and Node 2 because `|nums[0] - nums[2]| = |2 - 6| = 4`, which is greater than `maxDiff`. 
 Query `[1,3]`: There is a path between Node 1 and Node 3 through Node 2 since `|nums[1] - nums[2]| = |5 - 6| = 1` and `|nums[2] - nums[3]| = |6 - 8| = 2`, both of which are within `maxDiff`. 
 Query `[2,3]`: There is an edge between Node 2 and Node 3 because `|nums[2] - nums[3]| = |6 - 8| = 2`, which is equal to `maxDiff`. 
 Thus, the final answer after processing all the queries is `[false, false, true, true]`.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Path Existence Queries in a Graph I**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 2, nums = [1,3], maxDiff = 1, queries = [[0,0],[0,1]]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[true,false]`.
4. **Verification:** Query `[0,0]`: Node 0 has a trivial path to itself. 
 Query `[0,1]`: There is no edge between Node 0 and Node 1 because `|nums[0] - nums[1]| = |1 - 3| = 2`, which is greater than `maxDiff`. 
 Thus, the final answer after processing all the queries is `[true, false]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
Java

## Source Code
- [solution.java](./solution.java)


```java
class Solution {
    public boolean[] pathExistenceQueries(int n, int[] nums,
                                          int maxDiff, int[][] queries) {

        // component[i] = component number of node i
        int[] component = new int[n];

        int group = 0;
        component[0] = group;

        for (int i = 1; i < n; i++) {
            if (nums[i] - nums[i - 1] > maxDiff) {
                group++;
            }

            component[i] = group;
        }

        boolean[] answer = new boolean[queries.length];

        for (int i = 0; i < queries.length; i++) {
            int u = queries[i][0];
            int v = queries[i][1];

            answer[i] = component[u] == component[v];
        }

        return answer;
    }
}
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
- [3534. Path Existence Queries in a Graph II](../../3501-4000/3534-path-existence-queries-in-a-graph-ii/)
- [3841. Palindromic Path Queries in a Tree](../../3501-4000/3841-palindromic-path-queries-in-a-tree/)
- [1971. Find if Path Exists in Graph](../../1501-2000/1971-find-if-path-exists-in-graph/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/path-existence-queries-in-a-graph-i/)
