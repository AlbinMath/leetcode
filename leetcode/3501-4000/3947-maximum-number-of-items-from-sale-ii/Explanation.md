# LeetCode 3947: Maximum Number of Items From Sale II

**LeetCode Problem #3947 — Maximum Number of Items From Sale II**
Solve LeetCode Maximum Number of Items From Sale II using JavaScript, Python and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Number of Items From Sale II |
| LeetCode | #3947 |
| Difficulty | Medium |
| Language | JavaScript, Python |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a 2D integer array `items`, where `items[i] = [factor_i, price_i]` represents the `i^th` item. You are also given an integer `budget`.

There are unlimited copies of each item available for purchase. You may buy any number of copies of any items such that the total cost of the purchased copies is at most `budget`.

After buying items, you may receive free copies according to the following rules:

Each purchased copy of item `i` can give you **at most one** free copy of another item `j`. 
 The free item must satisfy `i != j` and `factor_i` divides `factor_j`. 
 For each ordered pair `(i, j)`, you can receive a free copy of item `j` from purchases of item `i` **at most once**, regardless of how many copies of item `i` you buy. 
 The same item `j` can be received multiple times for free if it is received from purchases of different item types.

Return the **maximum total number of item copies** you can obtain, including both purchased copies and free copies, while spending at most `budget` on purchased items.

## Constraints
- `1 <= items.length <= 10^5`
- `items[i] = [factor_i, price_i]`
- `1 <= factor_i <= items.length`
- `1 <= price_i <= 10^9`
- `1 <= budget <= 10^9`

## Examples
### Example 1
- **Input:** `items = [[1,6],[2,4],[3,5]], budget = 19`
- **Output:** `5`
- **Explanation:** You can buy 2 copies of item 0 and 1 copy of item 1 for a total cost of `2 * 6 + 4 = 16`, which is not greater than `budget = 19`. 
 One purchased copy of item 0 gives 1 free copy of item 1, because `factor_0 = 1` divides `factor_1 = 2`. 
 The other purchased copy of item 0 gives 1 free copy of item 2, because `factor_0 = 1` divides `factor_2 = 3`. 
 You leave with 3 purchased copies and 2 free copies, for a total of 5 item copies.

### Example 2
- **Input:** `items = [[2,8],[1,10],[6,6],[4,12],[5,20],[5,17]], budget = 35`
- **Output:** `7`
- **Explanation:** You can buy 2 copies of item 0, 1 copy of item 1, and 1 copy of item 2 for a total cost of `2 * 8 + 10 + 6 = 32`, which is not greater than `budget = 35`. 
 One purchased copy of item 0 gives 1 free copy of item 2, because `factor_0 = 2` divides `factor_2 = 6`. 
 The other purchased copy of item 0 gives 1 free copy of item 3, because `factor_0 = 2` divides `factor_3 = 4`. 
 The purchased copy of item 1 gives 1 free copy of item 2, because `factor_1 = 1` divides `factor_2 = 6`. 
 Buying item 2 gives no free copy, because `factor_2 = 6` does not divide the factor of any other item. 
 You leave with 4 purchased copies and 3 free copies, for a total of 7 item copies.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Number of Items From Sale II**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `items = [[1,6],[2,4],[3,5]], budget = 19`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** You can buy 2 copies of item 0 and 1 copy of item 1 for a total cost of `2 * 6 + 4 = 16`, which is not greater than `budget = 19`. 
 One purchased copy of item 0 gives 1 free copy of item 1, because `factor_0 = 1` divides `factor_1 = 2`. 
 The other purchased copy of item 0 gives 1 free copy of item 2, because `factor_0 = 1` divides `factor_2 = 3`. 
 You leave with 3 purchased copies and 2 free copies, for a total of 5 item copies.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### JavaScript
```javascript
var maximumSaleItems = function(items, budget) {
    const n = items.length;

    const freq = new Array(n + 1).fill(0);

    let minPrice = Infinity;
    let maxFactor = 0;

    for (const [factor, price] of items) {
        freq[factor]++;
        minPrice = Math.min(minPrice, price);
        maxFactor = Math.max(maxFactor, factor);
    }

    const multiples = freq.slice();

    for (let f = 1; f <= maxFactor; f++) {
        for (let j = 2 * f; j <= maxFactor; j += f) {
            multiples[f] += freq[j];
        }
    }

    const offers = [];

    for (const [factor, price] of items) {
        const freeCount = multiples[factor] - 1;

        if (freeCount > 0 && price <= 2 * minPrice) {
            offers.push([price, freeCount]);
        }
    }

    offers.sort((a, b) => a[0] - b[0]);

    let answer = 0;

    for (const [price, count] of offers) {
        const take = Math.min(count, Math.floor(budget / price));

        answer += 2 * take;
        budget -= take * price;
    }

    answer += Math.floor(budget / minPrice);

    return answer;
};
```

### Python
```python
from collections import defaultdict

class Solution:
    def maximumSaleItems(self, items, budget):
        n = len(items)
        cnt = [0] * (n + 1)
        for f, p in items:
            cnt[f] += 1
        M = [0] * (n + 1)
        for f in range(1, n + 1):
            M[f] = sum(cnt[f::f])          # harmonic sieve, O(n log n)
        pmin = min(p for _, p in items)

        groups = defaultdict(int)
        for f, p in items:
            d = M[f] - 1
            if d > 0:
                groups[p] += d

        R = budget
        total = 0
        for p in sorted(groups):
            if p > 2 * pmin:
                break
            t = min(groups[p], R // p)
            total += 2 * t
            R -= t * p
            if t < groups[p]:
                break
        total += R // pmin
        return total
```

## Why This Works
By utilizing **Math & Logic**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3946. Maximum Number of Items From Sale I](../../3501-4000/3946-maximum-number-of-items-from-sale-i/)
- [2503. Maximum Number of Points From Grid Queries](../../2501-3000/2503-maximum-number-of-points-from-grid-queries/)
- [2554. Maximum Number of Integers to Choose From a Range I](../../2501-3000/2554-maximum-number-of-integers-to-choose-from-a-range-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-number-of-items-from-sale-ii/)
