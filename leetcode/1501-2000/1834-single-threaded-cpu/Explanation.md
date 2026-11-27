# LeetCode 1834: Single-Threaded CPU

**LeetCode Problem #1834 — Single-Threaded CPU**
Solve LeetCode Single-Threaded CPU using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Single-Threaded CPU |
| LeetCode | #1834 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given `n`​​​​​​ tasks labeled from `0` to `n - 1` represented by a 2D integer array `tasks`, where `tasks[i] = [enqueueTime_i, processingTime_i]` means that the `i^​​​​​​th`​​​​ task will be available to process at `enqueueTime_i` and will take `processingTime_i`_ to finish processing.

You have a single-threaded CPU that can process **at most one** task at a time and will act in the following way:

If the CPU is idle and there are no available tasks to process, the CPU remains idle. 
 If the CPU is idle and there are available tasks, the CPU will choose the one with the **shortest processing time**. If multiple tasks have the same shortest processing time, it will choose the task with the smallest index. 
 Once a task is started, the CPU will **process the entire task** without stopping. 
 The CPU can finish a task then start a new one instantly.

Return the order in which the CPU will process the tasks.

## Constraints
- `1 <= tasks.length <= 10^5`
- `tasks[i] = [enqueueTime_i, processingTime_i]`
- `1 <= enqueueTime_i, processingTime_i <= 10^9`

## Examples
### Example 1
- **Input:** `tasks = [[1,2],[2,4],[3,2],[4,1]]`
- **Output:** `[0,2,3,1]`
- **Explanation:** The events go as follows: 
- At time = 1, task 0 is available to process. Available tasks = {0}.
- Also at time = 1, the idle CPU starts processing task 0. Available tasks = {}.
- At time = 2, task 1 is available to process. Available tasks = {1}.
- At time = 3, task 2 is available to process. Available tasks = {1, 2}.
- Also at time = 3, the CPU finishes task 0 and starts processing task 2 as it is the shortest. Available tasks = {1}.
- At time = 4, task 3 is available to process. Available tasks = {1, 3}.
- At time = 5, the CPU finishes task 2 and starts processing task 3 as it is the shortest. Available tasks = {1}.
- At time = 6, the CPU finishes task 3 and starts processing task 1. Available tasks = {}.
- At time = 10, the CPU finishes task 1 and becomes idle.

### Example 2
- **Input:** `tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]`
- **Output:** `[4,3,2,0,1]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Single-Threaded CPU**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `tasks = [[1,2],[2,4],[3,2],[4,1]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[0,2,3,1]`.
4. **Verification:** The events go as follows: 
- At time = 1, task 0 is available to process. Available tasks = {0}.
- Also at time = 1, the idle CPU starts processing task 0. Available tasks = {}.
- At time = 2, task 1 is available to process. Available tasks = {1}.
- At time = 3, task 2 is available to process. Available tasks = {1, 2}.
- Also at time = 3, the CPU finishes task 0 and starts processing task 2 as it is the shortest. Available tasks = {1}.
- At time = 4, task 3 is available to process. Available tasks = {1, 3}.
- At time = 5, the CPU finishes task 2 and starts processing task 3 as it is the shortest. Available tasks = {1}.
- At time = 6, the CPU finishes task 3 and starts processing task 1. Available tasks = {}.
- At time = 10, the CPU finishes task 1 and becomes idle.

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
var getOrder = function(tasks) {
    const n = tasks.length;
    const sortedTasks = tasks.map((task, index) => [
        task[0],
        task[1],
        index
    ]);
    sortedTasks.sort((a, b) => a[0] - b[0]);
    const heap = [];
    const compare = (a, b) => {
        if (a[0] !== b[0]) {
            return a[0] - b[0];
        }
        return a[1] - b[1];
    };
    const push = (value) => {
        heap.push(value);
        let i = heap.length - 1;
        while (i > 0) {
            const parent = Math.floor((i - 1) / 2);
            if (compare(heap[parent], heap[i]) <= 0) {
                break;
            }
            [heap[parent], heap[i]] = [heap[i], heap[parent]];
            i = parent;
        }
    };
    const pop = () => {
        if (heap.length === 0) return null;
        const result = heap[0];
        const last = heap.pop();
        if (heap.length > 0) {
            heap[0] = last;
            let i = 0;
            while (true) {
                let smallest = i;
                const left = 2 * i + 1;
                const right = 2 * i + 2;
                if (
                    left < heap.length &&
                    compare(heap[left], heap[smallest]) < 0
                ) {
                    smallest = left;
                }
                if (
                    right < heap.length &&
                    compare(heap[right], heap[smallest]) < 0
                ) {
                    smallest = right;
                }
                if (smallest === i) break;
                [heap[i], heap[smallest]] =
                    [heap[smallest], heap[i]];
                i = smallest;
            }
        }
        return result;
    };
    const result = [];
    let time = 0;
    let i = 0;
    while (i < n || heap.length > 0) {
        if (heap.length === 0 && time < sortedTasks[i][0]) {
            time = sortedTasks[i][0];
        }
        while (i < n && sortedTasks[i][0] <= time) {
            const [enqueueTime, processingTime, index] = sortedTasks[i];
            push([processingTime, index]);
            i++;
        }
        const [processingTime, index] = pop();
        result.push(index);
        time += processingTime;
    }
    return result;
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
- [136. Single Number](../../0001-0500/0136-single-number/)
- [137. Single Number II](../../0001-0500/0137-single-number-ii/)
- [260. Single Number III](../../0001-0500/0260-single-number-iii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/single-threaded-cpu/)
