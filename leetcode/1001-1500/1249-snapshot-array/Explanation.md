# LeetCode 1146: Snapshot Array

**LeetCode Problem #1146 — Snapshot Array**
Solve LeetCode Snapshot Array using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Snapshot Array |
| LeetCode | #1146 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Implement a SnapshotArray that supports the following interface:

`SnapshotArray(int length)` initializes an array-like data structure with the given length. **Initially, each element equals 0**. 
 `void set(index, val)` sets the element at the given `index` to be equal to `val`. 
 `int snap()` takes a snapshot of the array and returns the `snap_id`: the total number of times we called `snap()` minus `1`. 
 `int get(index, snap_id)` returns the value at the given `index`, at the time we took the snapshot with the given `snap_id`

## Constraints
- `1 <= length <= 5 * 10^4`
- `0 <= index < length`
- `0 <= val <= 10^9`
- `0 <= snap_id < `(the total number of times we call `snap()`)
- At most `5 * 10^4` calls will be made to `set`, `snap`, and `get`.

## Examples
### Example 1
- **Input:** `["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]`
- **Output:** `[null,null,0,null,5]`
- **Explanation:** SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
snapshotArr.set(0,5); // Set array[0] = 5
snapshotArr.snap(); // Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0); // Get the value of array[0] with snap_id = 0, return 5

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Snapshot Array**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null,null,0,null,5]`.
4. **Verification:** SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
snapshotArr.set(0,5); // Set array[0] = 5
snapshotArr.snap(); // Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0); // Get the value of array[0] with snap_id = 0, return 5

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
var SnapshotArray = function(length) {
    this.snapId = 0;
    this.history = Array.from({ length }, () => [[0, 0]]);
};

SnapshotArray.prototype.set = function(index, val) {
    const records = this.history[index];

    if (records[records.length - 1][0] === this.snapId) {
        records[records.length - 1][1] = val;
    } else {
        records.push([this.snapId, val]);
    }
};

SnapshotArray.prototype.snap = function() {
    return this.snapId++;
};

SnapshotArray.prototype.get = function(index, snap_id) {
    const records = this.history[index];
    let left = 0;
    let right = records.length - 1;
    let result = 0;

    while (left <= right) {
        const mid = Math.floor((left + right) / 2);

        if (records[mid][0] <= snap_id) {
            result = records[mid][1];
            left = mid + 1;
        } else {
            right = mid - 1;
        }
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
- [26. Remove Duplicates from Sorted Array](../../0001-0500/0026-remove-duplicates-from-sorted-array/)
- [33. Search in Rotated Sorted Array](../../0001-0500/0033-search-in-rotated-sorted-array/)
- [34. Find First and Last Position of Element in Sorted Array](../../0001-0500/0034-find-first-and-last-position-of-element-in-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/snapshot-array/)
