# LeetCode 2286: Booking Concert Tickets in Groups

**LeetCode Problem #2286 — Booking Concert Tickets in Groups**
Solve LeetCode Booking Concert Tickets in Groups using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Booking Concert Tickets in Groups |
| LeetCode | #2286 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A concert hall has `n` rows numbered from `0` to `n - 1`, each with `m` seats, numbered from `0` to `m - 1`. You need to design a ticketing system that can allocate seats in the following cases:

If a group of `k` spectators can sit **together** in a row. 
 If **every** member of a group of `k` spectators can get a seat. They may or **may not** sit together.

Note that the spectators are very picky. Hence:

They will book seats only if each member of their group can get a seat with row number **less than or equal** to `maxRow`. `maxRow` can **vary** from group to group. 
 In case there are multiple rows to choose from, the row with the **smallest** number is chosen. If there are multiple seats to choose in the same row, the seat with the **smallest** number is chosen.

Implement the `BookMyShow` class:

`BookMyShow(int n, int m)` Initializes the object with `n` as number of rows and `m` as number of seats per row. 
 `int[] gather(int k, int maxRow)` Returns an array of length `2` denoting the row and seat number (respectively) of the **first seat** being allocated to the `k` members of the group, who must sit **together**. In other words, it returns the smallest possible `r` and `c` such that all `[c, c + k - 1]` seats are valid and empty in row `r`, and `r <= maxRow`. Returns `[]` in case it is **not possible** to allocate seats to the group. 
 `boolean scatter(int k, int maxRow)` Returns `true` if all `k` members of the group can be allocated seats in rows `0` to `maxRow`, who may or **may not** sit together. If the seats can be allocated, it allocates `k` seats to the group with the **smallest** row numbers, and the smallest possible seat numbers in each row. Otherwise, returns `false`.

## Constraints
- `1 <= n <= 5 * 10^4`
- `1 <= m, k <= 10^9`
- `0 <= maxRow <= n - 1`
- At most `5 * 10^4` calls **in total** will be made to `gather` and `scatter`.

## Examples
### Example 1
- **Input:** `["BookMyShow", "gather", "gather", "scatter", "scatter"]
[[2, 5], [4, 0], [2, 0], [5, 1], [5, 1]]`
- **Output:** `[null, [0, 0], [], true, false]`
- **Explanation:** BookMyShow bms = new BookMyShow(2, 5); // There are 2 rows with 5 seats each 
bms.gather(4, 0); // return [0, 0]
 // The group books seats [0, 3] of row 0. 
bms.gather(2, 0); // return []
 // There is only 1 seat left in row 0,
 // so it is not possible to book 2 consecutive seats. 
bms.scatter(5, 1); // return True
 // The group books seat 4 of row 0 and seats [0, 3] of row 1. 
bms.scatter(5, 1); // return False
 // There is only one seat left in the hall.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Booking Concert Tickets in Groups**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["BookMyShow", "gather", "gather", "scatter", "scatter"]
[[2, 5], [4, 0], [2, 0], [5, 1], [5, 1]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, [0, 0], [], true, false]`.
4. **Verification:** BookMyShow bms = new BookMyShow(2, 5); // There are 2 rows with 5 seats each 
bms.gather(4, 0); // return [0, 0]
 // The group books seats [0, 3] of row 0. 
bms.gather(2, 0); // return []
 // There is only 1 seat left in row 0,
 // so it is not possible to book 2 consecutive seats. 
bms.scatter(5, 1); // return True
 // The group books seat 4 of row 0 and seats [0, 3] of row 1. 
bms.scatter(5, 1); // return False
 // There is only one seat left in the hall.

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
var BookMyShow = function(n, m) {
    this.n = n;
    this.m = m;
    this.remaining = new Array(n).fill(m);

    this.sumTree = new Array(4 * n).fill(0);
    this.maxTree = new Array(4 * n).fill(0);

    const build = (node, start, end) => {
        if (start === end) {
            this.sumTree[node] = m;
            this.maxTree[node] = m;
            return;
        }

        const mid = Math.floor((start + end) / 2);
        build(node * 2, start, mid);
        build(node * 2 + 1, mid + 1, end);
        this.pull(node);
    };

    this.pull = (node) => {
        this.sumTree[node] =
            this.sumTree[node * 2] + this.sumTree[node * 2 + 1];

        this.maxTree[node] = Math.max(
            this.maxTree[node * 2],
            this.maxTree[node * 2 + 1]
        );
    };

    this.update = (node, start, end, index, value) => {
        if (start === end) {
            this.sumTree[node] = value;
            this.maxTree[node] = value;
            return;
        }

        const mid = Math.floor((start + end) / 2);

        if (index <= mid) {
            this.update(node * 2, start, mid, index, value);
        } else {
            this.update(node * 2 + 1, mid + 1, end, index, value);
        }

        this.pull(node);
    };

    this.querySum = (node, start, end, left, right) => {
        if (right < start || end < left) return 0;

        if (left <= start && end <= right) {
            return this.sumTree[node];
        }

        const mid = Math.floor((start + end) / 2);

        return (
            this.querySum(node * 2, start, mid, left, right) +
            this.querySum(node * 2 + 1, mid + 1, end, left, right)
        );
    };

    this.findRow = (node, start, end, maxRow, k) => {
        if (start > maxRow || this.maxTree[node] < k) {
            return -1;
        }

        if (start === end) return start;

        const mid = Math.floor((start + end) / 2);

        let row = this.findRow(
            node * 2, start, mid, maxRow, k
        );

        if (row !== -1) return row;

        return this.findRow(
            node * 2 + 1, mid + 1, end, maxRow, k
        );
    };

    this.consume = (node, start, end, k) => {
        if (start === end) {
            const taken = Math.min(k, this.remaining[start]);
            this.remaining[start] -= taken;
            this.update(1, 0, this.n - 1, start, this.remaining[start]);
            return k - taken;
        }

        const mid = Math.floor((start + end) / 2);
        let leftOver = k;

        const leftSum = this.sumTree[node * 2];

        if (leftSum > 0) {
            leftOver = this.consume(
                node * 2, start, mid, leftOver
            );
        }

        if (leftOver > 0) {
            leftOver = this.consume(
                node * 2 + 1, mid + 1, end, leftOver
            );
        }

        this.pull(node);
        return leftOver;
    };

    build(1, 0, n - 1);
};

BookMyShow.prototype.gather = function(k, maxRow) {
    const row = this.findRow(1, 0, this.n - 1, maxRow, k);

    if (row === -1) return [];

    const seat = this.m - this.remaining[row];

    this.remaining[row] -= k;
    this.update(1, 0, this.n - 1, row, this.remaining[row]);

    return [row, seat];
};

BookMyShow.prototype.scatter = function(k, maxRow) {
    const available = this.querySum(
        1, 0, this.n - 1, 0, maxRow
    );

    if (available < k) return false;

    this.consume(1, 0, maxRow, k);

    return true;
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
- [983. Minimum Cost For Tickets](../../0501-1000/0983-minimum-cost-for-tickets/)
- [2073. Time Needed to Buy Tickets](../../2001-2500/2073-time-needed-to-buy-tickets/)
- [830. Positions of Large Groups](../../0501-1000/0830-positions-of-large-groups/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/booking-concert-tickets-in-groups/)
