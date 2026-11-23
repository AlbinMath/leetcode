# LeetCode 1227: Airplane Seat Assignment Probability

**LeetCode Problem #1227 — Airplane Seat Assignment Probability**
Solve LeetCode Airplane Seat Assignment Probability using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Airplane Seat Assignment Probability |
| LeetCode | #1227 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
`n` passengers board an airplane with exactly `n` seats. The first passenger has lost the ticket and picks a seat randomly. But after that, the rest of the passengers will:

Take their own seat if it is still available, and 
 Pick other seats randomly when they find their seat occupied

Return *the probability that the *`n^th`* person gets his own seat*.

## Constraints
- `1 <= n <= 10^5`

## Examples
### Example 1
- **Input:** `n = 1`
- **Output:** `1.00000`
- **Explanation:** The first person can only get the first seat.

### Example 2
- **Input:** `n = 2`
- **Output:** `0.50000`
- **Explanation:** The second person has a probability of 0.5 to get the second seat (when first person gets the first seat).

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Airplane Seat Assignment Probability**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 1`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1.00000`.
4. **Verification:** The first person can only get the first seat.

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
    def nthPersonGetsNthSeat(self, n: int) -> float:
        return 1.0 if n == 1 else 0.5
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
- [688. Knight Probability in Chessboard](../../0501-1000/0688-knight-probability-in-chessboard/)
- [1467. Probability of a Two Boxes Having The Same Number of Distinct Balls](../../1501-2000/1577-probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/)
- [1514. Path with Maximum Probability](../../1001-1500/1325-path-with-maximum-probability/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/airplane-seat-assignment-probability/)
