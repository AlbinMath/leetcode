# LeetCode 282: Expression Add Operators

**LeetCode Problem #282 — Expression Add Operators**
Solve LeetCode Expression Add Operators using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Expression Add Operators |
| LeetCode | #282 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a string `num` that contains only digits and an integer `target`, return ***all possibilities** to insert the binary operators *`'+'`*, *`'-'`*, and/or *`'*'`* between the digits of *`num`* so that the resultant expression evaluates to the *`target`* value*.

Note that operands in the returned expressions **should not** contain leading zeros.

**Note** that a number can contain multiple digits.

## Constraints
- `1 <= num.length <= 10`
- `num` consists of only digits.
- `-2^31 <= target <= 2^31 - 1`

## Examples
### Example 1
- **Input:** `num = "123", target = 6`
- **Output:** `["1*2*3","1+2+3"]`
- **Explanation:** Both "1*2*3" and "1+2+3" evaluate to 6.

### Example 2
- **Input:** `num = "232", target = 8`
- **Output:** `["2*3+2","2+3*2"]`
- **Explanation:** Both "2*3+2" and "2+3*2" evaluate to 8.

### Example 3
- **Input:** `num = "3456237490", target = 9191`
- **Output:** `[]`
- **Explanation:** There are no expressions that can be created from "3456237490" to evaluate to 9191.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Expression Add Operators**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `num = "123", target = 6`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `["1*2*3","1+2+3"]`.
4. **Verification:** Both "1*2*3" and "1+2+3" evaluate to 6.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Tree / Graph / Grid.

## Pattern
**Tree & Graph**

## Topics
- Tree
- Graph
- DFS
- BFS

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        n = len(num)

        def dfs(i, expr, cur, last):
            if i == n:
                if cur == target:
                    res.append(expr)
                return
            for j in range(i, n):
                if j > i and num[i] == '0':
                    break
                s = num[i:j + 1]
                v = int(s)
                if i == 0:
                    dfs(j + 1, s, v, v)
                else:
                    dfs(j + 1, expr + '+' + s, cur + v, v)
                    dfs(j + 1, expr + '-' + s, cur - v, -v)
                    dfs(j + 1, expr + '*' + s, cur - last + last * v, last * v)

        dfs(0, "", 0, 0)
        return res
```

## Why This Works
By utilizing **Tree & Graph**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [964. Least Operators to Express Number](../../0501-1000/0964-least-operators-to-express-number/)
- [2. Add Two Numbers](../../0001-0500/0002-add-two-numbers/)
- [67. Add Binary](../../0001-0500/0067-add-binary/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/expression-add-operators/)
