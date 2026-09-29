# Cinema Seat Allocation

## Problem Explanation
A cinema has `n` rows, each with 10 seats. Given a list of reserved seats, determine the maximum number of four-person groups that can be seated. A group occupies 4 consecutive seats and can fit in columns 2–5, 4–7, or 6–9.

## How the Code Works
The code uses **Bitmasks** for efficient seat tracking.

1. **Bitmask per Row:** For each reserved seat, set the corresponding bit in a bitmask for that row. Only rows with reservations are stored in a hash map.
2. **Unreserved Rows:** Rows without any reservations can always fit 2 groups (left: seats 2–5, right: seats 6–9). Contribute `2 * (n - reservedRows)`.
3. **Reserved Rows:** For each row with reservations, check three possible group positions using bitwise AND:
   - **Left** (seats 2–5): bits 2,3,4,5 must be free.
   - **Middle** (seats 4–7): bits 4,5,6,7 must be free.
   - **Right** (seats 6–9): bits 6,7,8,9 must be free.
   - If both left and right fit → 2 groups. Else if any one fits → 1 group.

Time complexity is $O(R)$ where $R$ is the number of reserved seats, and space complexity is $O(R)$.
