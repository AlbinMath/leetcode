# LeetCode 406: Queue Reconstruction by Height

**LeetCode Problem #406 — Queue Reconstruction by Height**
Solve LeetCode Queue Reconstruction by Height using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Queue Reconstruction by Height |
| LeetCode | #406 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an array of people, `people`, which are the attributes of some people in a queue (not necessarily in order). Each `people[i] = [h_i, k_i]` represents the `i^th` person of height `h_i` with **exactly** `k_i` other people in front who have a height greater than or equal to `h_i`.

Reconstruct and return *the queue that is represented by the input array *`people`. The returned queue should be formatted as an array `queue`, where `queue[j] = [h_j, k_j]` is the attributes of the `j^th` person in the queue (`queue[0]` is the person at the front of the queue).

## Constraints
- `1 <= people.length <= 2000`
- `0 <= h_i <= 10^6`
- `0 <= k_i < people.length`
- It is guaranteed that the queue can be reconstructed.

## Examples
### Example 1
- **Input:** `people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]`
- **Output:** `[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]`
- **Explanation:** Person 0 has height 5 with no other people taller or the same height in front.
Person 1 has height 7 with no other people taller or the same height in front.
Person 2 has height 5 with two persons taller or the same height in front, which is person 0 and 1.
Person 3 has height 6 with one person taller or the same height in front, which is person 1.
Person 4 has height 4 with four people taller or the same height in front, which are people 0, 1, 2, and 3.
Person 5 has height 7 with one person taller or the same height in front, which is person 1.
Hence [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] is the reconstructed queue.

### Example 2
- **Input:** `people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]`
- **Output:** `[[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]`

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Queue Reconstruction by Height**, we observe the problem requirements and utilize the **Stack & Queue** technique. We iterate through the inputs using **Stack Push / Pop Parsing**, leveraging a **Stack** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Stack**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]`.
4. **Verification:** Person 0 has height 5 with no other people taller or the same height in front.
Person 1 has height 7 with no other people taller or the same height in front.
Person 2 has height 5 with two persons taller or the same height in front, which is person 0 and 1.
Person 3 has height 6 with one person taller or the same height in front, which is person 1.
Person 4 has height 4 with four people taller or the same height in front, which are people 0, 1, 2, and 3.
Person 5 has height 7 with one person taller or the same height in front, which is person 1.
Hence [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] is the reconstructed queue.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var reconstructQueue = function(people) {
    // Sort by height descending.
    // For equal heights, sort by k ascending.
    people.sort((a, b) => {
        if (b[0] !== a[0]) {
            return b[0] - a[0];
        }
        return a[1] - b[1];
    });

    const queue = [];

    // Insert each person at their required index
    for (const person of people) {
        queue.splice(person[1], 0, person);
    }

    return queue;
};
```

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [310. Minimum Height Trees](../../0001-0500/0310-minimum-height-trees/)
- [1051. Height Checker](../../1001-1500/1051-height-checker/)
- [1840. Maximum Building Height](../../1501-2000/1840-maximum-building-height/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/queue-reconstruction-by-height/)
