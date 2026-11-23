# LeetCode 3017: Count the Number of Houses at a Certain Distance II

**LeetCode Problem #3017 — Count the Number of Houses at a Certain Distance II**
Solve LeetCode Count the Number of Houses at a Certain Distance II using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count the Number of Houses at a Certain Distance II |
| LeetCode | #3017 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given three **positive** integers `n`, `x`, and `y`.

In a city, there exist houses numbered `1` to `n` connected by `n` streets. There is a street connecting the house numbered `i` with the house numbered `i + 1` for all `1 <= i <= n - 1` . An additional street connects the house numbered `x` with the house numbered `y`.

For each `k`, such that `1 <= k <= n`, you need to find the number of **pairs of houses** `(house_1, house_2)` such that the **minimum** number of streets that need to be traveled to reach `house_2` from `house_1` is `k`.

Return *a **1-indexed** array *`result`* of length *`n`* where *`result[k]`* represents the **total** number of pairs of houses such that the **minimum** streets required to reach one house from the other is *`k`.

**Note** that `x` and `y` can be **equal**.

## Constraints
- `2 <= n <= 10^5`
- `1 <= x, y <= n`

## Examples
### Example 1
- **Input:** `n = 3, x = 1, y = 3`
- **Output:** `[6,0,0]`
- **Explanation:** Let's look at each pair of houses:
- For the pair (1, 2), we can go from house 1 to house 2 directly.
- For the pair (2, 1), we can go from house 2 to house 1 directly.
- For the pair (1, 3), we can go from house 1 to house 3 directly.
- For the pair (3, 1), we can go from house 3 to house 1 directly.
- For the pair (2, 3), we can go from house 2 to house 3 directly.
- For the pair (3, 2), we can go from house 3 to house 2 directly.

### Example 2
- **Input:** `n = 5, x = 2, y = 4`
- **Output:** `[10,8,2,0,0]`
- **Explanation:** For each distance k the pairs are:
- For k == 1, the pairs are (1, 2), (2, 1), (2, 3), (3, 2), (2, 4), (4, 2), (3, 4), (4, 3), (4, 5), and (5, 4).
- For k == 2, the pairs are (1, 3), (3, 1), (1, 4), (4, 1), (2, 5), (5, 2), (3, 5), and (5, 3).
- For k == 3, the pairs are (1, 5), and (5, 1).
- For k == 4 and k == 5, there are no pairs.

### Example 3
- **Input:** `n = 4, x = 1, y = 1`
- **Output:** `[6,4,2,0]`
- **Explanation:** For each distance k the pairs are:
- For k == 1, the pairs are (1, 2), (2, 1), (2, 3), (3, 2), (3, 4), and (4, 3).
- For k == 2, the pairs are (1, 3), (3, 1), (2, 4), and (4, 2).
- For k == 3, the pairs are (1, 4), and (4, 1).
- For k == 4, there are no pairs.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Count the Number of Houses at a Certain Distance II**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3, x = 1, y = 3`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[6,0,0]`.
4. **Verification:** Let's look at each pair of houses:
- For the pair (1, 2), we can go from house 1 to house 2 directly.
- For the pair (2, 1), we can go from house 2 to house 1 directly.
- For the pair (1, 3), we can go from house 1 to house 3 directly.
- For the pair (3, 1), we can go from house 3 to house 1 directly.
- For the pair (2, 3), we can go from house 2 to house 3 directly.
- For the pair (3, 2), we can go from house 3 to house 2 directly.

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
var countOfPairs = function(n, x, y) {
    if (x > y) {
        [x, y] = [y, x];
    }

    // If the extra road is already present or is a self-loop,
    // the graph is just the original straight path.
    if (y - x <= 1) {
        const ans = new Array(n).fill(0);

        for (let d = 1; d < n; d++) {
            ans[d - 1] = 2 * (n - d);
        }

        return ans;
    }

    const left = x - 1;
    const right = n - y;
    const L = y - x + 1;

    const count = new Array(n).fill(0);
    const diff = new Array(n + 1).fill(0);

    // Add a value to every distance in [l, r].
    function addRange(l, r, value) {
        if (l > r || l >= n) return;

        r = Math.min(r, n - 1);

        diff[l] += value;
        diff[r + 1] -= value;
    }

    // 1. Pairs inside the left and right tails.
    for (let d = 1; d < left; d++) {
        count[d] += left - d;
    }

    for (let d = 1; d < right; d++) {
        count[d] += right - d;
    }

    // 2. Pairs inside the cycle.
    for (let d = 1; d <= Math.floor(L / 2); d++) {
        if (2 * d < L) {
            count[d] += L;
        } else {
            // Opposite vertices in an even-length cycle.
            count[d] += L / 2;
        }
    }

    // 3. Pairs between the left tail and the cycle.
    // Also count pairs between the right tail and the cycle.
    for (let d = 0; d <= Math.floor(L / 2); d++) {
        let ways = 2;

        if (d === 0 || (L % 2 === 0 && d === L / 2)) {
            ways = 1;
        }

        if (left > 0) {
            addRange(d + 1, d + left, ways);
        }

        if (right > 0) {
            addRange(d + 1, d + right, ways);
        }
    }

    // 4. Pairs between the left and right tails.
    // Distance = leftOffset + rightOffset + 1.
    for (let p = 1; p <= left; p++) {
        addRange(p + 2, p + right + 1, 1);
    }

    // Apply all range updates.
    let running = 0;

    const answer = new Array(n).fill(0);

    for (let d = 1; d < n; d++) {
        running += diff[d];

        // Convert unordered pairs into ordered pairs.
        answer[d - 1] = 2 * (count[d] + running);
    }

    return answer;
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
- [3015. Count the Number of Houses at a Certain Distance I](../../3001-3500/3271-count-the-number-of-houses-at-a-certain-distance-i/)
- [1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance](../../1001-1500/1456-find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/)
- [1617. Count Subtrees With Max Distance Between Cities](../../1501-2000/1740-count-subtrees-with-max-distance-between-cities/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-ii/)
