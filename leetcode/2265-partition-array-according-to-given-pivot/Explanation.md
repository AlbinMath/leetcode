# Partition Array According To Given Pivot

## Problem Explanation
Rearrange `nums` so elements less than `pivot` come first, then elements equal to `pivot`, then elements greater. Maintain relative order within each group.

## How the Code Works
Three-pass approach: collect elements < pivot, then == pivot, then > pivot, and concatenate them. This maintains relative order within each partition.
