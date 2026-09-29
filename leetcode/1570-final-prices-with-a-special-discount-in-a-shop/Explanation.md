# Final Prices With A Special Discount In A Shop

## Problem Explanation
Given prices, for each item `i`, find the first item `j > i` where `prices[j] <= prices[i]`. The final price of item `i` is `prices[i] - prices[j]`. If no such `j` exists, no discount is applied.

## How the Code Works
The code uses a **Monotonic Stack** to efficiently find the next smaller or equal element for each index. It processes prices left to right, maintaining a stack of indices with unresolved discounts. When a price that qualifies as a discount is found, all applicable items on the stack get their discount applied.

Time complexity is $O(N)$ and space complexity is $O(N)$.
