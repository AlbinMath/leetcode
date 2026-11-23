# LeetCode 2462: Total Cost to Hire K Workers

**LeetCode Problem #2462 — Total Cost to Hire K Workers**
Solve LeetCode Total Cost to Hire K Workers using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Total Cost to Hire K Workers |
| LeetCode | #2462 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** integer array `costs` where `costs[i]` is the cost of hiring the `i^th` worker.

You are also given two integers `k` and `candidates`. We want to hire exactly `k` workers according to the following rules:

You will run `k` sessions and hire exactly one worker in each session. 
 In each hiring session, choose the worker with the lowest cost from either the first `candidates` workers or the last `candidates` workers. Break the tie by the smallest index.
 
 For example, if `costs = [3,2,7,7,1,2]` and `candidates = 2`, then in the first hiring session, we will choose the `4^th` worker because they have the lowest cost `[ 3,2 ,7,7, **1**,2 ]`. 
 In the second hiring session, we will choose `1^st` worker because they have the same lowest cost as `4^th` worker but they have the smallest index `[ 3,**2** ,7, 7,2 ]`. Please note that the indexing may be changed in the process. 
 
 
 If there are fewer than candidates workers remaining, choose the worker with the lowest cost among them. Break the tie by the smallest index. 
 A worker can only be chosen once.

Return *the total cost to hire exactly *`k`* workers.*

## Constraints
- `1 <= costs.length <= 10^5 `
- `1 <= costs[i] <= 10^5`
- `1 <= k, candidates <= costs.length`

## Examples
### Example 1
- **Input:** `costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4`
- **Output:** `11`
- **Explanation:** We hire 3 workers in total. The total cost is initially 0.
- In the first hiring round we choose the worker from [ 17,12,10,2 ,7, 2,11,20,8 ]. The lowest cost is 2, and we break the tie by the smallest index, which is 3. The total cost = 0 + 2 = 2.
- In the second hiring round we choose the worker from [ 17,12,10,7 , 2,11,20,8 ]. The lowest cost is 2 (index 4). The total cost = 2 + 2 = 4.
- In the third hiring round we choose the worker from [ 17,12,10,7,11,20,8 ]. The lowest cost is 7 (index 3). The total cost = 4 + 7 = 11. Notice that the worker with index 3 was common in the first and last four workers.
The total hiring cost is 11.

### Example 2
- **Input:** `costs = [1,2,4,1], k = 3, candidates = 3`
- **Output:** `4`
- **Explanation:** We hire 3 workers in total. The total cost is initially 0.
- In the first hiring round we choose the worker from [ 1,2,4,1 ]. The lowest cost is 1, and we break the tie by the smallest index, which is 0. The total cost = 0 + 1 = 1. Notice that workers with index 1 and 2 are common in the first and last 3 workers.
- In the second hiring round we choose the worker from [ 2,4,1 ]. The lowest cost is 1 (index 2). The total cost = 1 + 1 = 2.
- In the third hiring round there are less than three candidates. We choose the worker from the remaining workers [ 2,4 ]. The lowest cost is 2 (index 0). The total cost = 2 + 2 = 4.
The total hiring cost is 4.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Total Cost to Hire K Workers**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `11`.
4. **Verification:** We hire 3 workers in total. The total cost is initially 0.
- In the first hiring round we choose the worker from [ 17,12,10,2 ,7, 2,11,20,8 ]. The lowest cost is 2, and we break the tie by the smallest index, which is 3. The total cost = 0 + 2 = 2.
- In the second hiring round we choose the worker from [ 17,12,10,7 , 2,11,20,8 ]. The lowest cost is 2 (index 4). The total cost = 2 + 2 = 4.
- In the third hiring round we choose the worker from [ 17,12,10,7,11,20,8 ]. The lowest cost is 7 (index 3). The total cost = 4 + 7 = 11. Notice that the worker with index 3 was common in the first and last four workers.
The total hiring cost is 11.

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
var totalCost = function(costs, k, candidates) {
    const n = costs.length;
    let total = 0;
    let left = 0;
    let right = n - 1;

    const leftHeap = [];
    const rightHeap = [];

    function push(heap, worker) {
        heap.push(worker);
        let i = heap.length - 1;

        while (i > 0) {
            const parent = Math.floor((i - 1) / 2);

            if (
                heap[parent][0] < heap[i][0] ||
                (heap[parent][0] === heap[i][0] &&
                 heap[parent][1] < heap[i][1])
            ) {
                break;
            }

            [heap[parent], heap[i]] = [heap[i], heap[parent]];
            i = parent;
        }
    }

    function pop(heap) {
        const min = heap[0];
        const last = heap.pop();

        if (heap.length > 0) {
            heap[0] = last;
            let i = 0;

            while (true) {
                let smallest = i;
                const l = 2 * i + 1;
                const r = 2 * i + 2;

                function isSmaller(a, b) {
                    return (
                        heap[a][0] < heap[b][0] ||
                        (heap[a][0] === heap[b][0] &&
                         heap[a][1] < heap[b][1])
                    );
                }

                if (l < heap.length && isSmaller(l, smallest)) {
                    smallest = l;
                }

                if (r < heap.length && isSmaller(r, smallest)) {
                    smallest = r;
                }

                if (smallest === i) break;

                [heap[i], heap[smallest]] =
                    [heap[smallest], heap[i]];

                i = smallest;
            }
        }

        return min;
    }

    // Fill the initial candidate heaps
    while (leftHeap.length < candidates && left <= right) {
        push(leftHeap, [costs[left], left]);
        left++;
    }

    while (rightHeap.length < candidates && left <= right) {
        push(rightHeap, [costs[right], right]);
        right--;
    }

    // Hire k workers
    for (let i = 0; i < k; i++) {
        if (
            rightHeap.length === 0 ||
            (leftHeap.length > 0 &&
             (leftHeap[0][0] < rightHeap[0][0] ||
              (leftHeap[0][0] === rightHeap[0][0] &&
               leftHeap[0][1] < rightHeap[0][1])))
        ) {
            const [cost] = pop(leftHeap);
            total += cost;

            if (left <= right) {
                push(leftHeap, [costs[left], left]);
                left++;
            }
        } else {
            const [cost] = pop(rightHeap);
            total += cost;

            if (left <= right) {
                push(rightHeap, [costs[right], right]);
                right--;
            }
        }
    }

    return total;
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
- [2499. Minimum Total Cost to Make Arrays Unequal](../../2501-3000/2592-minimum-total-cost-to-make-arrays-unequal/)
- [3619. Count Islands With Total Value Divisible by K](../../3501-4000/3823-count-islands-with-total-value-divisible-by-k/)
- [3987. Minimum Total Cost to Process All Elements](../../4001-4500/4351-minimum-total-cost-to-process-all-elements/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/total-cost-to-hire-k-workers/)
