# Rotated Digits

## Problem Explanation
A number is considered "good" if after rotating each digit individually by 180 degrees, it becomes a **different** valid number. Digits `0, 1, 8` look the same after rotation, digits `2, 5, 6, 9` become valid different digits, and digits `3, 4, 7` are invalid after rotation. Given an integer `n`, count how many numbers from `1` to `n` are "good."

## How the Code Works
The code checks each number from `1` to `n` individually.

1. For each number, it extracts digits one by one using `x % 10` and `x /= 10`.
2. It tracks two flags:
   - `valid`: Remains `true` unless a digit `3`, `4`, or `7` is found (which makes the number invalid after rotation).
   - `different`: Set to `true` if any digit is `2`, `5`, `6`, or `9` (meaning the rotated number differs from the original).
3. A number is "good" only if `valid && different` — it must be valid after rotation AND actually change.

Time complexity is $O(N \log N)$ (each number has at most $\log_{10}(N)$ digits) and space complexity is $O(1)$.
