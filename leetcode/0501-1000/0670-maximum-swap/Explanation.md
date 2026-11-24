# LeetCode 670: Maximum Swap

**LeetCode Problem #670 — Maximum Swap**
Solve LeetCode Maximum Swap using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Swap |
| LeetCode | #670 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer `num`. You can swap two digits at most once to get the maximum valued number.

Return *the maximum valued number you can get*.

## Constraints
- `0 <= num <= 10^8`

## Examples
### Example 1
- **Input:** `num = 2736`
- **Output:** `7236`
- **Explanation:** Swap the number 2 and the number 7.

### Example 2
- **Input:** `num = 9973`
- **Output:** `9973`
- **Explanation:** No swap.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Swap**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `num = 2736`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7236`.
4. **Verification:** Swap the number 2 and the number 7.

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
class Solution:
    def maximumSwap(self, num: int) -> int:
        a = list(str(num))
        last = {int(x): i for i, x in enumerate(a)}
        for i, x in enumerate(a):
            for d in range(9, int(x), -1):
                if d in last and last[d] > i:
                    a[i], a[last[d]] = a[last[d]], a[i]
                    return int(''.join(a))
        return num
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
- [24. Swap Nodes in Pairs](../../0001-0500/0024-swap-nodes-in-pairs/)
- [627. Swap Sex of Employees](../../0501-1000/0627-swap-sex-of-employees/)
- [777. Swap Adjacent in LR String](../../0501-1000/0777-swap-adjacent-in-lr-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-swap/)
