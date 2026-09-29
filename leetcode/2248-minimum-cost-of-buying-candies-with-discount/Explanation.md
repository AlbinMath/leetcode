# Minimum Cost Of Buying Candies With Discount

## Problem Explanation
Buy candies where for every two you buy, you get the cheapest one free. Return the minimum cost.

## How the Code Works
Sort costs in descending order. Every third candy (index 2, 5, 8, ...) is free. Sum all costs except every third one.
