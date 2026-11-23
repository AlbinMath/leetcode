# LeetCode 284: Peeking Iterator

**LeetCode Problem #284 — Peeking Iterator**
Solve LeetCode Peeking Iterator using JavaScript and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Peeking Iterator |
| LeetCode | #284 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Design an iterator that supports the `peek` operation on an existing iterator in addition to the `hasNext` and the `next` operations.

Implement the `PeekingIterator` class:

`PeekingIterator(Iterator<int> nums)` Initializes the object with the given integer iterator `iterator`. 
 `int next()` Returns the next element in the array and moves the pointer to the next element. 
 `boolean hasNext()` Returns `true` if there are still elements in the array. 
 `int peek()` Returns the next element in the array **without** moving the pointer.

**Note:** Each language may have a different implementation of the constructor and `Iterator`, but they all support the `int next()` and `boolean hasNext()` functions.

## Constraints
- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 1000`
- All the calls to `next` and `peek` are valid.
- At most `1000` calls will be made to `next`, `hasNext`, and `peek`.

## Examples
### Example 1
- **Input:** `["PeekingIterator", "next", "peek", "next", "next", "hasNext"]
[[[1, 2, 3]], [], [], [], [], []]`
- **Output:** `[null, 1, 2, 2, 3, false]`
- **Explanation:** PeekingIterator peekingIterator = new PeekingIterator([1, 2, 3]); // [

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Peeking Iterator**, we observe the problem requirements and utilize the **Binary Search** technique. By maintaining a **Sorted Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Sorted Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["PeekingIterator", "next", "peek", "next", "next", "hasNext"]
[[[1, 2, 3]], [], [], [], [], []]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, 1, 2, 2, 3, false]`.
4. **Verification:** PeekingIterator peekingIterator = new PeekingIterator([1, 2, 3]); // [

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Sorted Array.

## Pattern
**Binary Search**

## Topics
- Binary Search
- Divide and Conquer
- Search Space

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
/**
 * // This is the Iterator's API interface.
 * // You should not implement it, or speculate about its implementation.
 * function Iterator() {}
 * Iterator.prototype.next = function() {};
 * Iterator.prototype.hasNext = function() {};
 */

/**
 * @param {Iterator} iterator
 */
var PeekingIterator = function(iterator) {
    this.iterator = iterator;
    this.hasPeeked = false;
    this.peekedValue = null;
};

/**
 * @return {number}
 */
PeekingIterator.prototype.peek = function() {
    if (!this.hasPeeked) {
        this.peekedValue = this.iterator.next();
        this.hasPeeked = true;
    }
    return this.peekedValue;
};

/**
 * @return {number}
 */
PeekingIterator.prototype.next = function() {
    if (this.hasPeeked) {
        const value = this.peekedValue;
        this.hasPeeked = false;
        this.peekedValue = null;
        return value;
    }
    return this.iterator.next();
};

/**
 * @return {boolean}
 */
PeekingIterator.prototype.hasNext = function() {
    return this.hasPeeked || this.iterator.hasNext();
};
```

## Why This Works
By utilizing **Binary Search**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Applying standard binary search without accounting for array rotation or duplicates.
2. Off-by-one errors when updating boundary pointers (`left = mid + 1` vs `right = mid - 1`).
3. Integer overflow during midpoint calculation (use `mid = left + (right - left) // 2`).

## Interview Notes
- **Tests:** Logarithmic search space reduction, boundary handling, and invariant preservation.
- **Follow-up:** How does performance change if the array contains duplicate elements?

## Related Problems
- [173. Binary Search Tree Iterator](../../0001-0500/0173-binary-search-tree-iterator/)
- [341. Flatten Nested List Iterator](../../0001-0500/0341-flatten-nested-list-iterator/)
- [900. RLE Iterator](../../0501-1000/0936-rle-iterator/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/peeking-iterator/)
