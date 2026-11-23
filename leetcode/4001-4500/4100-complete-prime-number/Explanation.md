# LeetCode 3765: Complete Prime Number

**LeetCode Problem #3765 — Complete Prime Number**
Solve LeetCode Complete Prime Number using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Complete Prime Number |
| LeetCode | #3765 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer `num`.

A number `num` is called a **Complete Prime Number ** if every **prefix** and every **suffix** of `num` is **prime**.

Return `true` if `num` is a Complete Prime Number, otherwise return `false`.

**Note**:

A **prefix** of a number is formed by the **first** `k` digits of the number. 
 A **suffix** of a number is formed by the **last** `k` digits of the number. 
 Single-digit numbers are considered Complete Prime Numbers only if they are **prime**.

## Constraints
- `1 <= num <= 10^9`

## Examples
### Example 1
- **Input:** `num = 23`
- **Output:** `true`

### Example 2
- **Input:** `num = 39`
- **Output:** `false`
- **Explanation:** Prefixes of `num = 39` are 3 and 39. 3 is prime, but 39 is not prime. 
 Suffixes of `num = 39` are 9 and 39. Both 9 and 39 are not prime. 
 At least one prefix or suffix is not prime, so 39 is not a Complete Prime Number and the answer is `false`.

### Example 3
- **Input:** `num = 7`
- **Output:** `true`
- **Explanation:** 7 is prime, so all its prefixes and suffixes are prime and the answer is `true`.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Complete Prime Number**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `num = 23`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var completePrime = function(num) {
    const isPrime = (x) => {
        if (x < 2) return false;
        if (x === 2 || x === 3) return true;
        if (x % 2 === 0 || x % 3 === 0) return false;

        for (let i = 5; i * i <= x; i += 6) {
            if (x % i === 0 || x % (i + 2) === 0) {
                return false;
            }
        }
        return true;
    };

    // 1. Check all prefixes (including num itself)
    let prefix = num;
    while (prefix > 0) {
        if (!isPrime(prefix)) return false;
        prefix = Math.floor(prefix / 10);
    }

    // 2. Check all proper suffixes
    let mod = 10;
    while (mod <= num) {
        if (!isPrime(num % mod)) return false;
        mod *= 10;
    }

    return true;
};
```

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2685. Count the Number of Complete Components](../../2501-3000/2793-count-the-number-of-complete-components/)
- [762. Prime Number of Set Bits in Binary Representation](../../0501-1000/0767-prime-number-of-set-bits-in-binary-representation/)
- [222. Count Complete Tree Nodes](../../0001-0500/0222-count-complete-tree-nodes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/complete-prime-number/)
