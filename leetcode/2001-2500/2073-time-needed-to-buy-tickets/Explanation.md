# LeetCode 2073: Time Needed to Buy Tickets

**LeetCode Problem #2073 — Time Needed to Buy Tickets**
Solve LeetCode Time Needed to Buy Tickets using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Time Needed to Buy Tickets |
| LeetCode | #2073 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There are `n` people in a line queuing to buy tickets, where the `0^th` person is at the **front** of the line and the `(n - 1)^th` person is at the **back** of the line.

You are given a **0-indexed** integer array `tickets` of length `n` where the number of tickets that the `i^th` person would like to buy is `tickets[i]`.

Each person takes **exactly 1 second** to buy a ticket. A person can only buy **1 ticket at a time** and has to go back to **the end** of the line (which happens **instantaneously**) in order to buy more tickets. If a person does not have any tickets left to buy, the person will **leave **the line.

Return the **time taken** for the person **initially** at position **k**** **(0-indexed) to finish buying tickets.

## Constraints
- `n == tickets.length`
- `1 <= n <= 100`
- `1 <= tickets[i] <= 100`
- `0 <= k < n`

## Examples
### Example 1
- **Input:** `tickets = [2,3,2], k = 2`
- **Output:** `6`
- **Explanation:** The queue starts as [2,3, 2 ], where the kth person is underlined. 
 After the person at the front has bought a ticket, the queue becomes [3, 2 ,1] at 1 second. 
 Continuing this process, the queue becomes [ 2 ,1,2] at 2 seconds. 
 Continuing this process, the queue becomes [1,2, 1 ] at 3 seconds. 
 Continuing this process, the queue becomes [2, 1 ] at 4 seconds. Note: the person at the front left the queue. 
 Continuing this process, the queue becomes [ 1 ,1] at 5 seconds. 
 Continuing this process, the queue becomes [1] at 6 seconds. The kth person has bought all their tickets, so return 6.

### Example 2
- **Input:** `tickets = [5,1,1,1], k = 0`
- **Output:** `8`
- **Explanation:** The queue starts as [ 5 ,1,1,1], where the kth person is underlined. 
 After the person at the front has bought a ticket, the queue becomes [1,1,1, 4 ] at 1 second. 
 Continuing this process for 3 seconds, the queue becomes [ 4] at 4 seconds. 
 Continuing this process for 4 seconds, the queue becomes [] at 8 seconds. The kth person has bought all their tickets, so return 8.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Time Needed to Buy Tickets**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `tickets = [2,3,2], k = 2`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** The queue starts as [2,3, 2 ], where the kth person is underlined. 
 After the person at the front has bought a ticket, the queue becomes [3, 2 ,1] at 1 second. 
 Continuing this process, the queue becomes [ 2 ,1,2] at 2 seconds. 
 Continuing this process, the queue becomes [1,2, 1 ] at 3 seconds. 
 Continuing this process, the queue becomes [2, 1 ] at 4 seconds. Note: the person at the front left the queue. 
 Continuing this process, the queue becomes [ 1 ,1] at 5 seconds. 
 Continuing this process, the queue becomes [1] at 6 seconds. The kth person has bought all their tickets, so return 6.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var timeRequiredToBuy = function(tickets, k) {
    let time = 0;

    for (let i = 0; i < tickets.length; i++) {
        if (i <= k) {
            time += Math.min(tickets[i], tickets[k]);
        } else {
            time += Math.min(tickets[i], tickets[k] - 1);
        }
    }

    return time;
};
```

## Why This Works
By utilizing **Math & Logic**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1376. Time Needed to Inform All Employees](../../1001-1500/1376-time-needed-to-inform-all-employees/)
- [2380. Time Needed to Rearrange a Binary String](../../2001-2500/2380-time-needed-to-rearrange-a-binary-string/)
- [121. Best Time to Buy and Sell Stock](../../0001-0500/0121-best-time-to-buy-and-sell-stock/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/time-needed-to-buy-tickets/)
