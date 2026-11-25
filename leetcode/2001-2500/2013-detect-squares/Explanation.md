# LeetCode 2013: Detect Squares

**LeetCode Problem #2013 — Detect Squares**
Solve LeetCode Detect Squares using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Detect Squares |
| LeetCode | #2013 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a stream of points on the X-Y plane. Design an algorithm that:

**Adds** new points from the stream into a data structure. **Duplicate** points are allowed and should be treated as different points. 
 Given a query point, **counts** the number of ways to choose three points from the data structure such that the three points and the query point form an **axis-aligned square** with **positive area**.

An **axis-aligned square** is a square whose edges are all the same length and are either parallel or perpendicular to the x-axis and y-axis.

Implement the `DetectSquares` class:

`DetectSquares()` Initializes the object with an empty data structure. 
 `void add(int[] point)` Adds a new point `point = [x, y]` to the data structure. 
 `int count(int[] point)` Counts the number of ways to form **axis-aligned squares** with point `point = [x, y]` as described above.

## Constraints
- `point.length == 2`
- `0 <= x, y <= 1000`
- At most `3000` calls **in total** will be made to `add` and `count`.

## Examples
### Example 1
- **Input:** `["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
[[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]`
- **Output:** `[null, null, null, null, 1, 0, null, 2]`
- **Explanation:** DetectSquares detectSquares = new DetectSquares();
detectSquares.add([3, 10]);
detectSquares.add([11, 2]);
detectSquares.add([3, 2]);
detectSquares.count([11, 10]); // return 1. You can choose:
 // - The first, second, and third points
detectSquares.count([14, 8]); // return 0. The query point cannot form a square with any points in the data structure.
detectSquares.add([11, 2]); // Adding duplicate points is allowed.
detectSquares.count([11, 10]); // return 2. You can choose:
 // - The first, second, and third points
 // - The first, third, and fourth points

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Detect Squares**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
[[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, null, null, null, 1, 0, null, 2]`.
4. **Verification:** DetectSquares detectSquares = new DetectSquares();
detectSquares.add([3, 10]);
detectSquares.add([11, 2]);
detectSquares.add([3, 2]);
detectSquares.count([11, 10]); // return 1. You can choose:
 // - The first, second, and third points
detectSquares.count([14, 8]); // return 0. The query point cannot form a square with any points in the data structure.
detectSquares.add([11, 2]); // Adding duplicate points is allowed.
detectSquares.count([11, 10]); // return 2. You can choose:
 // - The first, second, and third points
 // - The first, third, and fourth points

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
Python

## Source Code
- [solution.py](./solution.py)


```python
from collections import defaultdict

class DetectSquares:
    def __init__(self):
        self.cnt = defaultdict(int)             # (x, y) -> times added
        self.by_y = defaultdict(lambda: defaultdict(int))  # y -> {x: count}

    def add(self, point):
        x, y = point
        self.cnt[(x, y)] += 1
        self.by_y[y][x] += 1

    def count(self, point) -> int:
        qx, qy = point
        res = 0
        for x, c in self.by_y[qy].items():
            if x == qx:
                continue
            d = x - qx
            for ny in (qy + d, qy - d):
                res += c * self.cnt[(qx, ny)] * self.cnt[(x, ny)]
        return res
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
- [520. Detect Capital](../../0501-1000/0520-detect-capital/)
- [1559. Detect Cycles in 2D Grid](../../1501-2000/1559-detect-cycles-in-2d-grid/)
- [1566. Detect Pattern of Length M Repeated K or More Times](../../1501-2000/1566-detect-pattern-of-length-m-repeated-k-or-more-times/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/detect-squares/)
