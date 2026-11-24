# LeetCode 295: Find Median from Data Stream

**LeetCode Problem #295 — Find Median from Data Stream**
Solve LeetCode Find Median from Data Stream using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Median from Data Stream |
| LeetCode | #295 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
The **median** is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for `arr = [2,3,4]`, the median is `3`. 
 For example, for `arr = [2,3]`, the median is `(2 + 3) / 2 = 2.5`.

Implement the MedianFinder class:

`MedianFinder()` initializes the `MedianFinder` object. 
 `void addNum(int num)` adds the integer `num` from the data stream to the data structure. 
 `double findMedian()` returns the median of all elements so far. Answers within `10^-5` of the actual answer will be accepted.

## Constraints
- `-10^5 <= num <= 10^5`
- There will be at least one element in the data structure before calling `findMedian`.
- At most `5 * 10^4` calls will be made to `addNum` and `findMedian`.
- If all integer numbers from the stream are in the range `[0, 100]`, how would you optimize your solution?
- If `99%` of all integer numbers from the stream are in the range `[0, 100]`, how would you optimize your solution?

## Examples
### Example 1
- **Input:** `["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]`
- **Output:** `[null, null, null, 1.5, null, 2.0]`
- **Explanation:** MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1); // arr = [1]
medianFinder.addNum(2); // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3); // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Find Median from Data Stream**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, null, null, 1.5, null, 2.0]`.
4. **Verification:** MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1); // arr = [1]
medianFinder.addNum(2); // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3); // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0

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
var MedianFinder = function() {
    this.lower = []; // Max heap: smaller half
    this.upper = []; // Min heap: larger half
};

// Max heap insertion
MedianFinder.prototype.pushLower = function(num) {
    const heap = this.lower;
    heap.push(num);

    let i = heap.length - 1;

    while (i > 0) {
        const parent = Math.floor((i - 1) / 2);

        if (heap[parent] >= heap[i]) break;

        [heap[parent], heap[i]] = [heap[i], heap[parent]];
        i = parent;
    }
};

// Min heap insertion
MedianFinder.prototype.pushUpper = function(num) {
    const heap = this.upper;
    heap.push(num);

    let i = heap.length - 1;

    while (i > 0) {
        const parent = Math.floor((i - 1) / 2);

        if (heap[parent] <= heap[i]) break;

        [heap[parent], heap[i]] = [heap[i], heap[parent]];
        i = parent;
    }
};

// Remove the maximum from the max heap
MedianFinder.prototype.popLower = function() {
    const heap = this.lower;
    const top = heap[0];
    const last = heap.pop();

    if (heap.length > 0) {
        heap[0] = last;
        let i = 0;

        while (true) {
            let largest = i;
            const left = 2 * i + 1;
            const right = 2 * i + 2;

            if (
                left < heap.length &&
                heap[left] > heap[largest]
            ) largest = left;

            if (
                right < heap.length &&
                heap[right] > heap[largest]
            ) largest = right;

            if (largest === i) break;

            [heap[i], heap[largest]] =
                [heap[largest], heap[i]];

            i = largest;
        }
    }

    return top;
};

// Remove the minimum from the min heap
MedianFinder.prototype.popUpper = function() {
    const heap = this.upper;
    const top = heap[0];
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
                heap[left] < heap[smallest]
            ) smallest = left;

            if (
                right < heap.length &&
                heap[right] < heap[smallest]
            ) smallest = right;

            if (smallest === i) break;

            [heap[i], heap[smallest]] =
                [heap[smallest], heap[i]];

            i = smallest;
        }
    }

    return top;
};

MedianFinder.prototype.addNum = function(num) {
    if (
        this.lower.length === 0 ||
        num <= this.lower[0]
    ) {
        this.pushLower(num);
    } else {
        this.pushUpper(num);
    }

    // Balance the heaps
    if (this.lower.length > this.upper.length + 1) {
        this.pushUpper(this.popLower());
    } else if (this.upper.length > this.lower.length + 1) {
        this.pushLower(this.popUpper());
    }
};

MedianFinder.prototype.findMedian = function() {
    if (this.lower.length > this.upper.length) {
        return this.lower[0];
    }

    if (this.upper.length > this.lower.length) {
        return this.upper[0];
    }

    return (this.lower[0] + this.upper[0]) / 2;
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
- [2526. Find Consecutive Integers from a Data Stream](../../2501-3000/2620-find-consecutive-integers-from-a-data-stream/)
- [3134. Find the Median of the Uniqueness Array](../../3001-3500/3362-find-the-median-of-the-uniqueness-array/)
- [3585. Find Weighted Median Node in Tree](../../3501-4000/3900-find-weighted-median-node-in-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-median-from-data-stream/)
