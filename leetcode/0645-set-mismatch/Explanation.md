# Set Mismatch

## Problem Explanation
You have a set of integers `1` to `n`, but one of the numbers got duplicated (and consequently one is missing). Given the resulting array `nums`, find and return the duplicated number and the missing number as `[duplicate, missing]`.

## How the Code Works
The code uses a **HashSet** for straightforward detection.

1. **Find Duplicate:** It iterates through `nums`, adding each number to a `Set`. If a number is already in the set, it's the duplicate.
2. **Find Missing:** It loops from `1` to `n` and checks which number is not in the set — that's the missing number.

Time complexity is $O(N)$ and space complexity is $O(N)$.
