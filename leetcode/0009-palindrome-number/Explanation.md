# 0009 - Palindrome Number

## Approach
If the number is negative, it cannot be a palindrome (due to the minus sign), so we return `False`.
We store the `original` number and create a `reversed_num` variable initialized to `0`.
Using a `while` loop, we extract the last digit of the number using modulo 10 (`x % 10`) and append it to `reversed_num` by multiplying the current `reversed_num` by 10 and adding the digit.
Then, we remove the last digit from `x` using integer division (`x //= 10`).
Finally, we check if the `original` number is equal to the `reversed_num`.

## Complexity
- **Time Complexity:** $O(\log_{10}(N))$ because we divide the number by 10 in each iteration, which corresponds to the number of digits.
- **Space Complexity:** $O(1)$ since we only use a few variables to store the reversed number and digits.
