# LeetCode 1157: Online Majority Element In Subarray

**LeetCode Problem #1157 — Online Majority Element In Subarray**
Solve LeetCode Online Majority Element In Subarray using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Online Majority Element In Subarray |
| LeetCode | #1157 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Design a data structure that efficiently finds the **majority element** of a given subarray.

The **majority element** of a subarray is an element that occurs `threshold` times or more in the subarray.

Implementing the `MajorityChecker` class:

`MajorityChecker(int[] arr)` Initializes the instance of the class with the given array `arr`. 
 `int query(int left, int right, int threshold)` returns the element in the subarray `arr[left...right]` that occurs at least `threshold` times, or `-1` if no such element exists.

## Constraints
- `1 <= arr.length <= 2 * 10^4`
- `1 <= arr[i] <= 2 * 10^4`
- `0 <= left <= right < arr.length`
- `threshold <= right - left + 1`
- `2 * threshold > right - left + 1`
- At most `10^4` calls will be made to `query`.

## Examples
### Example 1
- **Input:** `["MajorityChecker", "query", "query", "query"]
[[[1, 1, 2, 2, 1, 1]], [0, 5, 4], [0, 3, 3], [2, 3, 2]]`
- **Output:** `[null, 1, -1, 2]`
- **Explanation:** MajorityChecker majorityChecker = new MajorityChecker([1, 1, 2, 2, 1, 1]);
majorityChecker.query(0, 5, 4); // return 1
majorityChecker.query(0, 3, 3); // return -1
majorityChecker.query(2, 3, 2); // return 2

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Online Majority Element In Subarray**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["MajorityChecker", "query", "query", "query"]
[[[1, 1, 2, 2, 1, 1]], [0, 5, 4], [0, 3, 3], [2, 3, 2]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, 1, -1, 2]`.
4. **Verification:** MajorityChecker majorityChecker = new MajorityChecker([1, 1, 2, 2, 1, 1]);
majorityChecker.query(0, 5, 4); // return 1
majorityChecker.query(0, 3, 3); // return -1
majorityChecker.query(2, 3, 2); // return 2

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var MajorityChecker = function(arr) {
    this.arr = arr;
    this.positions = new Map();

    // Store every value's sorted occurrence indices
    for (let i = 0; i < arr.length; i++) {
        if (!this.positions.has(arr[i])) {
            this.positions.set(arr[i], []);
        }
        this.positions.get(arr[i]).push(i);
    }
};

MajorityChecker.prototype.query = function(left, right, threshold) {
    const arr = this.arr;
    const positions = this.positions;

    // Randomly sample candidates and verify their frequencies
    for (let attempt = 0; attempt < 30; attempt++) {
        const index =
            left + Math.floor(Math.random() * (right - left + 1));

        const value = arr[index];
        const indices = positions.get(value);

        // First occurrence >= left
        let lo = 0;
        let hi = indices.length;

        while (lo < hi) {
            const mid = Math.floor((lo + hi) / 2);

            if (indices[mid] < left) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }

        const start = lo;

        // First occurrence > right
        lo = 0;
        hi = indices.length;

        while (lo < hi) {
            const mid = Math.floor((lo + hi) / 2);

            if (indices[mid] <= right) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }

        const end = lo;

        if (end - start >= threshold) {
            return value;
        }
    }

    return -1;
};
```

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [169. Majority Element](../../0001-0500/0169-majority-element/)
- [229. Majority Element II](../../0001-0500/0229-majority-element-ii/)
- [1493. Longest Subarray of 1's After Deleting One Element](../../1501-2000/1586-longest-subarray-of-1s-after-deleting-one-element/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/online-majority-element-in-subarray/)
