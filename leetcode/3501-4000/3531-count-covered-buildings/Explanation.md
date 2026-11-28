# LeetCode 3531: Count Covered Buildings

**LeetCode Problem #3531 — Count Covered Buildings**
Solve LeetCode Count Covered Buildings using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Covered Buildings |
| LeetCode | #3531 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a positive integer `n`, representing an `n x n` city. You are also given a 2D grid `buildings`, where `buildings[i] = [x, y]` denotes a **unique** building located at coordinates `[x, y]`.

A building is **covered** if there is at least one building in all **four** directions: left, right, above, and below.

Return the number of **covered** buildings.

## Constraints
- `2 <= n <= 10^5`
- `1 <= buildings.length <= 10^5 `
- `buildings[i] = [x, y]`
- `1 <= x, y <= n`
- All coordinates of `buildings` are **unique**.

## Examples
### Example 1
- **Input:** `n = 3, buildings = [[1,2],[2,2],[3,2],[2,1],[2,3]]`
- **Output:** `1`
- **Explanation:** Only building `[2,2]` is covered as it has at least one building:

 
 above (`[1,2]`) 
 below (`[3,2]`) 
 left (`[2,1]`) 
 right (`[2,3]`) 
 
 
 Thus, the count of covered buildings is 1.

### Example 2
- **Input:** `n = 3, buildings = [[1,1],[1,2],[2,1],[2,2]]`
- **Output:** `0`
- **Explanation:** No building has at least one building in all four directions.

### Example 3
- **Input:** `n = 5, buildings = [[1,3],[3,2],[3,3],[3,5],[5,3]]`
- **Output:** `1`
- **Explanation:** Only building `[3,3]` is covered as it has at least one building:

 
 above (`[1,3]`) 
 below (`[5,3]`) 
 left (`[3,2]`) 
 right (`[3,5]`) 
 
 
 Thus, the count of covered buildings is 1.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Count Covered Buildings**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3, buildings = [[1,2],[2,2],[3,2],[2,1],[2,3]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** Only building `[2,2]` is covered as it has at least one building:

 
 above (`[1,2]`) 
 below (`[3,2]`) 
 left (`[2,1]`) 
 right (`[2,3]`) 
 
 
 Thus, the count of covered buildings is 1.

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
var countCoveredBuildings = function(n, buildings) {
    const rowMin = new Map();
    const rowMax = new Map();
    const colMin = new Map();
    const colMax = new Map();

    for (const [x, y] of buildings) {
        rowMin.set(x, Math.min(rowMin.get(x) ?? Infinity, y));
        rowMax.set(x, Math.max(rowMax.get(x) ?? -Infinity, y));
        colMin.set(y, Math.min(colMin.get(y) ?? Infinity, x));
        colMax.set(y, Math.max(colMax.get(y) ?? -Infinity, x));
    }

    let count = 0;
    for (const [x, y] of buildings) {
        const hasLeft = y > rowMin.get(x);
        const hasRight = y < rowMax.get(x);
        const hasAbove = x > colMin.get(y);
        const hasBelow = x < colMax.get(y);

        if (hasLeft && hasRight && hasAbove && hasBelow) {
            count++;
        }
    }
    return count;
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
- [38. Count and Say](../../0001-0500/0038-count-and-say/)
- [204. Count Primes](../../0001-0500/0204-count-primes/)
- [222. Count Complete Tree Nodes](../../0001-0500/0222-count-complete-tree-nodes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-covered-buildings/)
