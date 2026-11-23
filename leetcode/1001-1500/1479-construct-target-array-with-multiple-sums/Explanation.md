# LeetCode 1354: Construct Target Array With Multiple Sums

**LeetCode Problem #1354 — Construct Target Array With Multiple Sums**
Solve LeetCode Construct Target Array With Multiple Sums using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Construct Target Array With Multiple Sums |
| LeetCode | #1354 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array `target` of n integers. From a starting array `arr` consisting of `n` 1's, you may perform the following procedure :

let `x` be the sum of all elements currently in your array. 
 choose index `i`, such that `0 <= i < n` and set the value of `arr` at index `i` to `x`. 
 You may repeat this procedure as many times as needed.

Return `true` *if it is possible to construct the* `target` *array from* `arr`*, otherwise, return* `false`.

## Constraints
- `n == target.length`
- `1 <= n <= 5 * 10^4`
- `1 <= target[i] <= 10^9`

## Examples
### Example 1
- **Input:** `target = [9,3,5]`
- **Output:** `true`
- **Explanation:** Start with arr = [1, 1, 1] 
[1, 1, 1], sum = 3 choose index 1
[1, 3, 1], sum = 5 choose index 2
[1, 3, 5], sum = 9 choose index 0
[9, 3, 5] Done

### Example 2
- **Input:** `target = [1,1,1,2]`
- **Output:** `false`
- **Explanation:** Impossible to create target array from [1,1,1,1].

### Example 3
- **Input:** `target = [8,5]`
- **Output:** `true`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Construct Target Array With Multiple Sums**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `target = [9,3,5]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** Start with arr = [1, 1, 1] 
[1, 1, 1], sum = 3 choose index 1
[1, 3, 1], sum = 5 choose index 2
[1, 3, 5], sum = 9 choose index 0
[9, 3, 5] Done

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
var isPossible = function(target) {
    let sum = target.reduce((a, b) => a + b, 0);
    const heap = [];

    function push(num) {
        heap.push(num);
        let i = heap.length - 1;

        while (i > 0) {
            let parent = Math.floor((i - 1) / 2);

            if (heap[parent] >= heap[i]) break;

            [heap[parent], heap[i]] = [heap[i], heap[parent]];
            i = parent;
        }
    }

    function pop() {
        const max = heap[0];
        const last = heap.pop();

        if (heap.length > 0) {
            heap[0] = last;
            let i = 0;

            while (true) {
                let largest = i;
                let left = 2 * i + 1;
                let right = 2 * i + 2;

                if (left < heap.length &&
                    heap[left] > heap[largest]) {
                    largest = left;
                }

                if (right < heap.length &&
                    heap[right] > heap[largest]) {
                    largest = right;
                }

                if (largest === i) break;

                [heap[i], heap[largest]] =
                    [heap[largest], heap[i]];

                i = largest;
            }
        }

        return max;
    }

    for (const num of target) {
        push(num);
    }

    while (true) {
        let largest = pop();
        let rest = sum - largest;

        if (largest === 1 || rest === 1) {
            return true;
        }

        if (rest === 0 || largest <= rest) {
            return false;
        }

        let previous = largest % rest;

        if (previous === 0) {
            return false;
        }

        sum = rest + previous;
        push(previous);
    }
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
- [1389. Create Target Array in the Given Order](../../1501-2000/1505-create-target-array-in-the-given-order/)
- [1526. Minimum Number of Increments on Subarrays to Form a Target Array](../../1501-2000/1633-minimum-number-of-increments-on-subarrays-to-form-a-target-array/)
- [1558. Minimum Numbers of Function Calls to Make Target Array](../../1501-2000/1662-minimum-numbers-of-function-calls-to-make-target-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/construct-target-array-with-multiple-sums/)
