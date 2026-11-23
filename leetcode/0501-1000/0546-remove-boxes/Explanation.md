# LeetCode 546: Remove Boxes

**LeetCode Problem #546 — Remove Boxes**
Solve LeetCode Remove Boxes using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Remove Boxes |
| LeetCode | #546 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given several `boxes` with different colors represented by different positive numbers.

You may experience several rounds to remove boxes until there is no box left. Each time you can choose some continuous boxes with the same color (i.e., composed of `k` boxes, `k >= 1`), remove them and get `k * k` points.

Return *the maximum points you can get*.

## Constraints
- `1 <= boxes.length <= 100`
- `1 <= boxes[i] <= 100`

## Examples
### Example 1
- **Input:** `boxes = [1,3,2,2,2,3,4,3,1]`
- **Output:** `23`
- **Explanation:** [1, 3, 2, 2, 2, 3, 4, 3, 1] 
----> [1, 3, 3, 4, 3, 1] (3*3=9 points) 
----> [1, 3, 3, 3, 1] (1*1=1 points) 
----> [1, 1] (3*3=9 points) 
----> [] (2*2=4 points)

### Example 2
- **Input:** `boxes = [1,1,1]`
- **Output:** `9`

### Example 3
- **Input:** `boxes = [1]`
- **Output:** `1`

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Remove Boxes**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `boxes = [1,3,2,2,2,3,4,3,1]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `23`.
4. **Verification:** [1, 3, 2, 2, 2, 3, 4, 3, 1] 
----> [1, 3, 3, 4, 3, 1] (3*3=9 points) 
----> [1, 3, 3, 3, 1] (1*1=1 points) 
----> [1, 1] (3*3=9 points) 
----> [] (2*2=4 points)

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for DP Table / Array.

## Pattern
**Dynamic Programming**

## Topics
- Dynamic Programming
- Memoization
- State Transition

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
import sys
from functools import lru_cache
from typing import List

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        sys.setrecursionlimit(10000)

        @lru_cache(maxsize=None)
        def dp(l, r, k):
            if l > r:
                return 0
            while l < r and boxes[l + 1] == boxes[l]:
                l += 1
                k += 1
            best = (k + 1) ** 2 + dp(l + 1, r, 0)
            for m in range(l + 1, r + 1):
                if boxes[m] == boxes[l]:
                    best = max(best, dp(l + 1, m - 1, 0) + dp(m, r, k + 1))
            return best

        return dp(0, len(boxes) - 1, 0)
```

## Why This Works
By utilizing **Dynamic Programming**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Incorrect base case initialization.
2. Flawed state transition equation.
3. Storing unnecessary state leading to Memory Limit Exceeded (MLE).

## Interview Notes
- **Tests:** Subproblem decomposition, state transition logic, and space optimization.
- **Follow-up:** Can space complexity be reduced from $O(n^2)$ to $O(n)$ or $O(1)$?

## Related Problems
- [1298. Maximum Candies You Can Get from Boxes](../../1001-1500/1424-maximum-candies-you-can-get-from-boxes/)
- [1467. Probability of a Two Boxes Having The Same Number of Distinct Balls](../../1501-2000/1577-probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/)
- [1687. Delivering Boxes from Storage to Ports](../../1501-2000/1789-delivering-boxes-from-storage-to-ports/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/remove-boxes/)
