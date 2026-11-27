# LeetCode 2125: Number of Laser Beams in a Bank

**LeetCode Problem #2125 — Number of Laser Beams in a Bank**
Solve LeetCode Number of Laser Beams in a Bank using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Laser Beams in a Bank |
| LeetCode | #2125 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Anti-theft security devices are activated inside a bank. You are given a **0-indexed** binary string array `bank` representing the floor plan of the bank, which is an `m x n` 2D matrix. `bank[i]` represents the `i^th` row, consisting of `'0'`s and `'1'`s. `'0'` means the cell is empty, while`'1'` means the cell has a security device.

There is **one** laser beam between any **two** security devices **if both** conditions are met:

The two devices are located on two **different rows**: `r_1` and `r_2`, where `r_1 < r_2`. 
 For **each** row `i` where `r_1 < i < r_2`, there are **no security devices** in the `i^th` row.

Laser beams are independent, i.e., one beam does not interfere nor join with another.

Return *the total number of laser beams in the bank*.

## Constraints
- `m == bank.length`
- `n == bank[i].length`
- `1 <= m, n <= 500`
- `bank[i][j]` is either `'0'` or `'1'`.

## Examples
### Example 1
- **Input:** `bank = ["011001","000000","010100","001000"]`
- **Output:** `8`
- **Explanation:** Between each of the following device pairs, there is one beam. In total, there are 8 beams:
 * bank[0][1] -- bank[2][1]
 * bank[0][1] -- bank[2][3]
 * bank[0][2] -- bank[2][1]
 * bank[0][2] -- bank[2][3]
 * bank[0][5] -- bank[2][1]
 * bank[0][5] -- bank[2][3]
 * bank[2][1] -- bank[3][2]
 * bank[2][3] -- bank[3][2]
Note that there is no beam between any device on the 0^th row with any on the 3^rd row.
This is because the 2^nd row contains security devices, which breaks the second condition.

### Example 2
- **Input:** `bank = ["000","111","000"]`
- **Output:** `0`
- **Explanation:** There does not exist two devices located on two different rows.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Number of Laser Beams in a Bank**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `bank = ["011001","000000","010100","001000"]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `8`.
4. **Verification:** Between each of the following device pairs, there is one beam. In total, there are 8 beams:
 * bank[0][1] -- bank[2][1]
 * bank[0][1] -- bank[2][3]
 * bank[0][2] -- bank[2][1]
 * bank[0][2] -- bank[2][3]
 * bank[0][5] -- bank[2][1]
 * bank[0][5] -- bank[2][3]
 * bank[2][1] -- bank[3][2]
 * bank[2][3] -- bank[3][2]
Note that there is no beam between any device on the 0^th row with any on the 3^rd row.
This is because the 2^nd row contains security devices, which breaks the second condition.

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
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        prev = 0  # device count of the previous non-empty row
        for row in bank:
            cnt = row.count('1')
            if cnt:
                res += prev * cnt
                prev = cnt
        return res
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
- [1587. Bank Account Summary II](../../1501-2000/1587-bank-account-summary-ii/)
- [1716. Calculate Money in Leetcode Bank](../../1501-2000/1716-calculate-money-in-leetcode-bank/)
- [2043. Simple Bank System](../../2001-2500/2043-simple-bank-system/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-laser-beams-in-a-bank/)
