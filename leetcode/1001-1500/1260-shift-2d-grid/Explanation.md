# LeetCode 1260: Shift 2D Grid

**LeetCode Problem #1260 — Shift 2D Grid**
Solve LeetCode Shift 2D Grid using Racket and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Shift 2D Grid |
| LeetCode | #1260 |
| Difficulty | Easy |
| Language | Racket |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a 2D `grid` of size `m x n` and an integer `k`. You need to shift the `grid` `k` times.

In one shift operation:

Element at `grid[i][j]` moves to `grid[i][j + 1]`. 
 Element at `grid[i][n - 1]` moves to `grid[i + 1][0]`. 
 Element at `grid[m - 1][n - 1]` moves to `grid[0][0]`.

Return the *2D grid* after applying shift operation `k` times.

## Constraints
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m <= 50`
- `1 <= n <= 50`
- `-1000 <= grid[i][j] <= 1000`
- `0 <= k <= 100`

## Examples
### Example 1
- **Input:** `grid` = [[1,2,3],[4,5,6],[7,8,9]], k = 1`
- **Output:** `[[9,1,2],[3,4,5],[6,7,8]]`

### Example 2
- **Input:** `grid` = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4`
- **Output:** `[[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]`

### Example 3
- **Input:** `grid` = [[1,2,3],[4,5,6],[7,8,9]], k = 9`
- **Output:** `[[1,2,3],[4,5,6],[7,8,9]]`

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code (in Racket) uses a **flatten-shift-reshape** approach:
1. **Flatten:** Convert the 2D grid into a 1D list.
2. **Shift:** Compute `shift = k % total` to avoid redundant full rotations. Split the flat list at `total - shift` and swap the two halves (move the last `shift` elements to the front).
3. **Reshape:** Convert the shifted 1D list back into a 2D grid with `m` rows and `n` columns.

Time complexity is $O(M \times N)$ and space complexity is $O(M \times N)$.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `grid` = [[1,2,3],[4,5,6],[7,8,9]], k = 1`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[9,1,2],[3,4,5],[6,7,8]]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Tree / Graph / Grid.

## Pattern
**Tree & Graph**

## Topics
- Tree
- Graph
- DFS
- BFS

## Language
Racket

## Source Code
- [solution.rkt](./solution.rkt)


```racket
(define/contract (shift-grid grid k)
  (-> (listof (listof exact-integer?)) exact-integer?
      (listof (listof exact-integer?)))

  (define m (length grid))
  (define n (length (first grid)))
  (define total (* m n))
  (define shift (modulo k total))

  (define flat (apply append grid))

  (define shifted
    (append
     (drop flat (- total shift))
     (take flat (- total shift))))

  (for/list ([i (in-range m)])
    (take (drop shifted (* i n)) n)))
```

## Why This Works
By utilizing **Tree & Graph**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1559. Detect Cycles in 2D Grid](../../1501-2000/1559-detect-cycles-in-2d-grid/)
- [3311. Construct 2D Grid Matching Graph Layout](../../3001-3500/3311-construct-2d-grid-matching-graph-layout/)
- [3361. Shift Distance Between Two Strings](../../3001-3500/3361-shift-distance-between-two-strings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/shift-2d-grid/)
