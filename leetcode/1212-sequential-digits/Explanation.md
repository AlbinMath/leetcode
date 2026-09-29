# Sequential Digits

## Problem Explanation
An integer has sequential digits if each digit is one more than the previous digit (e.g., `123`, `2345`). Given a range `[low, high]`, return a sorted list of all integers with sequential digits in that range.

## How the Code Works
The code generates all possible sequential digit numbers and filters those within the range.

1. It starts from each digit `1` through `9` as the first digit.
2. For each starting digit, it builds numbers by appending the next consecutive digit (e.g., starting from `1`: `1 → 12 → 123 → 1234 → ...`).
3. If a generated number falls within `[low, high]`, it's added to the result.
4. The generation stops when the next digit exceeds `9` or the number exceeds `high`.
5. The result is sorted before returning.

Since there are at most 36 sequential-digit numbers (9 possible lengths × varying starts), this runs in $O(1)$ time.
