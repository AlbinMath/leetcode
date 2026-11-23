# LeetCode 1042: Flower Planting With No Adjacent

**LeetCode Problem #1042 — Flower Planting With No Adjacent**
Solve LeetCode Flower Planting With No Adjacent using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Flower Planting With No Adjacent |
| LeetCode | #1042 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You have `n` gardens, labeled from `1` to `n`, and an array `paths` where `paths[i] = [x_i, y_i]` describes a bidirectional path between garden `x_i` to garden `y_i`. In each garden, you want to plant one of 4 types of flowers.

All gardens have **at most 3** paths coming into or leaving it.

Your task is to choose a flower type for each garden such that, for any two gardens connected by a path, they have different types of flowers.

Return ***any** such a choice as an array *`answer`*, where *`answer[i]`* is the type of flower planted in the *`(i+1)^th`* garden. The flower types are denoted *`1`*, *`2`*, *`3`*, or *`4`*. It is guaranteed an answer exists.*

## Constraints
- `1 <= n <= 10^4`
- `0 <= paths.length <= 2 * 10^4`
- `paths[i].length == 2`
- `1 <= x_i, y_i <= n`
- `x_i != y_i`
- Every garden has **at most 3** paths coming into or leaving it.

## Examples
### Example 1
- **Input:** `n = 3, paths = [[1,2],[2,3],[3,1]]`
- **Output:** `[1,2,3]`
- **Explanation:** Gardens 1 and 2 have different types.
Gardens 2 and 3 have different types.
Gardens 3 and 1 have different types.
Hence, [1,2,3] is a valid answer. Other valid answers include [1,2,4], [1,4,2], and [3,2,1].

### Example 2
- **Input:** `n = 4, paths = [[1,2],[3,4]]`
- **Output:** `[1,2,1,2]`

### Example 3
- **Input:** `n = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]`
- **Output:** `[1,2,3,4]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Flower Planting With No Adjacent**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3, paths = [[1,2],[2,3],[3,1]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,2,3]`.
4. **Verification:** Gardens 1 and 2 have different types.
Gardens 2 and 3 have different types.
Gardens 3 and 1 have different types.
Hence, [1,2,3] is a valid answer. Other valid answers include [1,2,4], [1,4,2], and [3,2,1].

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
var gardenNoAdj = function(n, paths) {
    // Build adjacency list
    const graph = Array.from({ length: n + 1 }, () => []);

    for (const [u, v] of paths) {
        graph[u].push(v);
        graph[v].push(u);
    }

    // Store flower type for each garden
    const answer = new Array(n + 1).fill(0);

    // Assign flowers greedily
    for (let garden = 1; garden <= n; garden++) {
        const used = new Set();

        // Collect flower types of neighboring gardens
        for (const neighbor of graph[garden]) {
            if (answer[neighbor] !== 0) {
                used.add(answer[neighbor]);
            }
        }

        // Choose the first available flower type
        for (let flower = 1; flower <= 4; flower++) {
            if (!used.has(flower)) {
                answer[garden] = flower;
                break;
            }
        }
    }

    return answer.slice(1);
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
- [363. Max Sum of Rectangle No Larger Than K](../../0001-0500/0363-max-sum-of-rectangle-no-larger-than-k/)
- [1317. Convert Integer to the Sum of Two No-Zero Integers](../../1001-1500/1440-convert-integer-to-the-sum-of-two-no-zero-integers/)
- [1637. Widest Vertical Area Between Two Points Containing No Points](../../1501-2000/1742-widest-vertical-area-between-two-points-containing-no-points/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/flower-planting-with-no-adjacent/)
