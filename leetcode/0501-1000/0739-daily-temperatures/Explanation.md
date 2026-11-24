# LeetCode 739: Daily Temperatures

**LeetCode Problem #739 — Daily Temperatures**
Solve LeetCode Daily Temperatures using JavaScript, TypeScript and Monotonic Stack. This solution finds the optimal result using Monotonic Stack Filtering in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Daily Temperatures |
| LeetCode | #739 |
| Difficulty | Medium |
| Language | JavaScript, TypeScript |
| Algorithm | Monotonic Stack Filtering |
| Data Structure | Stack |
| Pattern | Monotonic Stack |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an array of integers `temperatures` represents the daily temperatures, return *an array* `answer` *such that* `answer[i]` *is the number of days you have to wait after the* `i^th` *day to get a warmer temperature*. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

## Constraints
- `1 <= temperatures.length <= 10^5`
- `30 <= temperatures[i] <= 100`

## Examples
### Example 1
- **Input:** `temperatures = [73,74,75,71,69,72,76,73]`
- **Output:** `[1,1,4,2,1,1,0,0]`

### Example 2
- **Input:** `temperatures = [30,40,50,60]`
- **Output:** `[1,1,1,0]`

### Example 3
- **Input:** `temperatures = [30,60,90]`
- **Output:** `[1,1,0]`

## Key Insight
Maintain a stack whose elements are strictly increasing or decreasing to answer 'next greater' or 'previous smaller' query problems in $O(n)$ total operations.

## Approach
The code uses a **Monotonic Stack** (decreasing) to efficiently find the next warmer day for each index.

1. **Stack of Indices:** The stack stores indices of days whose "next warmer day" hasn't been found yet, in decreasing order of temperature.
2. **Iteration:** For each day `i`:
   - While the stack is not empty and `temperatures[i]` is greater than the temperature at the index on top of the stack: pop the index `prev` and set `result[prev] = i - prev`.
   - Push `i` onto the stack.
3. Any indices remaining in the stack after the loop already have `result[i] = 0` (initialized at the start).

Time complexity is $O(N)$ (each index is pushed and popped at most once) and space complexity is $O(N)$.

## Algorithm
1. Initialize state variables / data structure (**Stack**).
2. Process elements sequentially using **Monotonic Stack Filtering**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `temperatures = [73,74,75,71,69,72,76,73]`.
2. **Processing Steps:** We apply **Monotonic Stack Filtering** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,1,4,2,1,1,0,0]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Monotonic Stack**

## Topics
- Stack
- Monotonic Stack
- Array

## Language
JavaScript, TypeScript

## Source Code
- [solution.js](./solution.js)
- [solution.ts](./solution.ts)


### JavaScript
```javascript
var dailyTemperatures = function(temperatures) {
    const n = temperatures.length;
    const answer = new Array(n).fill(0);
    const stack = [];

    for (let i = 0; i < n; i++) {
        while (
            stack.length > 0 &&
            temperatures[i] > temperatures[stack[stack.length - 1]]
        ) {
            const prevIndex = stack.pop();
            answer[prevIndex] = i - prevIndex;
        }

        stack.push(i);
    }

    return answer;
};
```

### TypeScript
```typescript
function dailyTemperatures(temperatures: number[]): number[] {
    const result = new Array(temperatures.length).fill(0);
    const stack: number[] = [];

    for (let i = 0; i < temperatures.length; i++) {
        while (
            stack.length > 0 &&
            temperatures[i] > temperatures[stack[stack.length - 1]]
        ) {
            const prev = stack.pop()!;
            result[prev] = i - prev;
        }

        stack.push(i);
    }

    return result;
}
```

## Why This Works
By utilizing **Monotonic Stack**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Pushing elements instead of indices when index distance is required.
2. Using strict inequality (`<`) when non-strict (`<=`) is necessary.
3. Forgetting to flush remaining elements from stack at the end.

## Interview Notes
- **Tests:** Linear stack processing, nearest element relationship analysis.
- **Follow-up:** How do you handle circular array boundaries?

## Related Problems
- [1693. Daily Leads and Partners](../../1501-2000/1693-daily-leads-and-partners/)
- [28. Find the Index of the First Occurrence in a String](../../0001-0500/0028-find-the-index-of-the-first-occurrence-in-a-string/)
- [84. Largest Rectangle in Histogram](../../0001-0500/0084-largest-rectangle-in-histogram/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/daily-temperatures/)
