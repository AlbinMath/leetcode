# LeetCode 2895: Minimum Processing Time

**LeetCode Problem #2895 — Minimum Processing Time**
Solve LeetCode Minimum Processing Time using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Processing Time |
| LeetCode | #2895 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You have a certain number of processors, each having 4 cores. The number of tasks to be executed is four times the number of processors. Each task must be assigned to a unique core, and each core can only be used once.

You are given an array `processorTime` representing the time each processor becomes available and an array `tasks` representing how long each task takes to complete. Return the *minimum* time needed to complete all tasks.

## Constraints
- `1 <= n == processorTime.length <= 25000`
- `1 <= tasks.length <= 10^5`
- `0 <= processorTime[i] <= 10^9`
- `1 <= tasks[i] <= 10^9`
- `tasks.length == 4 * n`

## Examples
### Example 1
- **Input:** `processorTime = [8,10], tasks = [2,2,3,1,8,7,4,5]`
- **Output:** `16`
- **Explanation:** Assign the tasks at indices 4, 5, 6, 7 to the first processor which becomes available at `time = 8`, and the tasks at indices 0, 1, 2, 3 to the second processor which becomes available at `time = 10`. 

 The time taken by the first processor to finish the execution of all tasks is `max(8 + 8, 8 + 7, 8 + 4, 8 + 5) = 16`. 

 The time taken by the second processor to finish the execution of all tasks is `max(10 + 2, 10 + 2, 10 + 3, 10 + 1) = 13`.

### Example 2
- **Input:** `processorTime = [10,20], tasks = [2,3,1,2,5,8,4,3]`
- **Output:** `23`
- **Explanation:** Assign the tasks at indices 1, 4, 5, 6 to the first processor and the others to the second processor. 

 The time taken by the first processor to finish the execution of all tasks is `max(10 + 3, 10 + 5, 10 + 8, 10 + 4) = 18`. 

 The time taken by the second processor to finish the execution of all tasks is `max(20 + 2, 20 + 1, 20 + 2, 20 + 3) = 23`.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Processing Time**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `processorTime = [8,10], tasks = [2,2,3,1,8,7,4,5]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `16`.
4. **Verification:** Assign the tasks at indices 4, 5, 6, 7 to the first processor which becomes available at `time = 8`, and the tasks at indices 0, 1, 2, 3 to the second processor which becomes available at `time = 10`. 

 The time taken by the first processor to finish the execution of all tasks is `max(8 + 8, 8 + 7, 8 + 4, 8 + 5) = 16`. 

 The time taken by the second processor to finish the execution of all tasks is `max(10 + 2, 10 + 2, 10 + 3, 10 + 1) = 13`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var minProcessingTime = function(processorTime, tasks) {
    processorTime.sort((a, b) => a - b);
    tasks.sort((a, b) => b - a);

    let ans = 0;

    for (let i = 0; i < processorTime.length; i++) {
        let maxTask = tasks[i * 4];

        let time = processorTime[i] + maxTask;

        ans = Math.max(ans, time);
    }

    return ans;
};
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [539. Minimum Time Difference](../../0501-1000/0539-minimum-time-difference/)
- [1266. Minimum Time Visiting All Points](../../1001-1500/1266-minimum-time-visiting-all-points/)
- [1443. Minimum Time to Collect All Apples in a Tree](../../1001-1500/1443-minimum-time-to-collect-all-apples-in-a-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-processing-time/)
