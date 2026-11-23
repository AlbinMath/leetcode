# LeetCode 3534: Path Existence Queries in a Graph II

**LeetCode Problem #3534 — Path Existence Queries in a Graph II**
Solve LeetCode Path Existence Queries in a Graph II using PHP and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Path Existence Queries in a Graph II |
| LeetCode | #3534 |
| Difficulty | Hard |
| Language | PHP |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer `n` representing the number of nodes in a graph, labeled from 0 to `n - 1`.

You are also given an integer array `nums` of length `n` and an integer `maxDiff`.

An **undirected **edge exists between nodes `i` and `j` if the **absolute** difference between `nums[i]` and `nums[j]` is **at most** `maxDiff` (i.e., `|nums[i] - nums[j]| <= maxDiff`).

You are also given a 2D integer array `queries`. For each `queries[i] = [u_i, v_i]`, find the **minimum** distance between nodes `u_i` and `v_i`_. If no path exists between the two nodes, return -1 for that query.

Return an array `answer`, where `answer[i]` is the result of the `i^th` query.

**Note:** The edges between the nodes are unweighted.

## Constraints
- `1 <= n == nums.length <= 10^5`
- `0 <= nums[i] <= 10^5`
- `0 <= maxDiff <= 10^5`
- `1 <= queries.length <= 10^5`
- `queries[i] == [u_i, v_i]`
- `0 <= u_i, v_i < n`

## Examples
### Example 1
- **Input:** `n = 5, nums = [1,8,3,4,2], maxDiff = 3, queries = [[0,3],[2,4]]`
- **Output:** `[1,1]`
- **Explanation:** The resulting graph is: 

 

 
 
 
 Query 
 Shortest Path 
 Minimum Distance 
 
 
 [0, 3] 
 0 &rarr; 3 
 1 
 
 
 [2, 4] 
 2 &rarr; 4 
 1 
 
 
 

 Thus, the output is `[1, 1]`.

### Example 2
- **Input:** `n = 5, nums = [5,3,1,9,10], maxDiff = 2, queries = [[0,1],[0,2],[2,3],[4,3]]`
- **Output:** `[1,2,-1,1]`
- **Explanation:** The resulting graph is: 

 
 

 
 
 
 Query 
 Shortest Path 
 Minimum Distance 
 
 
 [0, 1] 
 0 &rarr; 1 
 1 
 
 
 [0, 2] 
 0 &rarr; 1 &rarr; 2 
 2 
 
 
 [2, 3] 
 None 
 -1 
 
 
 [4, 3] 
 3 &rarr; 4 
 1 
 
 
 

 Thus, the output is `[1, 2, -1, 1]`.

### Example 3
- **Input:** `n = 3, nums = [3,6,1], maxDiff = 1, queries = [[0,0],[0,1],[1,2]]`
- **Output:** `[0,-1,-1]`
- **Explanation:** There are no edges between any two nodes because: 

 
 Nodes 0 and 1: `|nums[0] - nums[1]| = |3 - 6| = 3 > 1` 
 Nodes 0 and 2: `|nums[0] - nums[2]| = |3 - 1| = 2 > 1` 
 Nodes 1 and 2: `|nums[1] - nums[2]| = |6 - 1| = 5 > 1` 
 

 Thus, no node can reach any other node, and the output is `[0, -1, -1]`.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Path Existence Queries in a Graph II**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 5, nums = [1,8,3,4,2], maxDiff = 3, queries = [[0,3],[2,4]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,1]`.
4. **Verification:** The resulting graph is: 

 

 
 
 
 Query 
 Shortest Path 
 Minimum Distance 
 
 
 [0, 3] 
 0 &rarr; 3 
 1 
 
 
 [2, 4] 
 2 &rarr; 4 
 1 
 
 
 

 Thus, the output is `[1, 1]`.

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
PHP

## Source Code
- [solution.php](./solution.php)


```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[] $nums
     * @param Integer $maxDiff
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function pathExistenceQueries($n, $nums, $maxDiff, $queries) {

        /*
         * Sort [value, originalIndex]
         */
        $arr = [];

        for ($i = 0; $i < $n; $i++) {
            $arr[] = [$nums[$i], $i];
        }

        usort($arr, function ($a, $b) {
            return $a[0] <=> $b[0];
        });

        /*
         * sortedValues[i] = value at sorted position i
         * position[originalIndex] = sorted position
         */
        $sortedValues = array_fill(0, $n, 0);
        $position = array_fill(0, $n, 0);

        for ($i = 0; $i < $n; $i++) {
            $sortedValues[$i] = $arr[$i][0];
            $position[$arr[$i][1]] = $i;
        }

        /*
         * far[i] = farthest sorted position reachable
         * from i in ONE jump.
         */
        $far = array_fill(0, $n, 0);

        $right = 0;

        for ($i = 0; $i < $n; $i++) {

            if ($right < $i) {
                $right = $i;
            }

            while (
                $right + 1 < $n &&
                $sortedValues[$right + 1] - $sortedValues[$i] <= $maxDiff
            ) {
                $right++;
            }

            $far[$i] = $right;
        }

        /*
         * Binary lifting.
         *
         * up[k][i] =
         * position reached after 2^k greedy jumps from i.
         */
        $LOG = 1;

        while ((1 << $LOG) <= $n) {
            $LOG++;
        }

        $up = [];

        $up[0] = $far;

        for ($k = 1; $k < $LOG; $k++) {

            $prev = $up[$k - 1];
            $cur = array_fill(0, $n, 0);

            for ($i = 0; $i < $n; $i++) {
                $cur[$i] = $prev[$prev[$i]];
            }

            $up[$k] = $cur;
        }

        /*
         * Answer queries.
         */
        $answer = [];

        foreach ($queries as $query) {

            $u = $query[0];
            $v = $query[1];

            $a = $position[$u];
            $b = $position[$v];

            /*
             * We always move from smaller sorted position
             * to larger sorted position.
             */
            if ($a > $b) {
                $tmp = $a;
                $a = $b;
                $b = $tmp;
            }

            /*
             * Same node.
             */
            if ($a === $b) {
                $answer[] = 0;
                continue;
            }

            /*
             * Direct edge.
             */
            if ($far[$a] >= $b) {
                $answer[] = 1;
                continue;
            }

            /*
             * Greedily make the largest possible jumps
             * while staying strictly before b.
             */
            $current = $a;
            $steps = 0;

            for ($k = $LOG - 1; $k >= 0; $k--) {

                $next = $up[$k][$current];

                if ($next < $b) {
                    $current = $next;
                    $steps += (1 << $k);
                }
            }

            /*
             * One final jump must reach b.
             *
             * If it cannot, there is no path.
             */
            if ($far[$current] >= $b) {
                $answer[] = $steps + 1;
            } else {
                $answer[] = -1;
            }
        }

        return $answer;
    }
}
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
- [3532. Path Existence Queries in a Graph I](../../3501-4000/3838-path-existence-queries-in-a-graph-i/)
- [3841. Palindromic Path Queries in a Tree](../../4001-4500/4209-palindromic-path-queries-in-a-tree/)
- [1971. Find if Path Exists in Graph](../../2001-2500/2121-find-if-path-exists-in-graph/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/)
