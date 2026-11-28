# LeetCode 4025: Minimize the Maximum Waiting Time at Synchronized Traffic Lights

**LeetCode Problem #4025 — Minimize the Maximum Waiting Time at Synchronized Traffic Lights**
Solve LeetCode Minimize the Maximum Waiting Time at Synchronized Traffic Lights using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimize the Maximum Waiting Time at Synchronized Traffic Lights |
| LeetCode | #4025 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer `period` and an integer array `lights`, where `lights[i]` is the duration, in seconds, of the green phase of the `i^th` traffic light.

At time 0, every traffic light starts at the beginning of its green phase. Their cycles are synchronized: every traffic light starts a new cycle at the same time, and every cycle lasts **exactly** `period` seconds. Therefore, the red phase of the `i^th` traffic light lasts for `period - lights[i]` seconds.

You are also given an integer array `arrivalTime`, where `arrivalTime[j]` is the arrival time, in seconds, of the `j^th` car.

Each car must be assigned to **exactly** one traffic light. Multiple cars may be assigned to the same traffic light. Any number of cars may cross the same traffic light simultaneously while it is green. Cars do not block or delay one another.

For a car `j` assigned to the `i^th` traffic light, let `r = arrivalTime[j] % period`. If `r < lights[i]`, its waiting time is 0. Otherwise, its waiting time is `period - r`.

The **penalty** of an assignment is the **maximum** waiting time among all cars.

Return an integer denoting the **minimum possible penalty**.

## Constraints
- `2 <= period <= 10^9`
- `1 <= lights.length <= 10^4`
- `1 <= lights[i] <= period - 1`
- `1 <= arrivalTime.length <= 10^5`
- `1 <= arrivalTime[i] <= 10^9`

## Examples
### Example 1
- **Input:** `period = 8, lights = [2,3], arrivalTime = [2,5,8,11]`
- **Output:** `5`
- **Explanation:** One optimal solution is: 

 
 Assign `arrivalTime[0]` to the traffic light with `lights[1] = 3`. Here, `r = 2 % 8 = 2`. Since `2 < 3`, the waiting time is 0. 
 Assign `arrivalTime[1]` to the traffic light with `lights[0] = 2`. Here, `r = 5 % 8 = 5`. Since `5 >= 2`, the waiting time is `8 - 5 = 3`. 
 Assign `arrivalTime[2]` to the traffic light with `lights[0] = 2`. Here, `r = 8 % 8 = 0`. Since `0 < 2`, the waiting time is 0. 
 Assign `arrivalTime[3]` to the traffic light with `lights[0] = 2`. Here, `r = 11 % 8 = 3`. Since `3 >= 2`, the waiting time is `8 - 3 = 5`. 
 

 The penalty of this assignment is 5, which is the minimum possible. Other optimal assignments may exist.

### Example 2
- **Input:** `period = 10, lights = [3,6,8], arrivalTime = [4,9,15]`
- **Output:** `1`
- **Explanation:** One optimal solution is: 

 
 Assign `arrivalTime[0]` to the traffic light with `lights[2] = 8`. Here, `r = 4 % 10 = 4`. Since `4 < 8`, the waiting time is 0. 
 Assign `arrivalTime[1]` to the traffic light with `lights[2] = 8`. Here, `r = 9 % 10 = 9`. Since `9 >= 8`, the waiting time is `10 - 9 = 1`. 
 Assign `arrivalTime[2]` to the traffic light with `lights[2] = 8`. Here, `r = 15 % 10 = 5`. Since `5 < 8`, the waiting time is 0. 
 

 The penalty of this assignment is 1, which is the minimum possible.

### Example 3
- **Input:** `period = 5, lights = [2], arrivalTime = [2,3,4,5,6]`
- **Output:** `3`
- **Explanation:** One optimal solution is: 

 
 Assign `arrivalTime[0]` to the traffic light with `lights[0] = 2`. Here, `r = 2 % 5 = 2`. Since `2 >= 2`, the waiting time is `5 - 2 = 3`. 
 Assign `arrivalTime[1]` to the traffic light with `lights[0] = 2`. Here, `r = 3 % 5 = 3`. Since `3 >= 2`, the waiting time is `5 - 3 = 2`. 
 Assign `arrivalTime[2]` to the traffic light with `lights[0] = 2`. Here, `r = 4 % 5 = 4`. Since `4 >= 2`, the waiting time is `5 - 4 = 1`. 
 Assign `arrivalTime[3]` to the traffic light with `lights[0] = 2`. Here, `r = 5 % 5 = 0`. Since `0 < 2`, the waiting time is 0. 
 Assign `arrivalTime[4]` to the traffic light with `lights[0] = 2`. Here, `r = 6 % 5 = 1`. Since `1 < 2`, the waiting time is 0. 
 

 The penalty of this assignment is 3, which is the minimum possible.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimize the Maximum Waiting Time at Synchronized Traffic Lights**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `period = 8, lights = [2,3], arrivalTime = [2,5,8,11]`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** One optimal solution is: 

 
 Assign `arrivalTime[0]` to the traffic light with `lights[1] = 3`. Here, `r = 2 % 8 = 2`. Since `2 < 3`, the waiting time is 0. 
 Assign `arrivalTime[1]` to the traffic light with `lights[0] = 2`. Here, `r = 5 % 8 = 5`. Since `5 >= 2`, the waiting time is `8 - 5 = 3`. 
 Assign `arrivalTime[2]` to the traffic light with `lights[0] = 2`. Here, `r = 8 % 8 = 0`. Since `0 < 2`, the waiting time is 0. 
 Assign `arrivalTime[3]` to the traffic light with `lights[0] = 2`. Here, `r = 11 % 8 = 3`. Since `3 >= 2`, the waiting time is `8 - 3 = 5`. 
 

 The penalty of this assignment is 5, which is the minimum possible. Other optimal assignments may exist.

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
var minPenalty = function(period, lights, arrivalTime) {
    const maxGreen = Math.max(...lights);

    let answer = 0;

    for (const time of arrivalTime) {
        const r = time % period;

        if (r >= maxGreen) {
            answer = Math.max(answer, period - r);
        }
    }

    return answer;
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
- [4009. Minimum Possible Maximum Waiting Time](../../4001-4500/4009-minimum-possible-maximum-waiting-time/)
- [1877. Minimize Maximum Pair Sum in Array](../../1501-2000/1877-minimize-maximum-pair-sum-in-array/)
- [2439. Minimize Maximum of Array](../../2001-2500/2439-minimize-maximum-of-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimize-the-maximum-waiting-time-at-synchronized-traffic-lights/)
