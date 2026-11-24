# LeetCode 2166: Design Bitset

**LeetCode Problem #2166 — Design Bitset**
Solve LeetCode Design Bitset using JavaScript and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Design Bitset |
| LeetCode | #2166 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A **Bitset** is a data structure that compactly stores bits.

Implement the `Bitset` class:

`Bitset(int size)` Initializes the Bitset with `size` bits, all of which are `0`. 
 `void fix(int idx)` Updates the value of the bit at the index `idx` to `1`. If the value was already `1`, no change occurs. 
 `void unfix(int idx)` Updates the value of the bit at the index `idx` to `0`. If the value was already `0`, no change occurs. 
 `void flip()` Flips the values of each bit in the Bitset. In other words, all bits with value `0` will now have value `1` and vice versa. 
 `boolean all()` Checks if the value of **each** bit in the Bitset is `1`. Returns `true` if it satisfies the condition, `false` otherwise. 
 `boolean one()` Checks if there is **at least one** bit in the Bitset with value `1`. Returns `true` if it satisfies the condition, `false` otherwise. 
 `int count()` Returns the **total number** of bits in the Bitset which have value `1`. 
 `String toString()` Returns the current composition of the Bitset. Note that in the resultant string, the character at the `i^th` index should coincide with the value at the `i^th` bit of the Bitset.

## Constraints
- `1 <= size <= 10^5`
- `0 <= idx <= size - 1`
- At most `10^5` calls will be made **in total** to `fix`, `unfix`, `flip`, `all`, `one`, `count`, and `toString`.
- At least one call will be made to `all`, `one`, `count`, or `toString`.
- At most `5` calls will be made to `toString`.

## Examples
### Example 1
- **Input:** `["Bitset", "fix", "fix", "flip", "all", "unfix", "flip", "one", "unfix", "count", "toString"]
[[5], [3], [1], [], [], [0], [], [], [0], [], []]`
- **Output:** `[null, null, null, null, false, null, null, true, null, 2, "01010"]`
- **Explanation:** Bitset bs = new Bitset(5); // bitset = "00000".
bs.fix(3); // the value at idx = 3 is updated to 1, so bitset = "00010".
bs.fix(1); // the value at idx = 1 is updated to 1, so bitset = "01010". 
bs.flip(); // the value of each bit is flipped, so bitset = "10101". 
bs.all(); // return False, as not all values of the bitset are 1.
bs.unfix(0); // the value at idx = 0 is updated to 0, so bitset = "00101".
bs.flip(); // the value of each bit is flipped, so bitset = "11010". 
bs.one(); // return True, as there is at least 1 index with value 1.
bs.unfix(0); // the value at idx = 0 is updated to 0, so bitset = "01010".
bs.count(); // return 2, as there are 2 bits with value 1.
bs.toString(); // return "01010", which is the composition of bitset.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Design Bitset**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["Bitset", "fix", "fix", "flip", "all", "unfix", "flip", "one", "unfix", "count", "toString"]
[[5], [3], [1], [], [], [0], [], [], [0], [], []]`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, null, null, null, false, null, null, true, null, 2, "01010"]`.
4. **Verification:** Bitset bs = new Bitset(5); // bitset = "00000".
bs.fix(3); // the value at idx = 3 is updated to 1, so bitset = "00010".
bs.fix(1); // the value at idx = 1 is updated to 1, so bitset = "01010". 
bs.flip(); // the value of each bit is flipped, so bitset = "10101". 
bs.all(); // return False, as not all values of the bitset are 1.
bs.unfix(0); // the value at idx = 0 is updated to 0, so bitset = "00101".
bs.flip(); // the value of each bit is flipped, so bitset = "11010". 
bs.one(); // return True, as there is at least 1 index with value 1.
bs.unfix(0); // the value at idx = 0 is updated to 0, so bitset = "01010".
bs.count(); // return 2, as there are 2 bits with value 1.
bs.toString(); // return "01010", which is the composition of bitset.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Integer Bitmask.

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var Bitset = function(size) {
    this.size = size;
    this.bits = new Uint8Array(size);
    this.ones = 0;
    this.flipped = 0; // 0 for false, 1 for true
};
Bitset.prototype.fix = function(idx) {
    if (this.bits[idx] === this.flipped) {
        this.bits[idx] ^= 1;
        this.ones++;
    }
};
Bitset.prototype.unfix = function(idx) {
    if (this.bits[idx] !== this.flipped) {
        this.bits[idx] ^= 1;
        this.ones--;
    }
};
Bitset.prototype.flip = function() {
    this.flipped ^= 1;
    this.ones = this.size - this.ones;
};
Bitset.prototype.all = function() {
    return this.ones === this.size;
};
Bitset.prototype.one = function() {
    return this.ones > 0;
};
Bitset.prototype.count = function() {
    return this.ones;
};
Bitset.prototype.toString = function() {
    const res = new Array(this.size);
    for (let i = 0; i < this.size; i++) {
        res[i] = this.bits[i] ^ this.flipped;
    }
    return res.join('');
};
```

## Why This Works
By utilizing **Bit Manipulation**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [211. Design Add and Search Words Data Structure](../../0001-0500/0211-design-add-and-search-words-data-structure/)
- [355. Design Twitter](../../0001-0500/0355-design-twitter/)
- [622. Design Circular Queue](../../0501-1000/0622-design-circular-queue/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/design-bitset/)
