# Smallest Missing Multiple Of K

## Problem Explanation
You are given an integer array `nums` and an integer `k`. You need to find the **smallest positive multiple** of `k` that is **not** present in the `nums` array. A multiple of `k` is any positive integer that is divisible by `k` (e.g., `k, 2k, 3k, 4k`, etc.).

For example, if `nums = [8, 2, 3, 4, 6]` and `k = 2`:
- The multiples of 2 are `2, 4, 6, 8, 10, ...`
- `2` is in the array.
- `4` is in the array.
- `6` is in the array.
- `8` is in the array.
- `10` is **not** in the array.
So, the smallest missing multiple of 2 is `10`.

## How the Code Works
The code uses a `HashSet` to efficiently check for the presence of numbers in $O(1)$ time.
1. First, it converts the `nums` array into a `HashSet<int>` called `set`. This allows us to quickly look up whether a number exists in the array without having to scan the entire array every time.
2. It initializes a variable `multiple` to the first multiple, which is `k`.
3. It uses a `while` loop to continuously check if `set` contains the current `multiple`.
   - If it does, we increment the `multiple` by `k` to check the next multiple (`2k`, `3k`, etc.).
4. The loop stops as soon as it finds a `multiple` that is **not** in the `HashSet`.
5. Finally, it returns that missing `multiple`.

This approach is highly efficient. Converting the array to a HashSet takes $O(N)$ time (where $N$ is the number of elements in `nums`), and the while loop takes at most $O(N)$ steps because there can be at most $N$ multiples of $k$ present in the array. Therefore, the overall time complexity is $O(N)$ and the space complexity is $O(N)$.
