# Find The Minimum And Maximum Number Of Nodes Between Critical Points

## Problem Explanation
A critical point in a linked list is a local minima or local maxima. Return `[minDistance, maxDistance]` between any two critical points, or `[-1, -1]` if fewer than two critical points exist.

## How the Code Works
Traverse the linked list, tracking the position of each critical point (where `prev.val`, `curr.val`, `curr.next.val` form a local min or max). The minimum distance is between consecutive critical points; the maximum is between the first and last.
