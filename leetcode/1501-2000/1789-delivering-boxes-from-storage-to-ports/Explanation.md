# LeetCode 1687: Delivering Boxes from Storage to Ports

**LeetCode Problem #1687 — Delivering Boxes from Storage to Ports**
Solve LeetCode Delivering Boxes from Storage to Ports using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Delivering Boxes from Storage to Ports |
| LeetCode | #1687 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You have the task of delivering some boxes from storage to their ports using only one ship. However, this ship has a **limit** on the **number of boxes** and the **total weight** that it can carry.

You are given an array `boxes`, where `boxes[i] = [ports_​​i​, weight_i]`, and three integers `portsCount`, `maxBoxes`, and `maxWeight`.

`ports_​​i` is the port where you need to deliver the `i^th` box and `weights_i` is the weight of the `i^th` box. 
 `portsCount` is the number of ports. 
 `maxBoxes` and `maxWeight` are the respective box and weight limits of the ship.

The boxes need to be delivered **in the order they are given**. The ship will follow these steps:

The ship will take some number of boxes from the `boxes` queue, not violating the `maxBoxes` and `maxWeight` constraints. 
 For each loaded box **in order**, the ship will make a **trip** to the port the box needs to be delivered to and deliver it. If the ship is already at the correct port, no **trip** is needed, and the box can immediately be delivered. 
 The ship then makes a return **trip** to storage to take more boxes from the queue.

The ship must end at storage after all the boxes have been delivered.

Return *the **minimum** number of **trips** the ship needs to make to deliver all boxes to their respective ports.*

## Constraints
- `1 <= boxes.length <= 10^5`
- `1 <= portsCount, maxBoxes, maxWeight <= 10^5`
- `1 <= ports_​​i <= portsCount`
- `1 <= weights_i <= maxWeight`

## Examples
### Example 1
- **Input:** `boxes = [[1,1],[2,1],[1,1]], portsCount = 2, maxBoxes = 3, maxWeight = 3`
- **Output:** `4`
- **Explanation:** The optimal strategy is as follows: 
- The ship takes all the boxes in the queue, goes to port 1, then port 2, then port 1 again, then returns to storage. 4 trips.
So the total number of trips is 4.
Note that the first and third boxes cannot be delivered together because the boxes need to be delivered in order (i.e. the second box needs to be delivered at port 2 before the third box).

### Example 2
- **Input:** `boxes = [[1,2],[3,3],[3,1],[3,1],[2,4]], portsCount = 3, maxBoxes = 3, maxWeight = 6`
- **Output:** `6`
- **Explanation:** The optimal strategy is as follows: 
- The ship takes the first box, goes to port 1, then returns to storage. 2 trips.
- The ship takes the second, third and fourth boxes, goes to port 3, then returns to storage. 2 trips.
- The ship takes the fifth box, goes to port 2, then returns to storage. 2 trips.
So the total number of trips is 2 + 2 + 2 = 6.

### Example 3
- **Input:** `boxes = [[1,4],[1,2],[2,1],[2,1],[3,2],[3,4]], portsCount = 3, maxBoxes = 6, maxWeight = 7`
- **Output:** `6`
- **Explanation:** The optimal strategy is as follows:
- The ship takes the first and second boxes, goes to port 1, then returns to storage. 2 trips.
- The ship takes the third and fourth boxes, goes to port 2, then returns to storage. 2 trips.
- The ship takes the fifth and sixth boxes, goes to port 3, then returns to storage. 2 trips.
So the total number of trips is 2 + 2 + 2 = 6.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Delivering Boxes from Storage to Ports**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `boxes = [[1,1],[2,1],[1,1]], portsCount = 2, maxBoxes = 3, maxWeight = 3`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The optimal strategy is as follows: 
- The ship takes all the boxes in the queue, goes to port 1, then port 2, then port 1 again, then returns to storage. 4 trips.
So the total number of trips is 4.
Note that the first and third boxes cannot be delivered together because the boxes need to be delivered in order (i.e. the second box needs to be delivered at port 2 before the third box).

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for DP Table / Array.

## Pattern
**Dynamic Programming**

## Topics
- Dynamic Programming
- Memoization
- State Transition

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
/**
 * @param {number[][]} boxes
 * @param {number} portsCount
 * @param {number} maxBoxes
 * @param {number} maxWeight
 * @return {number}
 */
var boxDelivering = function (boxes, portsCount, maxBoxes, maxWeight) {
    const n = boxes.length;
    const neg = new Array(n).fill(0);   // neg[t] = port changes among boxes 0..t
    const W = new Array(n + 1).fill(0); // prefix weights
    for (let t = 0; t < n; t++) {
        W[t + 1] = W[t] + boxes[t][1];
        if (t >= 1) neg[t] = neg[t - 1] + (boxes[t][0] !== boxes[t - 1][0] ? 1 : 0);
    }

    const dp = new Array(n + 1).fill(0);
    const dq = new Array(n + 1);
    let head = 0, tail = 0;

    for (let i = 1; i <= n; i++) {
        const j = i - 1;
        const val = dp[j] - neg[j];
        while (head < tail && dp[dq[tail - 1]] - neg[dq[tail - 1]] >= val) tail--;
        dq[tail++] = j;

        while (i - dq[head] > maxBoxes || W[i] - W[dq[head]] > maxWeight) head++;

        const f = dq[head];
        dp[i] = (dp[f] - neg[f]) + neg[i - 1] + 2;
    }
    return dp[n];
};
```

## Why This Works
By utilizing **Dynamic Programming**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Incorrect base case initialization.
2. Flawed state transition equation.
3. Storing unnecessary state leading to Memory Limit Exceeded (MLE).

## Interview Notes
- **Tests:** Subproblem decomposition, state transition logic, and space optimization.
- **Follow-up:** Can space complexity be reduced from $O(n^2)$ to $O(n)$ or $O(1)$?

## Related Problems
- [1298. Maximum Candies You Can Get from Boxes](../../1001-1500/1424-maximum-candies-you-can-get-from-boxes/)
- [546. Remove Boxes](../../0501-1000/0546-remove-boxes/)
- [1467. Probability of a Two Boxes Having The Same Number of Distinct Balls](../../1501-2000/1577-probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/delivering-boxes-from-storage-to-ports/)
