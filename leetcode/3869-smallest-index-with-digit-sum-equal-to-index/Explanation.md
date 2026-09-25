# Smallest Index With Digit Sum Equal to Index

## Problem Explanation
You are given an integer array `nums`. You need to find the **smallest index** `i` in the array where the **sum of the digits** of the number at that index `nums[i]` is exactly equal to the index `i`. 

If no such index exists in the array, you must return `-1`.

For example, if `nums = [1, 10, 11]`:
- At index `0`: `nums[0] = 1`. Sum of digits = `1`. Not equal to `0`.
- At index `1`: `nums[1] = 10`. Sum of digits = `1 + 0 = 1`. Equal to index `1`!
Since we want the smallest index and we iterate from left to right, we can stop and return `1`.

## How the Code Works
The code uses a straightforward iterative approach.
1. It uses a `for` loop to iterate through the array from the first element (index `0`) to the last. This naturally ensures we find the smallest index first.
2. For each index `i`, it takes the number `nums[i]`.
3. It calculates the sum of the digits of the number using a `while` loop:
   - `num % 10` extracts the last digit of the number, which is added to `sum`.
   - `Math.floor(num / 10)` removes the last digit from the number.
   - This repeats until all digits have been processed and `num` becomes 0.
4. It compares the calculated `sum` with the current index `i`.
   - If `sum === i`, it immediately returns `i`, fulfilling the condition of finding the smallest index.
5. If the loop finishes checking all elements without returning, it means no such index exists, so it returns `-1`.
