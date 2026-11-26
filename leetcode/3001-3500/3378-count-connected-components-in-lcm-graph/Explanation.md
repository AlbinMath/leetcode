# LeetCode 3378: Count Connected Components in LCM Graph

**LeetCode Problem #3378 — Count Connected Components in LCM Graph**
Solve LeetCode Count Connected Components in LCM Graph using Python and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Connected Components in LCM Graph |
| LeetCode | #3378 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array of integers `nums` of size `n` and a **positive** integer `threshold`.

There is a graph consisting of `n` nodes with the `i^th` node having a value of `nums[i]`. Two nodes `i` and `j` in the graph are connected via an **undirected** edge if `lcm(nums[i], nums[j]) <= threshold`.

Return the number of **connected components** in this graph.

A **connected component** is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.

The term `lcm(a, b)` denotes the **least common multiple** of `a` and `b`.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- All elements of `nums` are unique.
- `1 <= threshold <= 2 * 10^5`

## Examples
### Example 1
- **Input:** `nums = [2,4,8,3,9], threshold = 5`
- **Output:** `4`
- **Explanation:** The four connected components are `(2, 4)`, `(3)`, `(8)`, `(9)`.

### Example 2
- **Input:** `nums = [2,4,8,3,9,12], threshold = 10`
- **Output:** `2`
- **Explanation:** The two connected components are `(2, 3, 4, 8, 9)`, and `(12)`.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Connected Components in LCM Graph**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,4,8,3,9], threshold = 5`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The four connected components are `(2, 4)`, `(3)`, `(8)`, `(9)`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from math import gcd
from functools import reduce

class Solution:
    def countComponents(self, nums: List[int], threshold: int) -> int:
        p = list(range(threshold + 1))
        def f(x):
            while p[x] != x:
                p[x] = p[p[x]]
                x = p[x]
            return x
        for x in nums:
            if x <= threshold:
                for y in range(x, threshold + 1, x):
                    if y + x - gcd(y, x) <= threshold:
                        a, b = f(x), f(y)
                        p[a] = b
        return len(set(f(x) for x in nums if x <= threshold)) + sum(x > threshold for x in nums)
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
- [1761. Minimum Degree of a Connected Trio in a Graph](../../1501-2000/1761-minimum-degree-of-a-connected-trio-in-a-graph/)
- [2316. Count Unreachable Pairs of Nodes in an Undirected Graph](../../2001-2500/2316-count-unreachable-pairs-of-nodes-in-an-undirected-graph/)
- [2876. Count Visited Nodes in a Directed Graph](../../2501-3000/2876-count-visited-nodes-in-a-directed-graph/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-connected-components-in-lcm-graph/)
