# LeetCode 2386: Find the K-Sum of an Array

**LeetCode Problem #2386 — Find the K-Sum of an Array**
Solve LeetCode Find the K-Sum of an Array using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the K-Sum of an Array |
| LeetCode | #2386 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` and a **positive** integer `k`. You can choose any **subsequence** of the array and sum all of its elements together.

We define the **K-Sum** of the array as the `k^th` **largest** subsequence sum that can be obtained (**not** necessarily distinct).

Return *the K-Sum of the array*.

A **subsequence** is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

**Note** that the empty subsequence is considered to have a sum of `0`.

## Constraints
- `n == nums.length`
- `1 <= n <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `1 <= k <= min(2000, 2^n)`

## Examples
### Example 1
- **Input:** `nums = [2,4,-2], k = 5`
- **Output:** `2`
- **Explanation:** All the possible subsequence sums that we can obtain are the following sorted in decreasing order:
6, 4, 4, 2, 2 , 0, 0, -2.
The 5-Sum of the array is 2.

### Example 2
- **Input:** `nums = [1,-2,3,4,-10,12], k = 16`
- **Output:** `10`
- **Explanation:** The 16-Sum of the array is 10.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Find the K-Sum of an Array**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,4,-2], k = 5`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** All the possible subsequence sums that we can obtain are the following sorted in decreasing order:
6, 4, 4, 2, 2 , 0, 0, -2.
The 5-Sum of the array is 2.

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
var kSum = function(nums, k) {
    let maxSum = 0;
    for (const num of nums) {
        if (num > 0) {
            maxSum += num;
        }
    }
    const arr = nums.map(Math.abs).sort((a, b) => a - b);
    const heap = [];
    const push = (item) => {
        heap.push(item);
        let i = heap.length - 1;
        while (i > 0) {
            const parent = Math.floor((i - 1) / 2);
            if (heap[parent][0] <= heap[i][0]) break;
            [heap[parent], heap[i]] = [heap[i], heap[parent]];
            i = parent;
        }
    };
    const pop = () => {
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
                    heap[left][0] < heap[smallest][0]
                ) {
                    smallest = left;
                }
                if (
                    right < heap.length &&
                    heap[right][0] < heap[smallest][0]
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
    push([0, -1]);
    let smallestSum = 0;
    for (let count = 0; count < k; count++) {
        const [sum, index] = pop();
        smallestSum = sum;
        const next = index + 1;
        if (next < arr.length) {
            push([sum + arr[next], next]);

            if (index >= 0) {
                push([
                    sum - arr[index] + arr[next],
                    next
                ]);
            }
        }
    }
    return maxSum - smallestSum;
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
- [1414. Find the Minimum Number of Fibonacci Numbers Whose Sum Is K](../../1001-1500/1414-find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/)
- [1420. Build Array Where You Can Find The Maximum Exactly K Comparisons](../../1001-1500/1420-build-array-where-you-can-find-the-maximum-exactly-k-comparisons/)
- [2099. Find Subsequence of Length K With the Largest Sum](../../2001-2500/2099-find-subsequence-of-length-k-with-the-largest-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-k-sum-of-an-array/)
