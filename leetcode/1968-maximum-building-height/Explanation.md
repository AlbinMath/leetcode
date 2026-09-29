# Maximum Building Height

## Problem Explanation
You want to build `n` buildings where building 1 has height 0, adjacent buildings differ in height by at most 1, and some buildings have maximum height restrictions. Return the maximum possible height of any building.

## How the Code Works
The code uses **two-pass constraint propagation**.

1. Add restriction `[1, 0]` (building 1 must be height 0) and sort by building ID.
2. **Left-to-right pass:** Each restriction is tightened so it doesn't exceed the previous restriction's height + distance between them.
3. **Right-to-left pass:** Same tightening from the other direction.
4. **Calculate peaks:** Between each pair of consecutive restricted buildings, the maximum achievable peak is `(h1 + h2 + distance) / 2`.
5. Also check the height achievable after the last restriction (increases by 1 per building up to building `n`).

Time complexity is $O(M \log M)$ where $M$ is the number of restrictions, and space complexity is $O(M)$.
