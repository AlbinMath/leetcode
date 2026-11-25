# LeetCode 746: Min Cost Climbing Stairs

**LeetCode Problem #746 — Min Cost Climbing Stairs**
Solve LeetCode Min Cost Climbing Stairs using JavaScript, Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Min Cost Climbing Stairs |
| LeetCode | #746 |
| Difficulty | Easy |
| Language | JavaScript, Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `cost` where `cost[i]` is the cost of `i^th` step on a staircase.

Once you pay the cost, you can either climb **one** or **two** steps.

You can either start from the step with index 0, or the step with index 1.

Return the **minimum** cost to reach the top of the staircase, which is the position just past the last step (index `cost.length`).

## Constraints
- `2 <= cost.length <= 1000`
- `0 <= cost[i] <= 999`

## Examples
### Example 1
- **Input:** `cost = [10, 15 ,20]`
- **Output:** `15`
- **Explanation:** You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

### Example 2
- **Input:** `cost = [ 1 ,100, 1 ,1, 1 ,100, 1 , 1 ,100, 1 ]`
- **Output:** `6`
- **Explanation:** You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Min Cost Climbing Stairs**, we observe the problem requirements and utilize the **Stack & Queue** technique. We iterate through the inputs using **Stack Push / Pop Parsing**, leveraging a **Stack** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Stack**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `cost = [10, 15 ,20]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `15`.
4. **Verification:** You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### JavaScript
```javascript
var minCostClimbingStairs = function(cost) {
    let prev2 = 0;
    let prev1 = 0;

    for (let i = 2; i <= cost.length; i++) {
        const current = Math.min(
            prev1 + cost[i - 1],
            prev2 + cost[i - 2]
        );

        prev2 = prev1;
        prev1 = current;
    }

    return prev1;
};
```

### Python
```python
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        prev2 = 0
        prev1 = 0

        for i in range(2, len(cost) + 1):
            current = min(
                prev1 + cost[i - 1],
                prev2 + cost[i - 2]
            )

            prev2 = prev1
            prev1 = current

        return prev1
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
- [70. Climbing Stairs](../../0001-0500/0070-climbing-stairs/)
- [3693. Climbing Stairs II](../../3501-4000/3693-climbing-stairs-ii/)
- [1584. Min Cost to Connect All Points](../../1501-2000/1584-min-cost-to-connect-all-points/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/min-cost-climbing-stairs/)
