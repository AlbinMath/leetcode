# LeetCode 1622: Fancy Sequence

**LeetCode Problem #1622 — Fancy Sequence**
Solve LeetCode Fancy Sequence using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Fancy Sequence |
| LeetCode | #1622 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Write an API that generates fancy sequences using the `append`, `addAll`, and `multAll` operations.

Implement the `Fancy` class:

`Fancy()` Initializes the object with an empty sequence. 
 `void append(val)` Appends an integer `val` to the end of the sequence. 
 `void addAll(inc)` Increments all existing values in the sequence by an integer `inc`. 
 `void multAll(m)` Multiplies all existing values in the sequence by an integer `m`. 
 `int getIndex(idx)` Gets the current value at index `idx` (0-indexed) of the sequence **modulo** `10^9 + 7`. If the index is greater or equal than the length of the sequence, return `-1`.

## Constraints
- `1 <= val, inc, m <= 100`
- `0 <= idx <= 10^5`
- At most `10^5` calls total will be made to `append`, `addAll`, `multAll`, and `getIndex`.

## Examples
### Example 1
- **Input:** `["Fancy", "append", "addAll", "append", "multAll", "getIndex", "addAll", "append", "multAll", "getIndex", "getIndex", "getIndex"]
[[], [2], [3], [7], [2], [0], [3], [10], [2], [0], [1], [2]]`
- **Output:** `[null, null, null, null, null, 10, null, null, null, 26, 34, 20]`
- **Explanation:** Fancy fancy = new Fancy();
fancy.append(2); // fancy sequence: [2]
fancy.addAll(3); // fancy sequence: [2+3] -> [5]
fancy.append(7); // fancy sequence: [5, 7]
fancy.multAll(2); // fancy sequence: [5*2, 7*2] -> [10, 14]
fancy.getIndex(0); // return 10
fancy.addAll(3); // fancy sequence: [10+3, 14+3] -> [13, 17]
fancy.append(10); // fancy sequence: [13, 17, 10]
fancy.multAll(2); // fancy sequence: [13*2, 17*2, 10*2] -> [26, 34, 20]
fancy.getIndex(0); // return 26
fancy.getIndex(1); // return 34
fancy.getIndex(2); // return 20

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Fancy Sequence**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["Fancy", "append", "addAll", "append", "multAll", "getIndex", "addAll", "append", "multAll", "getIndex", "getIndex", "getIndex"]
[[], [2], [3], [7], [2], [0], [3], [10], [2], [0], [1], [2]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, null, null, null, null, 10, null, null, null, 26, 34, 20]`.
4. **Verification:** Fancy fancy = new Fancy();
fancy.append(2); // fancy sequence: [2]
fancy.addAll(3); // fancy sequence: [2+3] -> [5]
fancy.append(7); // fancy sequence: [5, 7]
fancy.multAll(2); // fancy sequence: [5*2, 7*2] -> [10, 14]
fancy.getIndex(0); // return 10
fancy.addAll(3); // fancy sequence: [10+3, 14+3] -> [13, 17]
fancy.append(10); // fancy sequence: [13, 17, 10]
fancy.multAll(2); // fancy sequence: [13*2, 17*2, 10*2] -> [26, 34, 20]
fancy.getIndex(0); // return 26
fancy.getIndex(1); // return 34
fancy.getIndex(2); // return 20

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
var Fancy = function () {
    this.MOD = 1000000007n;
    this.vals = [];
    this.mul = 1n;
    this.add = 0n;
};

Fancy.prototype.power = function (base, exp) {
    const MOD = this.MOD;
    let result = 1n;
    base %= MOD;
    while (exp > 0n) {
        if (exp & 1n) result = (result * base) % MOD;
        base = (base * base) % MOD;
        exp >>= 1n;
    }
    return result;
};

/** @param {number} val */
Fancy.prototype.append = function (val) {
    const MOD = this.MOD;
    const inv = this.power(this.mul, MOD - 2n);
    const stored = (((BigInt(val) - this.add) % MOD + MOD) % MOD) * inv % MOD;
    this.vals.push(stored);
};

/** @param {number} inc */
Fancy.prototype.addAll = function (inc) {
    this.add = (this.add + BigInt(inc)) % this.MOD;
};

/** @param {number} m */
Fancy.prototype.multAll = function (m) {
    const bm = BigInt(m);
    this.mul = (this.mul * bm) % this.MOD;
    this.add = (this.add * bm) % this.MOD;
};

/** @param {number} idx */
Fancy.prototype.getIndex = function (idx) {
    if (idx >= this.vals.length) return -1;
    return Number((this.vals[idx] * this.mul + this.add) % this.MOD);
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
- [60. Permutation Sequence](../../0001-0500/0060-permutation-sequence/)
- [128. Longest Consecutive Sequence](../../0001-0500/0128-longest-consecutive-sequence/)
- [842. Split Array into Fibonacci Sequence](../../0501-1000/0872-split-array-into-fibonacci-sequence/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/fancy-sequence/)
