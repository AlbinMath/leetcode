# LeetCode 3572: Maximize Y‑Sum by Picking a Triplet of Distinct X‑Values

**LeetCode Problem #3572 — Maximize Y‑Sum by Picking a Triplet of Distinct X‑Values**
Solve LeetCode Maximize Y‑Sum by Picking a Triplet of Distinct X‑Values using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximize Y‑Sum by Picking a Triplet of Distinct X‑Values |
| LeetCode | #3572 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two integer arrays `x` and `y`, each of length `n`. You must choose three **distinct** indices `i`, `j`, and `k` such that:

`x[i] != x[j]` 
 `x[j] != x[k]` 
 `x[k] != x[i]`

Your goal is to **maximize** the value of `y[i] + y[j] + y[k]` under these conditions. Return the **maximum** possible sum that can be obtained by choosing such a triplet of indices.

If no such triplet exists, return -1.

## Constraints
- `n == x.length == y.length`
- `3 <= n <= 10^5`
- `1 <= x[i], y[i] <= 10^6`

## Examples
### Example 1
- **Input:** `x = [1,2,1,3,2], y = [5,3,4,6,2]`
- **Output:** `14`
- **Explanation:** Choose `i = 0` (`x[i] = 1`, `y[i] = 5`), `j = 1` (`x[j] = 2`, `y[j] = 3`), `k = 3` (`x[k] = 3`, `y[k] = 6`). 
 All three values chosen from `x` are distinct. `5 + 3 + 6 = 14` is the maximum we can obtain. Hence, the output is 14.

### Example 2
- **Input:** `x = [1,2,1,2], y = [4,5,6,7]`
- **Output:** `-1`
- **Explanation:** There are only two distinct values in `x`. Hence, the output is -1.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximize Y‑Sum by Picking a Triplet of Distinct X‑Values**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `x = [1,2,1,3,2], y = [5,3,4,6,2]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `14`.
4. **Verification:** Choose `i = 0` (`x[i] = 1`, `y[i] = 5`), `j = 1` (`x[j] = 2`, `y[j] = 3`), `k = 3` (`x[k] = 3`, `y[k] = 6`). 
 All three values chosen from `x` are distinct. `5 + 3 + 6 = 14` is the maximum we can obtain. Hence, the output is 14.

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
var maxSumDistinctTriplet = function(x, y) {
    const maxY = new Map();

    for (let i = 0; i < x.length; i++) {
        maxY.set(
            x[i],
            Math.max(maxY.get(x[i]) || 0, y[i])
        );
    }

    const values = [...maxY.values()].sort((a, b) => b - a);

    if (values.length < 3) {
        return -1;
    }

    return values[0] + values[1] + values[2];
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
- [3569. Maximize Count of Distinct Primes After Split](../../3501-4000/3569-maximize-count-of-distinct-primes-after-split/)
- [3684. Maximize Sum of At Most K Distinct Elements](../../3501-4000/3684-maximize-sum-of-at-most-k-distinct-elements/)
- [115. Distinct Subsequences](../../0001-0500/0115-distinct-subsequences/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximize-ysum-by-picking-a-triplet-of-distinct-xvalues/)
