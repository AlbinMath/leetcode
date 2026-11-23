# LeetCode 1583: Count Unhappy Friends

**LeetCode Problem #1583 — Count Unhappy Friends**
Solve LeetCode Count Unhappy Friends using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Unhappy Friends |
| LeetCode | #1583 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a list of `preferences` for `n` friends, where `n` is always **even**.

For each person `i`, `preferences[i]` contains a list of friends **sorted** in the **order of preference**. In other words, a friend earlier in the list is more preferred than a friend later in the list. Friends in each list are denoted by integers from `0` to `n-1`.

All the friends are divided into pairs. The pairings are given in a list `pairs`, where `pairs[i] = [x_i, y_i]` denotes `x_i` is paired with `y_i` and `y_i` is paired with `x_i`.

However, this pairing may cause some of the friends to be unhappy. A friend `x` is unhappy if `x` is paired with `y` and there exists a friend `u` who is paired with `v` but:

`x` prefers `u` over `y`, and 
 `u` prefers `x` over `v`.

Return *the number of unhappy friends*.

## Constraints
- `2 <= n <= 500`
- `n` is even.
- `preferences.length == n`
- `preferences[i].length == n - 1`
- `0 <= preferences[i][j] <= n - 1`
- `preferences[i]` does not contain `i`.
- All values in `preferences[i]` are unique.
- `pairs.length == n/2`
- `pairs[i].length == 2`
- `x_i != y_i`
- `0 <= x_i, y_i <= n - 1`
- Each person is contained in **exactly one** pair.

## Examples
### Example 1
- **Input:** `n = 4, preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]], pairs = [[0, 1], [2, 3]]`
- **Output:** `2`
- **Explanation:** Friend 1 is unhappy because:
- 1 is paired with 0 but prefers 3 over 0, and
- 3 prefers 1 over 2.
Friend 3 is unhappy because:
- 3 is paired with 2 but prefers 1 over 2, and
- 1 prefers 3 over 0.
Friends 0 and 2 are happy.

### Example 2
- **Input:** `n = 2, preferences = [[1], [0]], pairs = [[1, 0]]`
- **Output:** `0`
- **Explanation:** Both friends 0 and 1 are happy.

### Example 3
- **Input:** `n = 4, preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]], pairs = [[1, 3], [0, 2]]`
- **Output:** `4`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Count Unhappy Friends**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 4, preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]], pairs = [[0, 1], [2, 3]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** Friend 1 is unhappy because:
- 1 is paired with 0 but prefers 3 over 0, and
- 3 prefers 1 over 2.
Friend 3 is unhappy because:
- 3 is paired with 2 but prefers 1 over 2, and
- 1 prefers 3 over 0.
Friends 0 and 2 are happy.

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
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        rank = [[0] * n for _ in range(n)]
        for i in range(n):
            for pos, j in enumerate(preferences[i]):
                rank[i][j] = pos

        partner = [0] * n
        for x, y in pairs:
            partner[x] = y
            partner[y] = x

        unhappy = 0
        for x in range(n):
            y = partner[x]
            for u in preferences[x]:
                if u == y:
                    break
                v = partner[u]
                if rank[u][x] < rank[u][v]:
                    unhappy += 1
                    break
        return unhappy
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
- [38. Count and Say](../../0001-0500/0038-count-and-say/)
- [204. Count Primes](../../0001-0500/0204-count-primes/)
- [222. Count Complete Tree Nodes](../../0001-0500/0222-count-complete-tree-nodes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-unhappy-friends/)
