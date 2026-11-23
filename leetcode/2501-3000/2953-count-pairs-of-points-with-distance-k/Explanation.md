# LeetCode 2857: Count Pairs of Points With Distance k

**LeetCode Problem #2857 — Count Pairs of Points With Distance k**
Solve LeetCode Count Pairs of Points With Distance k using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Pairs of Points With Distance k |
| LeetCode | #2857 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **2D** integer array `coordinates` and an integer `k`, where `coordinates[i] = [x_i, y_i]` are the coordinates of the `i^th` point in a 2D plane.

We define the **distance** between two points `(x_1, y_1)` and `(x_2, y_2)` as `(x1 XOR x2) + (y1 XOR y2)` where `XOR` is the bitwise `XOR` operation.

Return *the number of pairs *`(i, j)`* such that *`i < j`* and the distance between points *`i`* and *`j`* is equal to *`k`.

## Constraints
- `2 <= coordinates.length <= 50000`
- `0 <= x_i, y_i <= 10^6`
- `0 <= k <= 100`

## Examples
### Example 1
- **Input:** `coordinates = [[1,2],[4,2],[1,3],[5,2]], k = 5`
- **Output:** `2`
- **Explanation:** We can choose the following pairs:
- (0,1): Because we have (1 XOR 4) + (2 XOR 2) = 5.
- (2,3): Because we have (1 XOR 5) + (3 XOR 2) = 5.

### Example 2
- **Input:** `coordinates = [[1,3],[1,3],[1,3],[1,3],[1,3]], k = 0`
- **Output:** `10`
- **Explanation:** Any two chosen pairs will have a distance of 0. There are 10 ways to choose two pairs.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Count Pairs of Points With Distance k**, we observe the problem requirements and utilize the **Tree & Graph** technique. By maintaining a **Tree / Graph / Grid**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Tree / Graph / Grid** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `coordinates = [[1,2],[4,2],[1,3],[5,2]], k = 5`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** We can choose the following pairs:
- (0,1): Because we have (1 XOR 4) + (2 XOR 2) = 5.
- (2,3): Because we have (1 XOR 5) + (3 XOR 2) = 5.

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
class Solution(object):
    def countPairs(self, coordinates, k):
        seen = {}
        ans = 0
        for x, y in coordinates:
            for a in range(k + 1):
                key = (x ^ a, y ^ (k - a))
                ans += seen.get(key, 0)
            p = (x, y)
            seen[p] = seen.get(p, 0) + 1
        return ans
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
- [2183. Count Array Pairs Divisible by K](../../2001-2500/2301-count-array-pairs-divisible-by-k/)
- [4043. Count Rotations With Exactly K Equal Adjacent Pairs](../../4001-4500/4411-count-rotations-with-exactly-k-equal-adjacent-pairs/)
- [863. All Nodes Distance K in Binary Tree](../../0501-1000/0893-all-nodes-distance-k-in-binary-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-pairs-of-points-with-distance-k/)
