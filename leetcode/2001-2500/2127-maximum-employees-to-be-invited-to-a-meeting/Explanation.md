# LeetCode 2127: Maximum Employees to Be Invited to a Meeting

**LeetCode Problem #2127 — Maximum Employees to Be Invited to a Meeting**
Solve LeetCode Maximum Employees to Be Invited to a Meeting using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Employees to Be Invited to a Meeting |
| LeetCode | #2127 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A company is organizing a meeting and has a list of `n` employees, waiting to be invited. They have arranged for a large **circular** table, capable of seating **any number** of employees.

The employees are numbered from `0` to `n - 1`. Each employee has a **favorite** person and they will attend the meeting **only if** they can sit next to their favorite person at the table. The favorite person of an employee is **not** themself.

Given a **0-indexed** integer array `favorite`, where `favorite[i]` denotes the favorite person of the `i^th` employee, return *the **maximum number of employees** that can be invited to the meeting*.

## Constraints
- `n == favorite.length`
- `2 <= n <= 10^5`
- `0 <= favorite[i] <= n - 1`
- `favorite[i] != i`

## Examples
### Example 1
- **Input:** `favorite = [2,2,1,2]`
- **Output:** `3`
- **Explanation:** The above figure shows how the company can invite employees 0, 1, and 2, and seat them at the round table.
All employees cannot be invited because employee 2 cannot sit beside employees 0, 1, and 3, simultaneously.
Note that the company can also invite employees 1, 2, and 3, and give them their desired seats.
The maximum number of employees that can be invited to the meeting is 3.

### Example 2
- **Input:** `favorite = [1,2,0]`
- **Output:** `3`
- **Explanation:** Each employee is the favorite person of at least one other employee, and the only way the company can invite them is if they invite every employee.
The seating arrangement will be the same as that in the figure given in

### Example 3
- **Input:** `favorite = [3,0,1,4,1]`
- **Output:** `4`
- **Explanation:** The above figure shows how the company will invite employees 0, 1, 3, and 4, and seat them at the round table.
Employee 2 cannot be invited because the two spots next to their favorite employee 1 are taken.
So the company leaves them out of the meeting.
The maximum number of employees that can be invited to the meeting is 4.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximum Employees to Be Invited to a Meeting**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `favorite = [2,2,1,2]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The above figure shows how the company can invite employees 0, 1, and 2, and seat them at the round table.
All employees cannot be invited because employee 2 cannot sit beside employees 0, 1, and 3, simultaneously.
Note that the company can also invite employees 1, 2, and 3, and give them their desired seats.
The maximum number of employees that can be invited to the meeting is 3.

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
/**
 * @param {number[]} favorite
 * @return {number}
 */
var maximumInvitations = function (favorite) {
    const n = favorite.length;
    const indeg = new Int32Array(n);
    for (let i = 0; i < n; i++) indeg[favorite[i]]++;

    const depth = new Int32Array(n); // longest chain ending at node (excluding itself)
    const queue = [];
    for (let i = 0; i < n; i++) if (indeg[i] === 0) queue.push(i);

    const removed = new Uint8Array(n);
    let head = 0;
    while (head < queue.length) {
        const u = queue[head++];
        removed[u] = 1;
        const v = favorite[u];
        if (depth[u] + 1 > depth[v]) depth[v] = depth[u] + 1;
        if (--indeg[v] === 0) queue.push(v);
    }

    let maxCycle = 0, sum2 = 0;
    const seen = new Uint8Array(n);
    for (let i = 0; i < n; i++) {
        if (removed[i] || seen[i]) continue;
        let len = 0, cur = i;
        while (!seen[cur]) {
            seen[cur] = 1;
            len++;
            cur = favorite[cur];
        }
        if (len === 2) {
            const a = i, b = favorite[i];
            sum2 += 2 + depth[a] + depth[b];
        } else if (len > maxCycle) {
            maxCycle = len;
        }
    }
    return Math.max(maxCycle, sum2);
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
- [181. Employees Earning More Than Their Managers](../../0001-0500/0181-employees-earning-more-than-their-managers/)
- [627. Swap Sex of Employees](../../0501-1000/0627-swap-sex-of-employees/)
- [1075. Project Employees I](../../1001-1500/1075-project-employees-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/)
