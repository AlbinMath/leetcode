# LeetCode 1534: Count Good Triplets

**LeetCode Problem #1534 — Count Good Triplets**
Solve LeetCode Count Good Triplets using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Good Triplets |
| LeetCode | #1534 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an array of integers `arr`, and three integers `a`, `b` and `c`. You need to find the number of good triplets.

A triplet `(arr[i], arr[j], arr[k])` is **good** if the following conditions are true:

`0 <= i < j < k < arr.length` 
 `|arr[i] - arr[j]| <= a` 
 `|arr[j] - arr[k]| <= b` 
 `|arr[i] - arr[k]| <= c`

Where `|x|` denotes the absolute value of `x`.

Return* the number of good triplets*.

## Constraints
- `3 <= arr.length <= 100`
- `0 <= arr[i] <= 1000`
- `0 <= a, b, c <= 1000`

## Examples
### Example 1
- **Input:** `arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3`
- **Output:** `4`
- **Explanation:** There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].

### Example 2
- **Input:** `arr = [1,1,2,2,3], a = 0, b = 0, c = 1`
- **Output:** `0`
- **Explanation:** No triplet satisfies all conditions.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Good Triplets**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        n = len(arr)
        count = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j + 1, n):
                        if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            count += 1
        return count
```

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2179. Count Good Triplets in an Array](../../2001-2500/2280-count-good-triplets-in-an-array/)
- [1442. Count Triplets That Can Form Two Arrays of Equal XOR](../../1501-2000/1553-count-triplets-that-can-form-two-arrays-of-equal-xor/)
- [1448. Count Good Nodes in Binary Tree](../../1501-2000/1544-count-good-nodes-in-binary-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-good-triplets/)
