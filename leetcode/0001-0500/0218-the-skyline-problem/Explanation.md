# LeetCode 218: The Skyline Problem

**LeetCode Problem #218 — The Skyline Problem**
Solve LeetCode The Skyline Problem using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | The Skyline Problem |
| LeetCode | #218 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
A city's **skyline** is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return *the **skyline** formed by these buildings collectively*.

The geometric information of each building is given in the array `buildings` where `buildings[i] = [left_i, right_i, height_i]`:

`left_i` is the x coordinate of the left edge of the `i^th` building. 
 `right_i` is the x coordinate of the right edge of the `i^th` building. 
 `height_i` is the height of the `i^th` building.

You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height `0`.

The **skyline** should be represented as a list of "key points" **sorted by their x-coordinate** in the form `[[x_1,y_1],[x_2,y_2],...]`. Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, which always has a y-coordinate `0` and is used to mark the skyline's termination where the rightmost building ends. Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.

Note: There must be no consecutive horizontal lines of equal height in the output skyline. For instance, `[...,[2 3],[4 5],[7 5],[11 5],[12 7],...]` is not acceptable; the three lines of height 5 should be merged into one in the final output as such: `[...,[2 3],[4 5],[12 7],...]`

## Constraints
- `1 <= buildings.length <= 10^4`
- `0 <= left_i < right_i <= 2^31 - 1`
- `1 <= height_i <= 2^31 - 1`
- `buildings` is sorted by `left_i` in non-decreasing order.

## Examples
### Example 1
- **Input:** `buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]`
- **Output:** `[[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]`
- **Explanation:** Figure A shows the buildings of the input.
Figure B shows the skyline formed by those buildings. The red points in figure B represent the key points in the output list.

### Example 2
- **Input:** `buildings = [[0,2,3],[2,5,3]]`
- **Output:** `[[0,3],[5,0]]`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **The Skyline Problem**, we observe the problem requirements and utilize the **Dynamic Programming** technique. By maintaining a **DP Table / Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **DP Table / Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]`.
4. **Verification:** Figure A shows the buildings of the input.
Figure B shows the skyline formed by those buildings. The red points in figure B represent the key points in the output list.

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
var getSkyline = function(buildings) {
    const events = [];

    for (const [left, right, height] of buildings) {
        events.push([left, -height]);
        events.push([right, height]);
    }

    events.sort((a, b) => a[0] - b[0] || a[1] - b[1]);

    const result = [];
    const heap = [0];
    const active = new Map([[0, 1]]);

    function push(height) {
        heap.push(height);
        let i = heap.length - 1;

        while (i > 0) {
            const parent = Math.floor((i - 1) / 2);

            if (heap[parent] >= heap[i]) break;

            [heap[parent], heap[i]] = [heap[i], heap[parent]];
            i = parent;
        }
    }

    function pop() {
        const top = heap[0];
        const last = heap.pop();

        if (heap.length > 0) {
            heap[0] = last;
            let i = 0;

            while (true) {
                let largest = i;
                const left = 2 * i + 1;
                const right = 2 * i + 2;

                if (left < heap.length &&
                    heap[left] > heap[largest]) {
                    largest = left;
                }

                if (right < heap.length &&
                    heap[right] > heap[largest]) {
                    largest = right;
                }

                if (largest === i) break;

                [heap[i], heap[largest]] =
                    [heap[largest], heap[i]];

                i = largest;
            }
        }

        return top;
    }

    let prevMax = 0;
    let i = 0;

    while (i < events.length) {
        const x = events[i][0];

        // Process every event at this x-coordinate.
        while (i < events.length && events[i][0] === x) {
            const h = events[i][1];
            const height = Math.abs(h);

            if (h < 0) {
                active.set(height, (active.get(height) || 0) + 1);
                push(height);
            } else {
                active.set(height, (active.get(height) || 0) - 1);
            }

            i++;
        }

        // Remove expired heights from the top.
        while (
            heap.length > 0 &&
            (active.get(heap[0]) || 0) === 0
        ) {
            pop();
        }

        const currentMax = heap[0] || 0;

        if (currentMax !== prevMax) {
            result.push([x, currentMax]);
            prevMax = currentMax;
        }
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
- [807. Max Increase to Keep City Skyline](../../0501-1000/0807-max-increase-to-keep-city-skyline/)
- [365. Water and Jug Problem](../../0001-0500/0365-water-and-jug-problem/)
- [1. Two Sum](../../0001-0500/0001-two-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/the-skyline-problem/)
