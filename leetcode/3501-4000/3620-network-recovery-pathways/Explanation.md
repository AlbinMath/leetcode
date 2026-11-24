# LeetCode 3620: Network Recovery Pathways

**LeetCode Problem #3620 — Network Recovery Pathways**
Solve LeetCode Network Recovery Pathways using PHP and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Network Recovery Pathways |
| LeetCode | #3620 |
| Difficulty | Hard |
| Language | PHP |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a directed acyclic graph of `n` nodes numbered from 0 to `n &minus; 1`. This is represented by a 2D array edges of length `m` , where edges[i] = [u_i, v_i, cost_i] indicates a one‑way communication from node  u_i to node  v_i with a recovery cost of  cost_i .

Some nodes may be offline. You are given a boolean array online where online[i] = true means node  i is online. Nodes 0 and `n &minus; 1` are always online.

A path from 0 to `n &minus; 1` is valid if:

All intermediate nodes on the path are online. 
 The total recovery cost of all edges on the path does not exceed `k`.

For each valid path, define its score as the minimum edge‑cost along that path.

Return the **maximum** path score (i.e., the largest **minimum**-edge cost) among all valid paths. If no valid path exists, return -1.

## Constraints
- n == online.length
- 2 <= n <= 5 * 10^4
- 0 <= m == edges.length <= `min(10^5, n * (n - 1) / 2)`
- 0 <= u_i, v_i < n
- 0 <= cost_i <= 10^9
- 0 <= k <= 5 * 10^13

## Examples
### Example 1
- **Input:** `edges = [[0,1,5],[1,3,10],[0,2,3],[2,3,4]], online = [true,true,true,true], k = 10`
- **Output:** `3`
- **Explanation:** The graph has two possible routes from node 0 to node 3: 

 
 
 Path `0 &rarr; 1 &rarr; 3` 

 
 
 Total cost = `5 + 10 = 15`, which exceeds k (`15 > 10`), so this path is invalid. 
 
 
 
 
 Path `0 &rarr; 2 &rarr; 3` 

 
 
 Total cost = `3 + 4 = 7 <= k`, so this path is valid. 
 
 
 The minimum edge‐cost along this path is `min(3, 4) = 3`. 
 
 
 
 
 
 
 There are no other valid paths. Hence, the maximum among all valid path‐scores is 3.

### Example 2
- **Input:** `edges = [[0,1,7],[1,4,5],[0,2,6],[2,3,6],[3,4,2],[2,4,6]], online = [true,true,true,false,true], k = 12`
- **Output:** `6`
- **Explanation:** Node 3 is offline, so any path passing through 3 is invalid. 
 
 
 Consider the remaining routes from 0 to 4: 

 
 
 Path `0 &rarr; 1 &rarr; 4` 

 
 
 Total cost = `7 + 5 = 12 <= k`, so this path is valid. 
 
 
 The minimum edge‐cost along this path is `min(7, 5) = 5`. 
 
 
 
 
 Path `0 &rarr; 2 &rarr; 3 &rarr; 4` 

 
 
 Node 3 is offline, so this path is invalid regardless of cost. 
 
 
 
 
 Path `0 &rarr; 2 &rarr; 4` 

 
 
 Total cost = `6 + 6 = 12 <= k`, so this path is valid. 
 
 
 The minimum edge‐cost along this path is `min(6, 6) = 6`. 
 
 
 
 
 
 
 Among the two valid paths, their scores are 5 and 6. Therefore, the answer is 6.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Network Recovery Pathways**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `edges = [[0,1,5],[1,3,10],[0,2,3],[2,3,4]], online = [true,true,true,true], k = 10`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The graph has two possible routes from node 0 to node 3: 

 
 
 Path `0 &rarr; 1 &rarr; 3` 

 
 
 Total cost = `5 + 10 = 15`, which exceeds k (`15 > 10`), so this path is invalid. 
 
 
 
 
 Path `0 &rarr; 2 &rarr; 3` 

 
 
 Total cost = `3 + 4 = 7 <= k`, so this path is valid. 
 
 
 The minimum edge‐cost along this path is `min(3, 4) = 3`. 
 
 
 
 
 
 
 There are no other valid paths. Hence, the maximum among all valid path‐scores is 3.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Sorted Array.

## Pattern
**Binary Search**

## Topics
- Binary Search
- Divide and Conquer
- Search Space

## Language
PHP

## Source Code
- [solution.php](./solution.php)


```php
class Solution {

    /**
     * @param Integer[][] $edges
     * @param Boolean[] $online
     * @param Integer $k
     * @return Integer
     */
    function findMaxPathScore($edges, $online, $k) {
        $n = count($online);

        /*
         * Build graph using only online nodes.
         * An offline intermediate node can never be part
         * of a valid path.
         */
        $graph = array_fill(0, $n, []);
        $indegree = array_fill(0, $n, 0);

        $maxCost = 0;

        foreach ($edges as $edge) {
            $u = $edge[0];
            $v = $edge[1];
            $cost = $edge[2];

            if (!$online[$u] || !$online[$v]) {
                continue;
            }

            $graph[$u][] = [$v, $cost];
            $indegree[$v]++;

            if ($cost > $maxCost) {
                $maxCost = $cost;
            }
        }

        /*
         * Topological sort (Kahn's algorithm).
         */
        $queue = [];
        $head = 0;

        for ($i = 0; $i < $n; $i++) {
            if ($indegree[$i] == 0) {
                $queue[] = $i;
            }
        }

        $topo = [];

        while ($head < count($queue)) {
            $u = $queue[$head++];
            $topo[] = $u;

            foreach ($graph[$u] as $edge) {
                $v = $edge[0];

                $indegree[$v]--;

                if ($indegree[$v] == 0) {
                    $queue[] = $v;
                }
            }
        }

        /*
         * Check whether a path exists whose:
         *
         * 1. Every edge cost >= $threshold
         * 2. Total cost <= k
         */
        $check = function ($threshold) use (
            &$graph,
            &$topo,
            $n,
            $k
        ) {
            $INF = PHP_INT_MAX;

            $dist = array_fill(0, $n, $INF);
            $dist[0] = 0;

            foreach ($topo as $u) {

                if ($dist[$u] === $INF) {
                    continue;
                }

                /*
                 * No need to continue paths already over budget.
                 */
                if ($dist[$u] > $k) {
                    continue;
                }

                foreach ($graph[$u] as $edge) {
                    $v = $edge[0];
                    $cost = $edge[1];

                    /*
                     * This edge would make the path score
                     * smaller than the threshold.
                     */
                    if ($cost < $threshold) {
                        continue;
                    }

                    $newCost = $dist[$u] + $cost;

                    /*
                     * We only care about paths within budget.
                     */
                    if ($newCost <= $k && $newCost < $dist[$v]) {
                        $dist[$v] = $newCost;
                    }
                }
            }

            return $dist[$n - 1] <= $k;
        };

        /*
         * No path at all.
         */
        if (!$check(0)) {
            return -1;
        }

        /*
         * Binary search for the maximum possible
         * minimum edge cost.
         */
        $left = 0;
        $right = $maxCost;

        while ($left < $right) {
            $mid = intdiv($left + $right + 1, 2);

            if ($check($mid)) {
                $left = $mid;
            } else {
                $right = $mid - 1;
            }
        }

        return $left;
    }
}
```

## Why This Works
By utilizing **Binary Search**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Applying standard binary search without accounting for array rotation or duplicates.
2. Off-by-one errors when updating boundary pointers (`left = mid + 1` vs `right = mid - 1`).
3. Integer overflow during midpoint calculation (use `mid = left + (right - left) // 2`).

## Interview Notes
- **Tests:** Logarithmic search space reduction, boundary handling, and invariant preservation.
- **Follow-up:** How does performance change if the array contains duplicate elements?

## Related Problems
- [3586. Find COVID Recovery Patients](../../3501-4000/3586-find-covid-recovery-patients/)
- [743. Network Delay Time](../../0501-1000/0743-network-delay-time/)
- [1192. Critical Connections in a Network](../../1001-1500/1192-critical-connections-in-a-network/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/network-recovery-pathways/)
