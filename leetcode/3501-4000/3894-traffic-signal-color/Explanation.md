# LeetCode 3894: Traffic Signal Color

**LeetCode Problem #3894 — Traffic Signal Color**
Solve LeetCode Traffic Signal Color using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Traffic Signal Color |
| LeetCode | #3894 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer `timer` representing the remaining time (in seconds) on a traffic signal.

The signal follows these rules:

If `timer == 0`, the signal is `"Green"` 
 If `timer == 30`, the signal is `"Orange"` 
 If `30 < timer <= 90`, the signal is `"Red"`

Return the current state of the signal. If none of the above conditions are met, return `"Invalid"`.

## Constraints
- `0 <= timer <= 1000`

## Examples
### Example 1
- **Input:** `timer = 60`
- **Output:** `"Red"`
- **Explanation:** Since `timer = 60`, and `30 < timer <= 90`, the answer is `"Red"`.

### Example 2
- **Input:** `timer = 5`
- **Output:** `"Invalid"`
- **Explanation:** Since `timer = 5`, it does not satisfy any of the given conditions, the answer is `"Invalid"`.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Traffic Signal Color**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `timer = 60`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"Red"`.
4. **Verification:** Since `timer = 60`, and `30 < timer <= 90`, the answer is `"Red"`.

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
    def trafficSignal(self, timer: int) -> str:
        if timer == 0:
            return "Green"
        if timer == 30:
            return "Orange"
        if 30 < timer <= 90:
            return "Red"
        return "Invalid"
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
- [601. Human Traffic of Stadium](../../0501-1000/0601-human-traffic-of-stadium/)
- [4025. Minimize the Maximum Waiting Time at Synchronized Traffic Lights](../../4001-4500/4025-minimize-the-maximum-waiting-time-at-synchronized-traffic-lights/)
- [1812. Determine Color of a Chessboard Square](../../1501-2000/1812-determine-color-of-a-chessboard-square/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/traffic-signal-color/)
