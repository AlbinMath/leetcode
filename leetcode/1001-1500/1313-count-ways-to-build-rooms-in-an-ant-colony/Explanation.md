# LeetCode 1916: Count Ways to Build Rooms in an Ant Colony

**LeetCode Problem #1916 — Count Ways to Build Rooms in an Ant Colony**
Solve LeetCode Count Ways to Build Rooms in an Ant Colony using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Ways to Build Rooms in an Ant Colony |
| LeetCode | #1916 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are an ant tasked with adding `n` new rooms numbered `0` to `n-1` to your colony. You are given the expansion plan as a **0-indexed** integer array of length `n`, `prevRoom`, where `prevRoom[i]` indicates that you must build room `prevRoom[i]` before building room `i`, and these two rooms must be connected **directly**. Room `0` is already built, so `prevRoom[0] = -1`. The expansion plan is given such that once all the rooms are built, every room will be reachable from room `0`.

You can only build **one room** at a time, and you can travel freely between rooms you have **already built** only if they are **connected**. You can choose to build **any room** as long as its **previous room** is already built.

Return *the **number of different orders** you can build all the rooms in*. Since the answer may be large, return it **modulo** `10^9 + 7`.

## Constraints
- `n == prevRoom.length`
- `2 <= n <= 10^5`
- `prevRoom[0] == -1`
- `0 <= prevRoom[i] < n` for all `1 <= i < n`
- Every room is reachable from room `0` once all the rooms are built.

## Examples
### Example 1
- **Input:** `prevRoom = [-1,0,1]`
- **Output:** `1`
- **Explanation:** There is only one way to build the additional rooms: 0 &rarr; 1 &rarr; 2

### Example 2
- **Input:** `prevRoom = [-1,0,0,1,2]`
- **Output:** `6`
- **Explanation:** The 6 ways are:
0 &rarr; 1 &rarr; 3 &rarr; 2 &rarr; 4
0 &rarr; 2 &rarr; 4 &rarr; 1 &rarr; 3
0 &rarr; 1 &rarr; 2 &rarr; 3 &rarr; 4
0 &rarr; 1 &rarr; 2 &rarr; 4 &rarr; 3
0 &rarr; 2 &rarr; 1 &rarr; 3 &rarr; 4
0 &rarr; 2 &rarr; 1 &rarr; 4 &rarr; 3

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Ways to Build Rooms in an Ant Colony**, we observe the problem requirements and utilize the **Stack & Queue** technique. We iterate through the inputs using **Stack Push / Pop Parsing**, leveraging a **Stack** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Stack**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `prevRoom = [-1,0,1]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** There is only one way to build the additional rooms: 0 &rarr; 1 &rarr; 2

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
var waysToBuildRooms = function(prevRoom) {
    const MOD = 1000000007n;
    const n = prevRoom.length;

    const children = Array.from({ length: n }, () => []);

    for (let i = 1; i < n; i++) {
        children[prevRoom[i]].push(i);
    }

    const fact = Array(n + 1).fill(1n);
    const invFact = Array(n + 1).fill(1n);

    for (let i = 1; i <= n; i++) {
        fact[i] = fact[i - 1] * BigInt(i) % MOD;
    }

    function modPow(a, b) {
        let result = 1n;
        while (b > 0n) {
            if (b % 2n === 1n) result = result * a % MOD;
            a = a * a % MOD;
            b /= 2n;
        }
        return result;
    }

    invFact[n] = modPow(fact[n], MOD - 2n);

    for (let i = n; i >= 1; i--) {
        invFact[i - 1] = invFact[i] * BigInt(i) % MOD;
    }

    const size = Array(n).fill(1);
    const ways = Array(n).fill(1n);

    const order = [0];
    for (let i = 0; i < order.length; i++) {
        for (const child of children[order[i]]) {
            order.push(child);
        }
    }

    for (let i = n - 1; i >= 0; i--) {
        const node = order[i];
        let totalSize = 0;
        let result = 1n;

        for (const child of children[node]) {
            totalSize += size[child];
            result = result * ways[child] % MOD;
            result = result * invFact[size[child]] % MOD;
        }

        size[node] = totalSize + 1;
        ways[node] = result * fact[totalSize] % MOD;
    }

    return Number(ways[0]);
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
- [1735. Count Ways to Make Array With Product](../../1501-2000/1836-count-ways-to-make-array-with-product/)
- [3725. Count Ways to Choose Coprime Integers from Rows](../../4001-4500/4069-count-ways-to-choose-coprime-integers-from-rows/)
- [3028. Ant on the Boundary](../../3001-3500/3311-ant-on-the-boundary/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-ways-to-build-rooms-in-an-ant-colony/)
