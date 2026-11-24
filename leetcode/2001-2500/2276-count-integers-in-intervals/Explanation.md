# LeetCode 2276: Count Integers in Intervals

**LeetCode Problem #2276 — Count Integers in Intervals**
Solve LeetCode Count Integers in Intervals using JavaScript and Heap. This solution finds the optimal result using Min/Max Heap Priority Selection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Integers in Intervals |
| LeetCode | #2276 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Min/Max Heap Priority Selection |
| Data Structure | Heap / Priority Queue |
| Pattern | Heap |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an **empty** set of intervals, implement a data structure that can:

**Add** an interval to the set of intervals. 
 **Count** the number of integers that are present in **at least one** interval.

Implement the `CountIntervals` class:

`CountIntervals()` Initializes the object with an empty set of intervals. 
 `void add(int left, int right)` Adds the interval `[left, right]` to the set of intervals. 
 `int count()` Returns the number of integers that are present in **at least one** interval.

**Note** that an interval `[left, right]` denotes all the integers `x` where `left <= x <= right`.

## Constraints
- `1 <= left <= right <= 10^9`
- At most `10^5` calls **in total** will be made to `add` and `count`.
- At least **one** call will be made to `count`.

## Examples
### Example 1
- **Input:** `["CountIntervals", "add", "add", "count", "add", "count"]
[[], [2, 3], [7, 10], [], [5, 8], []]`
- **Output:** `[null, null, null, 6, null, 8]`
- **Explanation:** CountIntervals countIntervals = new CountIntervals(); // initialize the object with an empty set of intervals. 
countIntervals.add(2, 3); // add [2, 3] to the set of intervals.
countIntervals.add(7, 10); // add [7, 10] to the set of intervals.
countIntervals.count(); // return 6
 // the integers 2 and 3 are present in the interval [2, 3].
 // the integers 7, 8, 9, and 10 are present in the interval [7, 10].
countIntervals.add(5, 8); // add [5, 8] to the set of intervals.
countIntervals.count(); // return 8
 // the integers 2 and 3 are present in the interval [2, 3].
 // the integers 5 and 6 are present in the interval [5, 8].
 // the integers 7 and 8 are present in the intervals [5, 8] and [7, 10].
 // the integers 9 and 10 are present in the interval [7, 10].

## Key Insight
Leverage **Heap** with **Heap / Priority Queue** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Integers in Intervals**, we observe the problem requirements and utilize the **Heap** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["CountIntervals", "add", "add", "count", "add", "count"]
[[], [2, 3], [7, 10], [], [5, 8], []]`.
2. **Processing Steps:** We apply **Min/Max Heap Priority Selection** using our **Heap / Priority Queue**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, null, null, 6, null, 8]`.
4. **Verification:** CountIntervals countIntervals = new CountIntervals(); // initialize the object with an empty set of intervals. 
countIntervals.add(2, 3); // add [2, 3] to the set of intervals.
countIntervals.add(7, 10); // add [7, 10] to the set of intervals.
countIntervals.count(); // return 6
 // the integers 2 and 3 are present in the interval [2, 3].
 // the integers 7, 8, 9, and 10 are present in the interval [7, 10].
countIntervals.add(5, 8); // add [5, 8] to the set of intervals.
countIntervals.count(); // return 8
 // the integers 2 and 3 are present in the interval [2, 3].
 // the integers 5 and 6 are present in the interval [5, 8].
 // the integers 7 and 8 are present in the intervals [5, 8] and [7, 10].
 // the integers 9 and 10 are present in the interval [7, 10].

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Heap / Priority Queue.

## Pattern
**Heap**

## Topics
- Heap
- Priority Queue
- Sorting

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var CountIntervals = function() {
    this.intervals = [];
    this.total = 0;
};
CountIntervals.prototype.add = function(left, right) {
    let lo = 0;
    let hi = this.intervals.length;
    while (lo < hi) {
        const mid = (lo + hi) >> 1;
        if (this.intervals[mid][1] < left - 1) {
            lo = mid + 1;
        } else {
            hi = mid;
        }
    }
    
    let end = lo;
    while (end < this.intervals.length && this.intervals[end][0] <= right + 1) {
        const [l, r] = this.intervals[end];
        if (l < left) left = l;
        if (r > right) right = r;
        this.total -= (r - l + 1);
        end++;
    }
    
    this.intervals.splice(lo, end - lo, [left, right]);
    this.total += (right - left + 1);
};
CountIntervals.prototype.count = function() {
    return this.total;
};
```

## Why This Works
By utilizing **Heap**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2180. Count Integers With Even Digit Sum](../../2001-2500/2180-count-integers-with-even-digit-sum/)
- [2442. Count Number of Distinct Integers After Reverse Operations](../../2001-2500/2442-count-number-of-distinct-integers-after-reverse-operations/)
- [2843.   Count Symmetric Integers](../../2501-3000/2843-count-symmetric-integers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-integers-in-intervals/)
