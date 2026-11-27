# LeetCode 991: Broken Calculator

**LeetCode Problem #991 — Broken Calculator**
Solve LeetCode Broken Calculator using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Broken Calculator |
| LeetCode | #991 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is a broken calculator that has the integer `startValue` on its display initially. In one operation, you can:

multiply the number on display by `2`, or 
 subtract `1` from the number on display.

Given two integers `startValue` and `target`, return *the minimum number of operations needed to display *`target`* on the calculator*.

## Constraints
- `1 <= startValue, target <= 10^9`

## Examples
### Example 1
- **Input:** `startValue = 2, target = 3`
- **Output:** `2`
- **Explanation:** Use double operation and then decrement operation {2 -> 4 -> 3}.

### Example 2
- **Input:** `startValue = 5, target = 8`
- **Output:** `2`
- **Explanation:** Use decrement and then double {5 -> 4 -> 8}.

### Example 3
- **Input:** `startValue = 3, target = 10`
- **Output:** `3`
- **Explanation:** Use double, decrement and double {3 -> 6 -> 5 -> 10}.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Broken Calculator**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `startValue = 2, target = 3`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** Use double operation and then decrement operation {2 -> 4 -> 3}.

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
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        operations = 0
        
        while target > startValue:
            operations += 1
            if target % 2 == 0:
                target //= 2
            else:
                target += 1
                
        return operations + (startValue - target)
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
- [224. Basic Calculator](../../0001-0500/0224-basic-calculator/)
- [227. Basic Calculator II](../../0001-0500/0227-basic-calculator-ii/)
- [770. Basic Calculator IV](../../0501-1000/0770-basic-calculator-iv/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/broken-calculator/)
