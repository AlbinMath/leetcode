# LeetCode 470: Implement Rand10() Using Rand7()

**LeetCode Problem #470 — Implement Rand10() Using Rand7()**
Solve LeetCode Implement Rand10() Using Rand7() using JavaScript and Trie. This solution finds the optimal result using Prefix Tree Lookup in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Implement Rand10() Using Rand7() |
| LeetCode | #470 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Prefix Tree Lookup |
| Data Structure | Trie Node |
| Pattern | Trie |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given the **API** `rand7()` that generates a uniform random integer in the range `[1, 7]`, write a function `rand10()` that generates a uniform random integer in the range `[1, 10]`. You can only call the API `rand7()`, and you shouldn't call any other API. Please **do not** use a language's built-in random API.

Each test case will have one **internal** argument `n`, the number of times that your implemented function `rand10()` will be called while testing. Note that this is **not an argument** passed to `rand10()`.

## Constraints
- `1 <= n <= 10^5`
- What is the expected value for the number of calls to `rand7()` function?
- Could you minimize the number of calls to `rand7()`?

## Examples
### Example 1
- **Input:** `n = 1`
- **Output:** `[2]`

### Example 2
- **Input:** `n = 2`
- **Output:** `[2,8]`

### Example 3
- **Input:** `n = 3`
- **Output:** `[3,8,10]`

## Key Insight
Leverage **Trie** with **Trie Node** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Implement Rand10() Using Rand7()**, we observe the problem requirements and utilize the **Trie** technique. We iterate through the inputs using **Prefix Tree Lookup**, leveraging a **Trie Node** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Trie Node**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 1`.
2. **Processing Steps:** We apply **Prefix Tree Lookup** using our **Trie Node**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Trie Node.

## Pattern
**Trie**

## Topics
- Trie
- String
- Prefix Search

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
/**
 * The rand7() API is already defined for you.
 * @return {number} a random integer in [1, 7]
 */

/**
 * @return {number}
 */
var rand10 = function() {
    while (true) {
        const a = rand7() - 1;
        const b = rand7() - 1;

        const num = a * 7 + b; // Uniform integer from 0 to 48

        if (num < 40) {
            return (num % 10) + 1;
        }
    }
};
```

## Why This Works
By utilizing **Trie**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [225. Implement Stack using Queues](../../0001-0500/0225-implement-stack-using-queues/)
- [232. Implement Queue using Stacks](../../0001-0500/0232-implement-queue-using-stacks/)
- [1320. Minimum Distance to Type a Word Using Two Fingers](../../1001-1500/1443-minimum-distance-to-type-a-word-using-two-fingers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/implement-rand10-using-rand7/)
