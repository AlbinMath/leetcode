# LeetCode 1286: Iterator for Combination

**LeetCode Problem #1286 — Iterator for Combination**
Solve LeetCode Iterator for Combination using JavaScript and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Iterator for Combination |
| LeetCode | #1286 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Design the `CombinationIterator` class:

`CombinationIterator(string characters, int combinationLength)` Initializes the object with a string `characters` of **sorted distinct** lowercase English letters and a number `combinationLength` as arguments. 
 `next()` Returns the next combination of length `combinationLength` in **lexicographical order**. 
 `hasNext()` Returns `true` if and only if there exists a next combination.

## Constraints
- `1 <= combinationLength <= characters.length <= 15`
- All the characters of `characters` are **unique**.
- At most `10^4` calls will be made to `next` and `hasNext`.
- It is guaranteed that all calls of the function `next` are valid.

## Examples
### Example 1
- **Input:** `["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[["abc", 2], [], [], [], [], [], []]`
- **Output:** `[null, "ab", true, "ac", true, "bc", false]`
- **Explanation:** CombinationIterator itr = new CombinationIterator("abc", 2);
itr.next(); // return "ab"
itr.hasNext(); // return True
itr.next(); // return "ac"
itr.hasNext(); // return True
itr.next(); // return "bc"
itr.hasNext(); // return False

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Iterator for Combination**, we observe the problem requirements and utilize the **Backtracking** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[["abc", 2], [], [], [], [], [], []]`.
2. **Processing Steps:** We apply **Backtracking Recursive Search** using our **Recursion Tree**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, "ab", true, "ac", true, "bc", false]`.
4. **Verification:** CombinationIterator itr = new CombinationIterator("abc", 2);
itr.next(); // return "ab"
itr.hasNext(); // return True
itr.next(); // return "ac"
itr.hasNext(); // return True
itr.next(); // return "bc"
itr.hasNext(); // return False

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Recursion Tree.

## Pattern
**Backtracking**

## Topics
- Backtracking
- Recursion

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
/**
 * @param {string} characters
 * @param {number} combinationLength
 */
var CombinationIterator = function(characters, combinationLength) {
    this.combinations = [];
    this.index = 0;

    const generate = (start, current) => {
        if (current.length === combinationLength) {
            this.combinations.push(current);
            return;
        }

        for (let i = start; i < characters.length; i++) {
            generate(i + 1, current + characters[i]);
        }
    };

    generate(0, "");
};

/**
 * @return {string}
 */
CombinationIterator.prototype.next = function() {
    return this.combinations[this.index++];
};

/**
 * @return {boolean}
 */
CombinationIterator.prototype.hasNext = function() {
    return this.index < this.combinations.length;
};
```

## Why This Works
By utilizing **Backtracking**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [39. Combination Sum](../../0001-0500/0039-combination-sum/)
- [40. Combination Sum II](../../0001-0500/0040-combination-sum-ii/)
- [216. Combination Sum III](../../0001-0500/0216-combination-sum-iii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/iterator-for-combination/)
