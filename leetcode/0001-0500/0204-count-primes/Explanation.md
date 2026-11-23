# LeetCode 204: Count Primes

**LeetCode Problem #204 — Count Primes**
Solve LeetCode Count Primes using JavaScript, Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Primes |
| LeetCode | #204 |
| Difficulty | Medium |
| Language | JavaScript, Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an integer `n`, return *the number of prime numbers that are strictly less than* `n`.

## Constraints
- `0 <= n <= 5 * 10^6`

## Examples
### Example 1
- **Input:** `n = 10`
- **Output:** `4`
- **Explanation:** There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

### Example 2
- **Input:** `n = 0`
- **Output:** `0`

### Example 3
- **Input:** `n = 1`
- **Output:** `0`

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Primes**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 10`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### JavaScript
```javascript
var countPrimes = function(n) {
    if (n <= 2) return 0;

    const isPrime = new Uint8Array(n);
    isPrime.fill(1);

    isPrime[0] = 0;
    isPrime[1] = 0;

    for (let i = 2; i * i < n; i++) {
        if (isPrime[i]) {
            for (let j = i * i; j < n; j += i) {
                isPrime[j] = 0;
            }
        }
    }

    let count = 0;

    for (let i = 2; i < n; i++) {
        count += isPrime[i];
    }

    return count;
};
```

### Python
```python
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        p = bytearray(b'\x01') * n
        p[0:2] = b'\x00\x00'
        for i in range(2, int(n**0.5) + 1):
            if p[i]:
                p[i*i:n:i] = b'\x00' * (((n - 1 - i*i) // i) + 1)
        return sum(p)
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
- [3569. Maximize Count of Distinct Primes After Split](../../3501-4000/3878-maximize-count-of-distinct-primes-after-split/)
- [38. Count and Say](../../0001-0500/0038-count-and-say/)
- [222. Count Complete Tree Nodes](../../0001-0500/0222-count-complete-tree-nodes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-primes/)
