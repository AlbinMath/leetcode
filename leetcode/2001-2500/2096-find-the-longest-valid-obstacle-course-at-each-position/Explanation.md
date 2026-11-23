# LeetCode 1964: Find the Longest Valid Obstacle Course at Each Position

**LeetCode Problem #1964 — Find the Longest Valid Obstacle Course at Each Position**
Solve LeetCode Find the Longest Valid Obstacle Course at Each Position using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Longest Valid Obstacle Course at Each Position |
| LeetCode | #1964 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You want to build some obstacle courses. You are given a **0-indexed** integer array `obstacles` of length `n`, where `obstacles[i]` describes the height of the `i^th` obstacle.

For every index `i` between `0` and `n - 1` (**inclusive**), find the length of the **longest obstacle course** in `obstacles` such that:

You choose any number of obstacles between `0` and `i` **inclusive**. 
 You must include the `i^th` obstacle in the course. 
 You must put the chosen obstacles in the **same order** as they appear in `obstacles`. 
 Every obstacle (except the first) is **taller** than or the **same height** as the obstacle immediately before it.

Return *an array* `ans` *of length* `n`, *where* `ans[i]` *is the length of the **longest obstacle course** for index* `i`* as described above*.

## Constraints
- `n == obstacles.length`
- `1 <= n <= 10^5`
- `1 <= obstacles[i] <= 10^7`

## Examples
### Example 1
- **Input:** `obstacles = [1,2,3,2]`
- **Output:** `[1,2,3,3]`
- **Explanation:** The longest valid obstacle course at each position is:
- i = 0: [ 1 ], [1] has length 1.
- i = 1: [ 1 , 2 ], [1,2] has length 2.
- i = 2: [ 1 , 2 , 3 ], [1,2,3] has length 3.
- i = 3: [ 1 , 2 ,3, 2 ], [1,2,2] has length 3.

### Example 2
- **Input:** `obstacles = [2,2,1]`
- **Output:** `[1,2,1]`
- **Explanation:** The longest valid obstacle course at each position is:
- i = 0: [ 2 ], [2] has length 1.
- i = 1: [ 2 , 2 ], [2,2] has length 2.
- i = 2: [2,2, 1 ], [1] has length 1.

### Example 3
- **Input:** `obstacles = [3,1,5,6,4,2]`
- **Output:** `[1,1,2,3,2,2]`
- **Explanation:** The longest valid obstacle course at each position is:
- i = 0: [ 3 ], [3] has length 1.
- i = 1: [3, 1 ], [1] has length 1.
- i = 2: [ 3 ,1, 5 ], [3,5] has length 2. [1,5] is also valid.
- i = 3: [ 3 ,1, 5 , 6 ], [3,5,6] has length 3. [1,5,6] is also valid.
- i = 4: [ 3 ,1,5,6, 4 ], [3,4] has length 2. [1,4] is also valid.
- i = 5: [3, 1 ,5,6,4, 2 ], [1,2] has length 2.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Find the Longest Valid Obstacle Course at Each Position**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `obstacles = [1,2,3,2]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,2,3,3]`.
4. **Verification:** The longest valid obstacle course at each position is:
- i = 0: [ 1 ], [1] has length 1.
- i = 1: [ 1 , 2 ], [1,2] has length 2.
- i = 2: [ 1 , 2 , 3 ], [1,2,3] has length 3.
- i = 3: [ 1 , 2 ,3, 2 ], [1,2,2] has length 3.

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
var longestObstacleCourseAtEachPosition = function(obstacles) {
    const tails = [];
    const ans = [];

    for (const height of obstacles) {
        let left = 0;
        let right = tails.length;

        // Find the first tails element > height
        while (left < right) {
            const mid = Math.floor((left + right) / 2);

            if (tails[mid] <= height) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        // Course length ending at this obstacle
        ans.push(left + 1);

        // Extend tails or replace an existing ending height
        if (left === tails.length) {
            tails.push(height);
        } else {
            tails[left] = height;
        }
    }

    return ans;
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
- [32. Longest Valid Parentheses](../../0001-0500/0032-longest-valid-parentheses/)
- [1178. Number of Valid Words for Each Puzzle](../../1001-1500/1282-number-of-valid-words-for-each-puzzle/)
- [1517. Find Users With Valid E-Mails](../../1501-2000/1664-find-users-with-valid-e-mails/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/)
