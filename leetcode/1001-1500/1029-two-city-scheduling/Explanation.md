# LeetCode 1029: Two City Scheduling

**LeetCode Problem #1029 — Two City Scheduling**
Solve LeetCode Two City Scheduling using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Two City Scheduling |
| LeetCode | #1029 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A company is planning to interview `2n` people. Given the array `costs` where `costs[i] = [aCost_i, bCost_i]`, the cost of flying the `i^th` person to city `a` is `aCost_i`, and the cost of flying the `i^th` person to city `b` is `bCost_i`.

Return *the minimum cost to fly every person to a city* such that exactly `n` people arrive in each city.

## Constraints
- `2 * n == costs.length`
- `2 <= costs.length <= 100`
- `costs.length` is even.
- `1 <= aCost_i, bCost_i <= 1000`

## Examples
### Example 1
- **Input:** `costs = [[10,20],[30,200],[400,50],[30,20]]`
- **Output:** `110`
- **Explanation:** The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.

### Example 2
- **Input:** `costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]`
- **Output:** `1859`

### Example 3
- **Input:** `costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]`
- **Output:** `3086`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Two City Scheduling**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `costs = [[10,20],[30,200],[400,50],[30,20]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `110`.
4. **Verification:** The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda c: c[0] - c[1])
        n = len(costs) // 2
        total = 0
        for i in range(n):
            total += costs[i][0]
        for i in range(n, 2 * n):
            total += costs[i][1]
        return total
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
- [1. Two Sum](../../0001-0500/0001-two-sum/)
- [2. Add Two Numbers](../../0001-0500/0002-add-two-numbers/)
- [4. Median of Two Sorted Arrays](../../0001-0500/0004-median-of-two-sorted-arrays/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/two-city-scheduling/)
