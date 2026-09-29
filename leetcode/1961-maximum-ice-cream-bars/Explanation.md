# Maximum Ice Cream Bars

## Problem Explanation
Given ice cream bar costs and available coins, return the maximum number of bars you can buy.

## How the Code Works
1. **Sort** the costs in ascending order.
2. **Greedy:** Buy the cheapest bars first. Iterate through sorted costs, subtracting each cost from coins. Stop when you can't afford the next bar.
3. Return the count.

Time complexity is $O(N \log N)$ and space complexity is $O(\log N)$.
