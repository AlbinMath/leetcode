# LeetCode 1386: Cinema Seat Allocation

**LeetCode Problem #1386 — Cinema Seat Allocation**
Solve LeetCode Cinema Seat Allocation using C++, Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Cinema Seat Allocation |
| LeetCode | #1386 |
| Difficulty | Medium |
| Language | C++, Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
A cinema has `n` rows of seats, numbered from 1 to `n`. Each row has 10 seats, numbered from 1 to 10.

You are given a 2D integer array reservedSeats , where reservedSeats[i] = [row_i, seat_i] means that seat seat_i in row row_i is already reserved.

A four-person group must be assigned to four seats in the **same** row. The group can be seated in one of the following seat blocks:

seats 2, 3, 4, 5 
 seats 4, 5, 6, 7 
 seats 6, 7, 8, 9

A block can be used only if **none** of its seats are reserved. Each seat can be assigned to **at most **one group.

Return an integer denoting the **maximum** number of four-person groups that can be assigned.

## Constraints
- `1 <= n <= 10^9`
- `1 <= reservedSeats.length <= min(10 * n, 10^4)`
- `reservedSeats[i] == [row_i, seat_i]`
- `1 <= row_i <= n`
- `1 <= seat_i <= 10`
- All `reservedSeats[i]` are distinct.

## Examples
### Example 1
- **Input:** `n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]`
- **Output:** `4`
- **Explanation:** The figure above shows an optimal allocation of four groups. Seats marked in blue are already reserved, and each set of four contiguous seats marked in orange is assigned to one group.

### Example 2
- **Input:** `n = 2, reservedSeats = [[2,1],[1,8],[2,6]]`
- **Output:** `2`

### Example 3
- **Input:** `n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]]`
- **Output:** `4`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
The code uses **Bitmasks** for efficient seat tracking.

1. **Bitmask per Row:** For each reserved seat, set the corresponding bit in a bitmask for that row. Only rows with reservations are stored in a hash map.
2. **Unreserved Rows:** Rows without any reservations can always fit 2 groups (left: seats 2–5, right: seats 6–9). Contribute `2 * (n - reservedRows)`.
3. **Reserved Rows:** For each row with reservations, check three possible group positions using bitwise AND:
   - **Left** (seats 2–5): bits 2,3,4,5 must be free.
   - **Middle** (seats 4–7): bits 4,5,6,7 must be free.
   - **Right** (seats 6–9): bits 6,7,8,9 must be free.
   - If both left and right fit → 2 groups. Else if any one fits → 1 group.

Time complexity is $O(R)$ where $R$ is the number of reserved seats, and space complexity is $O(R)$.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The figure above shows an optimal allocation of four groups. Seats marked in blue are already reserved, and each set of four contiguous seats marked in orange is assigned to one group.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
C++, Python

## Source Code
- [solution.cpp](./solution.cpp)
- [solution.py](./solution.py)


### C++
```cpp
class Solution {
public:
    int maxNumberOfFamilies(int n, vector<vector<int>>& reservedSeats) {
        unordered_map<int, int> rows;

        // Store reserved seats as a bitmask for each row
        for (auto &seat : reservedSeats) {
            int row = seat[0];
            int col = seat[1];

            rows[row] |= (1 << col);
        }

        // Rows without reservations can fit 2 groups
        long long ans = 2LL * (n - rows.size());

        for (auto &[row, mask] : rows) {
            // Seats 2,3,4,5
            bool left = (mask & ((1 << 2) |
                                (1 << 3) |
                                (1 << 4) |
                                (1 << 5))) == 0;

            // Seats 4,5,6,7
            bool middle = (mask & ((1 << 4) |
                                   (1 << 5) |
                                   (1 << 6) |
                                   (1 << 7))) == 0;

            // Seats 6,7,8,9
            bool right = (mask & ((1 << 6) |
                                  (1 << 7) |
                                  (1 << 8) |
                                  (1 << 9))) == 0;

            if (left && right) {
                // Two non-overlapping groups
                ans += 2;
            }
            else if (left || middle || right) {
                // Only one group can fit
                ans += 1;
            }
        }

        return (int)ans;
    }
};
```

### Python
```python
from collections import defaultdict
from typing import List

class Solution:
    def maxNumberOfFamilies(
        self, n: int, reservedSeats: List[List[int]]
    ) -> int:
        rows = defaultdict(int)

        # Record reserved seats using bits 1 through 10
        for row, seat in reservedSeats:
            rows[row] |= 1 << seat

        # Seat blocks: 2-5, 4-7, 6-9
        left =  sum(1 << s for s in range(2, 6))
        middle = sum(1 << s for s in range(4, 8))
        right = sum(1 << s for s in range(6, 10))

        result = 2 * n

        for mask in rows.values():
            left_free = (mask & left) == 0
            middle_free = (mask & middle) == 0
            right_free = (mask & right) == 0

            if left_free and right_free:
                # Two families fit in this row
                continue
            elif left_free or middle_free or right_free:
                # Only one family fits
                result -= 1
            else:
                # No family fits
                result -= 2

        return result
```

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [1227. Airplane Seat Assignment Probability](../../1001-1500/1227-airplane-seat-assignment-probability/)
- [1845. Seat Reservation Manager](../../1501-2000/1845-seat-reservation-manager/)
- [2037. Minimum Number of Moves to Seat Everyone](../../2001-2500/2037-minimum-number-of-moves-to-seat-everyone/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/cinema-seat-allocation/)
