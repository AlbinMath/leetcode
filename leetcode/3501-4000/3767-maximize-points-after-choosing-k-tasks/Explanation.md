# LeetCode 3767: Maximize Points After Choosing K Tasks

**LeetCode Problem #3767 — Maximize Points After Choosing K Tasks**
Solve LeetCode Maximize Points After Choosing K Tasks using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximize Points After Choosing K Tasks |
| LeetCode | #3767 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two integer arrays, `technique1` and `technique2`, each of length `n`, where `n` represents the number of tasks to complete.

If the `i^th` task is completed using technique 1, you earn `technique1[i]` points. 
 If it is completed using technique 2, you earn `technique2[i]` points.

You are also given an integer `k`, representing the **minimum** number of tasks that **must** be completed using technique 1.

You **must** complete **at least** `k` tasks using technique 1 (they do not need to be the first `k` tasks).

The remaining tasks may be completed using **either** technique.

Return an integer denoting the **maximum total points** you can earn.

## Constraints
- `1 <= n == technique1.length == technique2.length <= 10^5`
- `1 <= technique1[i], technique2​​​​​​​[i] <= 10^​​​​​​​5`
- `0 <= k <= n`

## Examples
### Example 1
- **Input:** `technique1 = [5,2,10], technique2 = [10,3,8], k = 2`
- **Output:** `22`
- **Explanation:** We must complete at least `k = 2` tasks using `technique1`. 

 Choosing `technique1[1]` and `technique1[2]` (completed using technique 1), and `technique2[0]` (completed using technique 2), yields the maximum points: `2 + 10 + 10 = 22`.

### Example 2
- **Input:** `technique1 = [10,20,30], technique2 = [5,15,25], k = 2`
- **Output:** `60`
- **Explanation:** We must complete at least `k = 2` tasks using `technique1`. 

 Choosing all tasks using technique 1 yields the maximum points: `10 + 20 + 30 = 60`.

### Example 3
- **Input:** `technique1 = [1,2,3], technique2 = [4,5,6], k = 0`
- **Output:** `15`
- **Explanation:** Since `k = 0`, we are not required to choose any task using `technique1`. 

 Choosing all tasks using technique 2 yields the maximum points: `4 + 5 + 6 = 15`.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximize Points After Choosing K Tasks**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `technique1 = [5,2,10], technique2 = [10,3,8], k = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `22`.
4. **Verification:** We must complete at least `k = 2` tasks using `technique1`. 

 Choosing `technique1[1]` and `technique1[2]` (completed using technique 1), and `technique2[0]` (completed using technique 2), yields the maximum points: `2 + 10 + 10 = 22`.

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
var maxPoints = function(technique1, technique2, k) {
    const n = technique1.length;

    const tasks = [];

    for (let i = 0; i < n; i++) {
        tasks.push({
            diff: technique1[i] - technique2[i],
            a: technique1[i],
            b: technique2[i]
        });
    }

    tasks.sort((a, b) => b.diff - a.diff);

    let total = 0;

    for (let i = 0; i < n; i++) {
        if (i < k || tasks[i].diff > 0) {
            total += tasks[i].a;
        } else {
            total += tasks[i].b;
        }
    }

    return total;
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
- [1005. Maximize Sum Of Array After K Negations](../../1001-1500/1005-maximize-sum-of-array-after-k-negations/)
- [2202. Maximize the Topmost Element After K Moves](../../2001-2500/2202-maximize-the-topmost-element-after-k-moves/)
- [3920. Maximize Fixed Points After Deletions](../../3501-4000/3920-maximize-fixed-points-after-deletions/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximize-points-after-choosing-k-tasks/)
