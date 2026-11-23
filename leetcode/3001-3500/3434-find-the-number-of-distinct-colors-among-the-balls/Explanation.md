# LeetCode 3160: Find the Number of Distinct Colors Among the Balls

**LeetCode Problem #3160 — Find the Number of Distinct Colors Among the Balls**
Solve LeetCode Find the Number of Distinct Colors Among the Balls using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Number of Distinct Colors Among the Balls |
| LeetCode | #3160 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer `limit` and a 2D array `queries` of size `n x 2`.

There are `limit + 1` balls with **distinct** labels in the range `[0, limit]`. Initially, all balls are uncolored. For every query in `queries` that is of the form `[x, y]`, you mark ball `x` with the color `y`. After each query, you need to find the number of colors among the balls.

Return an array `result` of length `n`, where `result[i]` denotes the number of colors *after* `i^th` query.

**Note** that when answering a query, lack of a color *will not* be considered as a color.

## Constraints
- `1 <= limit <= 10^9`
- `1 <= n == queries.length <= 10^5`
- `queries[i].length == 2`
- `0 <= queries[i][0] <= limit`
- `1 <= queries[i][1] <= 10^9`

## Examples
### Example 1
- **Input:** `limit = 4, queries = [[1,4],[2,5],[1,3],[3,4]]`
- **Output:** `[1,2,2,3]`
- **Explanation:** After query 0, ball 1 has color 4. 
 After query 1, ball 1 has color 4, and ball 2 has color 5. 
 After query 2, ball 1 has color 3, and ball 2 has color 5. 
 After query 3, ball 1 has color 3, ball 2 has color 5, and ball 3 has color 4.

### Example 2
- **Input:** `limit = 4, queries = [[0,1],[1,2],[2,2],[3,4],[4,5]]`
- **Output:** `[1,2,2,3,4]`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Find the Number of Distinct Colors Among the Balls**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `limit = 4, queries = [[1,4],[2,5],[1,3],[3,4]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,2,2,3]`.
4. **Verification:** After query 0, ball 1 has color 4. 
 After query 1, ball 1 has color 4, and ball 2 has color 5. 
 After query 2, ball 1 has color 3, and ball 2 has color 5. 
 After query 3, ball 1 has color 3, ball 2 has color 5, and ball 3 has color 4.

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
var queryResults = function(limit, queries) {
    const ballColor = new Map();
    const colorCount = new Map();
    const result = new Array(queries.length);

    for (let i = 0; i < queries.length; i++) {
        const [ball, color] = queries[i];

        if (ballColor.has(ball)) {
            const oldColor = ballColor.get(ball);
            const updatedCount = colorCount.get(oldColor) - 1;
            if (updatedCount === 0) {
                colorCount.delete(oldColor);
            } else {
                colorCount.set(oldColor, updatedCount);
            }
        }

        ballColor.set(ball, color);
        colorCount.set(color, (colorCount.get(color) || 0) + 1);
        result[i] = colorCount.size;
    }

    return result;
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
- [1467. Probability of a Two Boxes Having The Same Number of Distinct Balls](../../1501-2000/1577-probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/)
- [1742. Maximum Number of Balls in a Box](../../1501-2000/1844-maximum-number-of-balls-in-a-box/)
- [1769. Minimum Number of Operations to Move All Balls to Each Box](../../1501-2000/1895-minimum-number-of-operations-to-move-all-balls-to-each-box/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/)
