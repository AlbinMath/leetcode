# LeetCode 686: Repeated String Match

**LeetCode Problem #686 — Repeated String Match**
Solve LeetCode Repeated String Match using JavaScript and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Repeated String Match |
| LeetCode | #686 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given two strings `a` and `b`, return *the minimum number of times you should repeat string *`a`* so that string* `b` *is a substring of it*. If it is impossible for `b`​​​​​​ to be a substring of `a` after repeating it, return `-1`.

**Notice:** string `"abc"` repeated 0 times is `""`, repeated 1 time is `"abc"` and repeated 2 times is `"abcabc"`.

## Constraints
- `1 <= a.length, b.length <= 10^4`
- `a` and `b` consist of lowercase English letters.

## Examples
### Example 1
- **Input:** `a = "abcd", b = "cdabcdab"`
- **Output:** `3`
- **Explanation:** We return 3 because by repeating a three times "ab

### Example 2
- **Input:** `a = "a", b = "aa"`
- **Output:** `2`

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Repeated String Match**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `a = "abcd", b = "cdabcdab"`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** We return 3 because by repeating a three times "ab

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Tree / Graph / Grid.

## Pattern
**Tree & Graph**

## Topics
- Tree
- Graph
- DFS
- BFS

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var repeatedStringMatch = function(a, b) {
    let repeated = a;
    let count = 1;

    while (repeated.length < b.length) {
        repeated += a;
        count++;
    }

    if (repeated.includes(b)) {
        return count;
    }

    repeated += a;
    count++;

    if (repeated.includes(b)) {
        return count;
    }

    return -1;
};
```

## Why This Works
By utilizing **Tree & Graph**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [4105. Repeated String Match II](../../4001-4500/4105-repeated-string-match-ii/)
- [942. DI String Match](../../0501-1000/0942-di-string-match/)
- [971. Flip Binary Tree To Match Preorder Traversal](../../0501-1000/0971-flip-binary-tree-to-match-preorder-traversal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/repeated-string-match/)
