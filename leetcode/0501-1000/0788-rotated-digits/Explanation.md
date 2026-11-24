# LeetCode 788: Rotated Digits

**LeetCode Problem #788 — Rotated Digits**
Solve LeetCode Rotated Digits using C++ and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Rotated Digits |
| LeetCode | #788 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
An integer `x` is a **good** if after rotating each digit individually by 180 degrees, we get a valid number that is different from `x`. Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. For example:

`0`, `1`, and `8` rotate to themselves, 
 `2` and `5` rotate to each other (in this case they are rotated in a different direction, in other words, `2` or `5` gets mirrored), 
 `6` and `9` rotate to each other, and 
 the rest of the numbers do not rotate to any other number and become invalid.

Given an integer `n`, return *the number of **good** integers in the range *`[1, n]`.

## Constraints
- `1 <= n <= 10^4`

## Examples
### Example 1
- **Input:** `n = 10`
- **Output:** `4`
- **Explanation:** There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.

### Example 2
- **Input:** `n = 1`
- **Output:** `0`

### Example 3
- **Input:** `n = 2`
- **Output:** `1`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
The code checks each number from `1` to `n` individually.

1. For each number, it extracts digits one by one using `x % 10` and `x /= 10`.
2. It tracks two flags:
   - `valid`: Remains `true` unless a digit `3`, `4`, or `7` is found (which makes the number invalid after rotation).
   - `different`: Set to `true` if any digit is `2`, `5`, `6`, or `9` (meaning the rotated number differs from the original).
3. A number is "good" only if `valid && different` — it must be valid after rotation AND actually change.

Time complexity is $O(N \log N)$ (each number has at most $\log_{10}(N)$ digits) and space complexity is $O(1)$.

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `n = 10`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Sorted Array.

## Pattern
**Binary Search**

## Topics
- Binary Search
- Divide and Conquer
- Search Space

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    int rotatedDigits(int n) {
        int count = 0;

        for (int i = 1; i <= n; i++) {
            int x = i;
            bool valid = true;
            bool different = false;

            while (x > 0) {
                int digit = x % 10;

                // Invalid after rotation
                if (digit == 3 || digit == 4 || digit == 7) {
                    valid = false;
                    break;
                }

                // These digits change after rotation
                if (digit == 2 || digit == 5 || digit == 6 || digit == 9) {
                    different = true;
                }

                x /= 10;
            }

            if (valid && different) {
                count++;
            }
        }

        return count;
    }
};
```

## Why This Works
By utilizing **Binary Search**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Applying standard binary search without accounting for array rotation or duplicates.
2. Off-by-one errors when updating boundary pointers (`left = mid + 1` vs `right = mid - 1`).
3. Integer overflow during midpoint calculation (use `mid = left + (right - left) // 2`).

## Interview Notes
- **Tests:** Logarithmic search space reduction, boundary handling, and invariant preservation.
- **Follow-up:** How does performance change if the array contains duplicate elements?

## Related Problems
- [258. Add Digits](../../0001-0500/0258-add-digits/)
- [357. Count Numbers with Unique Digits](../../0001-0500/0357-count-numbers-with-unique-digits/)
- [402. Remove K Digits](../../0001-0500/0402-remove-k-digits/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/rotated-digits/)
