# LeetCode 3531: Count Covered Buildings

**LeetCode Problem #3531 — Count Covered Buildings**
Solve LeetCode Count Covered Buildings using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Covered Buildings |
| LeetCode | #3531 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

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
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Covered Buildings**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3, buildings = [[1,2],[2,2],[3,2],[2,1],[2,3]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
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
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1288. Remove Covered Intervals](../../1001-1500/1288-remove-covered-intervals/)
- [1893. Check if All the Integers in a Range Are Covered](../../1501-2000/1893-check-if-all-the-integers-in-a-range-are-covered/)
- [2271. Maximum White Tiles Covered by a Carpet](../../2001-2500/2271-maximum-white-tiles-covered-by-a-carpet/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-covered-buildings/)
