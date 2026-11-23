# LeetCode 3528: Unit Conversion I

**LeetCode Problem #3528 — Unit Conversion I**
Solve LeetCode Unit Conversion I using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Unit Conversion I |
| LeetCode | #3528 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There are `n` types of units indexed from `0` to `n - 1`. You are given a 2D integer array `conversions` of length `n - 1`, where `conversions[i] = [sourceUnit_i, targetUnit_i, conversionFactor_i]`. This indicates that a single unit of type `sourceUnit_i` is equivalent to `conversionFactor_i` units of type `targetUnit_i`.

Return an array `baseUnitConversion` of length `n`, where `baseUnitConversion[i]` is the number of units of type `i` equivalent to a single unit of type 0. Since the answer may be large, return each `baseUnitConversion[i]` **modulo** `10^9 + 7`.

## Constraints
- `2 <= n <= 10^5`
- `conversions.length == n - 1`
- `0 <= sourceUnit_i, targetUnit_i < n`
- `1 <= conversionFactor_i <= 10^9`
- It is guaranteed that unit 0 can be converted into any other unit through a **unique** combination of conversions without using any conversions in the opposite direction.

## Examples
### Example 1
- **Input:** `conversions = [[0,1,2],[1,2,3]]`
- **Output:** `[1,2,6]`
- **Explanation:** Convert a single unit of type 0 into 2 units of type 1 using `conversions[0]`. 
 Convert a single unit of type 0 into 6 units of type 2 using `conversions[0]`, then `conversions[1]`.

### Example 2
- **Input:** `conversions = [[0,1,2],[0,2,3],[1,3,4],[1,4,5],[2,5,2],[4,6,3],[5,7,4]]`
- **Output:** `[1,2,3,8,10,6,30,24]`
- **Explanation:** Convert a single unit of type 0 into 2 units of type 1 using `conversions[0]`. 
 Convert a single unit of type 0 into 3 units of type 2 using `conversions[1]`. 
 Convert a single unit of type 0 into 8 units of type 3 using `conversions[0]`, then `conversions[2]`. 
 Convert a single unit of type 0 into 10 units of type 4 using `conversions[0]`, then `conversions[3]`. 
 Convert a single unit of type 0 into 6 units of type 5 using `conversions[1]`, then `conversions[4]`. 
 Convert a single unit of type 0 into 30 units of type 6 using `conversions[0]`, `conversions[3]`, then `conversions[5]`. 
 Convert a single unit of type 0 into 24 units of type 7 using `conversions[1]`, `conversions[4]`, then `conversions[6]`.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Unit Conversion I**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `conversions = [[0,1,2],[1,2,3]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,2,6]`.
4. **Verification:** Convert a single unit of type 0 into 2 units of type 1 using `conversions[0]`. 
 Convert a single unit of type 0 into 6 units of type 2 using `conversions[0]`, then `conversions[1]`.

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
var baseUnitConversions = function(conversions) {
    const MOD = 1000000007n;
    const n = conversions.length + 1;

    const graph = Array.from({ length: n }, () => []);

    for (const [source, target, factor] of conversions) {
        graph[source].push([target, BigInt(factor)]);
    }

    const ans = new Array(n).fill(0n);
    ans[0] = 1n;

    const queue = [0];
    let head = 0;

    while (head < queue.length) {
        const u = queue[head++];

        for (const [v, factor] of graph[u]) {
            ans[v] = (ans[u] * factor) % MOD;
            queue.push(v);
        }
    }

    // Convert BigInt results back to Numbers for LeetCode.
    return ans.map(value => Number(value));
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
- [6. Zigzag Conversion](../../0001-0500/0006-zigzag-conversion/)
- [3497. Analyze Subscription Conversion ](../../3501-4000/3848-analyze-subscription-conversion-/)
- [5. Longest Palindromic Substring](../../0001-0500/0005-longest-palindromic-substring/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/unit-conversion-i/)
