# LeetCode 1845: Seat Reservation Manager

**LeetCode Problem #1845 — Seat Reservation Manager**
Solve LeetCode Seat Reservation Manager using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Seat Reservation Manager |
| LeetCode | #1845 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Design a system that manages the reservation state of `n` seats that are numbered from `1` to `n`.

Implement the `SeatManager` class:

`SeatManager(int n)` Initializes a `SeatManager` object that will manage `n` seats numbered from `1` to `n`. All seats are initially available. 
 `int reserve()` Fetches the **smallest-numbered** unreserved seat, reserves it, and returns its number. 
 `void unreserve(int seatNumber)` Unreserves the seat with the given `seatNumber`.

## Constraints
- `1 <= n <= 10^5`
- `1 <= seatNumber <= n`
- For each call to `reserve`, it is guaranteed that there will be at least one unreserved seat.
- For each call to `unreserve`, it is guaranteed that `seatNumber` will be reserved.
- At most `10^5` calls **in total** will be made to `reserve` and `unreserve`.

## Examples
### Example 1
- **Input:** `["SeatManager", "reserve", "reserve", "unreserve", "reserve", "reserve", "reserve", "reserve", "unreserve"]
[[5], [], [], [2], [], [], [], [], [5]]`
- **Output:** `[null, 1, 2, null, 2, 3, 4, 5, null]`
- **Explanation:** SeatManager seatManager = new SeatManager(5); // Initializes a SeatManager with 5 seats.
seatManager.reserve(); // All seats are available, so return the lowest numbered seat, which is 1.
seatManager.reserve(); // The available seats are [2,3,4,5], so return the lowest of them, which is 2.
seatManager.unreserve(2); // Unreserve seat 2, so now the available seats are [2,3,4,5].
seatManager.reserve(); // The available seats are [2,3,4,5], so return the lowest of them, which is 2.
seatManager.reserve(); // The available seats are [3,4,5], so return the lowest of them, which is 3.
seatManager.reserve(); // The available seats are [4,5], so return the lowest of them, which is 4.
seatManager.reserve(); // The only available seat is seat 5, so return 5.
seatManager.unreserve(5); // Unreserve seat 5, so now the available seats are [5].

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Seat Reservation Manager**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["SeatManager", "reserve", "reserve", "unreserve", "reserve", "reserve", "reserve", "reserve", "unreserve"]
[[5], [], [], [2], [], [], [], [], [5]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, 1, 2, null, 2, 3, 4, 5, null]`.
4. **Verification:** SeatManager seatManager = new SeatManager(5); // Initializes a SeatManager with 5 seats.
seatManager.reserve(); // All seats are available, so return the lowest numbered seat, which is 1.
seatManager.reserve(); // The available seats are [2,3,4,5], so return the lowest of them, which is 2.
seatManager.unreserve(2); // Unreserve seat 2, so now the available seats are [2,3,4,5].
seatManager.reserve(); // The available seats are [2,3,4,5], so return the lowest of them, which is 2.
seatManager.reserve(); // The available seats are [3,4,5], so return the lowest of them, which is 3.
seatManager.reserve(); // The available seats are [4,5], so return the lowest of them, which is 4.
seatManager.reserve(); // The only available seat is seat 5, so return 5.
seatManager.unreserve(5); // Unreserve seat 5, so now the available seats are [5].

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
var SeatManager = function(n) {
    this.marker = 1;
    this.heap = [];
};
SeatManager.prototype.reserve = function() {
    if (this.heap.length > 0) {
        return this._pop();
    }
    return this.marker++;
};
SeatManager.prototype.unreserve = function(seatNumber) {
    this._push(seatNumber);
};

SeatManager.prototype._push = function(val) {
    this.heap.push(val);
    let i = this.heap.length - 1;
    while (i > 0) {
        const parent = (i - 1) >> 1;
        if (this.heap[parent] <= this.heap[i]) break;
        [this.heap[parent], this.heap[i]] = [this.heap[i], this.heap[parent]];
        i = parent;
    }
};

SeatManager.prototype._pop = function() {
    const top = this.heap[0];
    const last = this.heap.pop();
    if (this.heap.length > 0) {
        this.heap[0] = last;
        let i = 0;
        const len = this.heap.length;
        while (true) {
            let smallest = i;
            const left = (i << 1) + 1;
            const right = (i << 1) + 2;
            if (left < len && this.heap[left] < this.heap[smallest]) smallest = left;
            if (right < len && this.heap[right] < this.heap[smallest]) smallest = right;
            if (smallest === i) break;
            [this.heap[i], this.heap[smallest]] = [this.heap[smallest], this.heap[i]];
            i = smallest;
        }
    }
    return top;
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
- [1227. Airplane Seat Assignment Probability](../../1001-1500/1362-airplane-seat-assignment-probability/)
- [1386. Cinema Seat Allocation](../../1001-1500/1487-cinema-seat-allocation/)
- [2037. Minimum Number of Moves to Seat Everyone](../../2001-2500/2148-minimum-number-of-moves-to-seat-everyone/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/seat-reservation-manager/)
