# LeetCode 341: Flatten Nested List Iterator

**LeetCode Problem #341 — Flatten Nested List Iterator**
Solve LeetCode Flatten Nested List Iterator using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Flatten Nested List Iterator |
| LeetCode | #341 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a nested list of integers `nestedList`. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

Implement the `NestedIterator` class:

`NestedIterator(List<NestedInteger> nestedList)` Initializes the iterator with the nested list `nestedList`. 
 `int next()` Returns the next integer in the nested list. 
 `boolean hasNext()` Returns `true` if there are still some integers in the nested list and `false` otherwise.

Your code will be tested with the following pseudocode:

initialize iterator with nestedList
res = []
while iterator.hasNext()
 append iterator.next() to the end of res
return res

If `res` matches the expected flattened list, then your code will be judged as correct.

## Constraints
- `1 <= nestedList.length <= 500`
- The values of the integers in the nested list is in the range `[-10^6, 10^6]`.

## Examples
### Example 1
- **Input:** `nestedList = [[1,1],2,[1,1]]`
- **Output:** `[1,1,2,1,1]`
- **Explanation:** By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

### Example 2
- **Input:** `nestedList = [1,[4,[6]]]`
- **Output:** `[1,4,6]`
- **Explanation:** By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Flatten Nested List Iterator**, we observe the problem requirements and utilize the **Two Pointers** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nestedList = [[1,1],2,[1,1]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,1,2,1,1]`.
4. **Verification:** By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

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
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation.
 * function NestedInteger() {}
 * NestedInteger.prototype.isInteger = function() {};
 * NestedInteger.prototype.getInteger = function() {};
 * NestedInteger.prototype.getList = function() {};
 */

/**
 * @param {NestedInteger[]} nestedList
 */
var NestedIterator = function(nestedList) {
    this.stack = nestedList.slice().reverse();
};

/**
 * @return {number}
 */
NestedIterator.prototype.next = function() {
    this.hasNext();
    return this.stack.pop().getInteger();
};

/**
 * @return {boolean}
 */
NestedIterator.prototype.hasNext = function() {
    while (this.stack.length > 0) {
        const top = this.stack[this.stack.length - 1];

        if (top.isInteger()) {
            return true;
        }

        this.stack.pop();
        const list = top.getList();

        for (let i = list.length - 1; i >= 0; i--) {
            this.stack.push(list[i]);
        }
    }

    return false;
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
- [114. Flatten Binary Tree to Linked List](../../0001-0500/0114-flatten-binary-tree-to-linked-list/)
- [430. Flatten a Multilevel Doubly Linked List](../../0001-0500/0430-flatten-a-multilevel-doubly-linked-list/)
- [2625. Flatten Deeply Nested Array](../../2501-3000/2625-flatten-deeply-nested-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/flatten-nested-list-iterator/)
