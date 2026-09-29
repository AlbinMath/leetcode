# Find The Highest Altitude

## Problem Explanation
A biker starts at altitude `0` and goes through `n+1` points. `gain[i]` is the altitude change between point `i` and `i+1`. Return the highest altitude reached.

## How the Code Works
The code simply accumulates the altitude by adding each gain value to a running sum, tracking the maximum value encountered. Start at `0`, add each `gain[i]`, and keep updating the highest altitude.

Time complexity is $O(N)$ and space complexity is $O(1)$.
