# LeetCode 3387: Maximize Amount After Two Days of Conversions

**LeetCode Problem #3387 — Maximize Amount After Two Days of Conversions**
Solve LeetCode Maximize Amount After Two Days of Conversions using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximize Amount After Two Days of Conversions |
| LeetCode | #3387 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string `initialCurrency`, and you start with `1.0` of `initialCurrency`.

You are also given four arrays with currency pairs (strings) and rates (real numbers):

`pairs1[i] = [startCurrency_i, targetCurrency_i]` denotes that you can convert from `startCurrency_i` to `targetCurrency_i` at a rate of `rates1[i]` on **day 1**. 
 `pairs2[i] = [startCurrency_i, targetCurrency_i]` denotes that you can convert from `startCurrency_i` to `targetCurrency_i` at a rate of `rates2[i]` on **day 2**. 
 Also, each `targetCurrency` can be converted back to its corresponding `startCurrency` at a rate of `1 / rate`.

You can perform **any** number of conversions, **including zero**, using `rates1` on day 1, **followed** by any number of additional conversions, **including zero**, using `rates2` on day 2.

Return the **maximum** amount of `initialCurrency` you can have after performing any number of conversions on both days **in order**.

**Note: **Conversion rates are valid, and there will be no contradictions in the rates for either day. The rates for the days are independent of each other.

## Constraints
- `1 <= initialCurrency.length <= 3`
- `initialCurrency` consists only of uppercase English letters.
- `1 <= n == pairs1.length <= 10`
- `1 <= m == pairs2.length <= 10`
- `pairs1[i] == [startCurrency_i, targetCurrency_i]`
- `pairs2[i] == [startCurrency_i, targetCurrency_i]`
- `1 <= startCurrency_i.length, targetCurrency_i.length <= 3`
- `startCurrency_i` and `targetCurrency_i` consist only of uppercase English letters.
- `rates1.length == n`
- `rates2.length == m`
- `1.0 <= rates1[i], rates2[i] <= 10.0`
- The input is generated such that there are no contradictions or cycles in the conversion graphs for either day.
- The input is generated such that the output is **at most** `5 * 10^10`.

## Examples
### Example 1
- **Input:** `initialCurrency = "EUR", pairs1 = [["EUR","USD"],["USD","JPY"]], rates1 = [2.0,3.0], pairs2 = [["JPY","USD"],["USD","CHF"],["CHF","EUR"]], rates2 = [4.0,5.0,6.0]`
- **Output:** `720.00000`
- **Explanation:** To get the maximum amount of

### Example 2
- **Input:** `initialCurrency = "NGN", pairs1 = [["NGN","EUR"]] , rates1 = [9.0] , pairs2 = [["NGN","EUR"]] , rates2 = [6.0]`
- **Output:** `1.50000`
- **Explanation:** Converting

### Example 3
- **Input:** `initialCurrency = "USD", pairs1 = [["USD","EUR"]], rates1 = [1.0], pairs2 = [["EUR","JPY"]], rates2 = [10.0]`
- **Output:** `1.00000`
- **Explanation:** In this example, there is no need to make any conversions on either day.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Maximize Amount After Two Days of Conversions**, we observe the problem requirements and utilize the **Tree & Graph** technique. By maintaining a **Tree / Graph / Grid**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Tree / Graph / Grid** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `initialCurrency = "EUR", pairs1 = [["EUR","USD"],["USD","JPY"]], rates1 = [2.0,3.0], pairs2 = [["JPY","USD"],["USD","CHF"],["CHF","EUR"]], rates2 = [4.0,5.0,6.0]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `720.00000`.
4. **Verification:** To get the maximum amount of

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var maxAmount = function(initialCurrency, pairs1, rates1, pairs2, rates2) {
    function buildGraph(pairs, rates) {
        const graph = new Map();

        function addEdge(from, to, rate) {
            if (!graph.has(from)) {
                graph.set(from, []);
            }
            graph.get(from).push([to, rate]);
        }

        for (let i = 0; i < pairs.length; i++) {
            const [from, to] = pairs[i];
            const rate = rates[i];

            addEdge(from, to, rate);
            addEdge(to, from, 1 / rate);
        }

        return graph;
    }

    function calculateRates(graph, start) {
        const amounts = new Map();
        amounts.set(start, 1.0);

        const stack = [start];

        while (stack.length > 0) {
            const currency = stack.pop();
            const amount = amounts.get(currency);

            for (const [next, rate] of graph.get(currency) || []) {
                if (amounts.has(next)) continue;

                amounts.set(next, amount * rate);
                stack.push(next);
            }
        }

        return amounts;
    }

    const graph1 = buildGraph(pairs1, rates1);
    const graph2 = buildGraph(pairs2, rates2);

    // Day 1: Currency obtainable from 1 initial currency.
    const day1 = calculateRates(graph1, initialCurrency);

    // Day 2: Currency obtainable from 1 initial currency.
    const day2 = calculateRates(graph2, initialCurrency);

    let answer = 1.0;

    for (const [currency, amountDay1] of day1) {
        if (day2.has(currency)) {
            // Reverse the Day 2 conversion rate.
            const amountDay2 = 1 / day2.get(currency);

            answer = Math.max(
                answer,
                amountDay1 * amountDay2
            );
        }
    }

    return answer;
};
```

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [957. Prison Cells After N Days](../../0501-1000/0957-prison-cells-after-n-days/)
- [1005. Maximize Sum Of Array After K Negations](../../1001-1500/1005-maximize-sum-of-array-after-k-negations/)
- [1799. Maximize Score After N Operations](../../1501-2000/1799-maximize-score-after-n-operations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximize-amount-after-two-days-of-conversions/)
