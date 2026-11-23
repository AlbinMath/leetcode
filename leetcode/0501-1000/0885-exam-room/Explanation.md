# LeetCode 855: Exam Room

**LeetCode Problem #855 — Exam Room**
Solve LeetCode Exam Room using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Exam Room |
| LeetCode | #855 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is an exam room with `n` seats in a single row labeled from `0` to `n - 1`.

When a student enters the room, they must sit in the seat that maximizes the distance to the closest person. If there are multiple such seats, they sit in the seat with the lowest number. If no one is in the room, then the student sits at seat number `0`.

Design a class that simulates the mentioned exam room.

Implement the `ExamRoom` class:

`ExamRoom(int n)` Initializes the object of the exam room with the number of the seats `n`. 
 `int seat()` Returns the label of the seat at which the next student will set. 
 `void leave(int p)` Indicates that the student sitting at seat `p` will leave the room. It is guaranteed that there will be a student sitting at seat `p`.

## Constraints
- `1 <= n <= 10^9`
- It is guaranteed that there is a student sitting at seat `p`.
- At most `10^4` calls will be made to `seat` and `leave`.

## Examples
### Example 1
- **Input:** `["ExamRoom", "seat", "seat", "seat", "seat", "leave", "seat"]
[[10], [], [], [], [], [4], []]`
- **Output:** `[null, 0, 9, 4, 2, null, 5]`
- **Explanation:** ExamRoom examRoom = new ExamRoom(10);
examRoom.seat(); // return 0, no one is in the room, then the student sits at seat number 0.
examRoom.seat(); // return 9, the student sits at the last seat number 9.
examRoom.seat(); // return 4, the student sits at the last seat number 4.
examRoom.seat(); // return 2, the student sits at the last seat number 2.
examRoom.leave(4);
examRoom.seat(); // return 5, the student sits at the last seat number 5.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Exam Room**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["ExamRoom", "seat", "seat", "seat", "seat", "leave", "seat"]
[[10], [], [], [], [], [4], []]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, 0, 9, 4, 2, null, 5]`.
4. **Verification:** ExamRoom examRoom = new ExamRoom(10);
examRoom.seat(); // return 0, no one is in the room, then the student sits at seat number 0.
examRoom.seat(); // return 9, the student sits at the last seat number 9.
examRoom.seat(); // return 4, the student sits at the last seat number 4.
examRoom.seat(); // return 2, the student sits at the last seat number 2.
examRoom.leave(4);
examRoom.seat(); // return 5, the student sits at the last seat number 5.

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
var ExamRoom = function(n) {
    this.n = n;
    this.seats = [];
};
ExamRoom.prototype.seat = function() {
    if (this.seats.length === 0) {
        this.seats.push(0);
        return 0;
    }

    let maxDist = this.seats[0];
    let target = 0;
    for (let i = 0; i < this.seats.length - 1; i++) {
        const a = this.seats[i];
        const b = this.seats[i + 1];
        const dist = (b - a) >> 1;
        if (dist > maxDist) {
            maxDist = dist;
            target = a + dist;
        }
    }
    if ((this.n - 1) - this.seats[this.seats.length - 1] > maxDist) {
        target = this.n - 1;
    }
    
    let left = 0;
    let right = this.seats.length;
    while (left < right) {
        const mid = (left + right) >> 1;
        if (this.seats[mid] < target) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    
    this.seats.splice(left, 0, target);
    return target;
};
ExamRoom.prototype.leave = function(p) {
    let left = 0;
    let right = this.seats.length - 1;
    while (left <= right) {
        const mid = (left + right) >> 1;
        if (this.seats[mid] === p) {
            this.seats.splice(mid, 1);
            return;
        } else if (this.seats[mid] < p) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
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
- [1349. Maximum Students Taking Exam](../../1001-1500/1471-maximum-students-taking-exam/)
- [2024. Maximize the Confusion of an Exam](../../2001-2500/2134-maximize-the-confusion-of-an-exam/)
- [3709. Design Exam Scores Tracker](../../4001-4500/4059-design-exam-scores-tracker/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/exam-room/)
