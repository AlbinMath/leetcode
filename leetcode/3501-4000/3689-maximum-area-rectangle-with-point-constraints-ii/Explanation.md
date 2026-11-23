# LeetCode 3382: Maximum Area Rectangle With Point Constraints II

**LeetCode Problem #3382 — Maximum Area Rectangle With Point Constraints II**
Solve LeetCode Maximum Area Rectangle With Point Constraints II using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Area Rectangle With Point Constraints II |
| LeetCode | #3382 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
There are n points on an infinite plane. You are given two integer arrays `xCoord` and `yCoord` where `(xCoord[i], yCoord[i])` represents the coordinates of the `i^th` point.

Your task is to find the **maximum **area of a rectangle that:

Can be formed using **four** of these points as its corners. 
 Does **not** contain any other point inside or on its border. 
 Has its edges **parallel** to the axes.

Return the **maximum area** that you can obtain or -1 if no such rectangle is possible.

## Constraints
- `1 <= xCoord.length == yCoord.length <= 2 * 10^5`
- `0 <= xCoord[i], yCoord[i] <= 8 * 10^7`
- All the given points are **unique**.

## Examples
### Example 1
- **Input:** `xCoord = [1,1,3,3], yCoord = [1,3,1,3]`
- **Output:** `4`

### Example 2
- **Input:** `xCoord = [1,1,3,3,2], yCoord = [1,3,1,3,2]`
- **Output:** `-1`

### Example 3
- **Input:** `xCoord = [1,1,3,3,1,3], yCoord = [1,3,1,3,2,2]`
- **Output:** `2`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Maximum Area Rectangle With Point Constraints II**, we observe the problem requirements and utilize the **Math & Logic** technique. By maintaining a **Primitive Types**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Primitive Types** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `xCoord = [1,1,3,3], yCoord = [1,3,1,3]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.

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
var maxRectangleArea = function(xCoord, yCoord) {
    const n = xCoord.length;

    const points = Array.from({ length: n }, (_, i) => [
        xCoord[i],
        yCoord[i]
    ]);

    points.sort((a, b) => a[0] - b[0] || a[1] - b[1]);

    // Coordinate-compress y values.
    const ys = [...new Set(yCoord)].sort((a, b) => a - b);
    const m = ys.length;
    const yIndex = new Map();

    for (let i = 0; i < m; i++) {
        yIndex.set(ys[i], i);
    }

    // Segment tree: maximum x-coordinate seen at each y.
    let size = 1;
    while (size < m) size *= 2;

    const tree = new Array(size * 2).fill(-1);

    function update(pos, value) {
        let i = pos + size;
        tree[i] = value;

        for (i >>= 1; i > 0; i >>= 1) {
            tree[i] = Math.max(tree[i * 2], tree[i * 2 + 1]);
        }
    }

    function rangeMax(left, right) {
        let result = -1;
        left += size;
        right += size;

        while (left <= right) {
            if (left & 1) {
                result = Math.max(result, tree[left++]);
            }

            if (!(right & 1)) {
                result = Math.max(result, tree[right--]);
            }

            left >>= 1;
            right >>= 1;
        }

        return result;
    }

    // Latest x-coordinate where each vertical pair appeared.
    const lastPairX = new Map();
    let answer = -1;

    let start = 0;

    while (start < n) {
        let end = start;

        while (
            end + 1 < n &&
            points[end + 1][0] === points[start][0]
        ) {
            end++;
        }

        const x = points[start][0];

        // Collect y-coordinates in this column.
        const column = [];

        for (let i = start; i <= end; i++) {
            column.push(points[i][1]);
        }

        // Only consecutive points in a column can form
        // an unobstructed vertical rectangle edge.
        for (let i = 0; i + 1 < column.length; i++) {
            const y1 = column[i];
            const y2 = column[i + 1];
            const key = `${y1},${y2}`;

            if (lastPairX.has(key)) {
                const prevX = lastPairX.get(key);
                const low = yIndex.get(y1);
                const high = yIndex.get(y2);

                // No point in the rectangle's y-range
                // may have appeared between prevX and x.
                if (rangeMax(low, high) === prevX) {
                    const area = (x - prevX) * (y2 - y1);
                    answer = Math.max(answer, area);
                }
            }

            lastPairX.set(key, x);
        }

        // Update only after checking every pair in this column.
        for (const y of column) {
            update(yIndex.get(y), x);
        }

        start = end + 1;
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
- [3380. Maximum Area Rectangle With Point Constraints I](../../3501-4000/3681-maximum-area-rectangle-with-point-constraints-i/)
- [223. Rectangle Area](../../0001-0500/0223-rectangle-area/)
- [850. Rectangle Area II](../../0501-1000/0880-rectangle-area-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-ii/)
