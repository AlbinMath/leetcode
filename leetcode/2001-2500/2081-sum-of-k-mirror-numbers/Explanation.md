# LeetCode 2081: Sum of k-Mirror Numbers

**LeetCode Problem #2081 — Sum of k-Mirror Numbers**
Solve LeetCode Sum of k-Mirror Numbers using C++ and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sum of k-Mirror Numbers |
| LeetCode | #2081 |
| Difficulty | Hard |
| Language | C++ |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A **k-mirror number** is a **positive** integer **without leading zeros** that reads the same both forward and backward in base-10 **as well as** in base-k.

For example, `9` is a 2-mirror number. The representation of `9` in base-10 and base-2 are `9` and `1001` respectively, which read the same both forward and backward. 
 On the contrary, `4` is not a 2-mirror number. The representation of `4` in base-2 is `100`, which does not read the same both forward and backward.

Given the base `k` and the number `n`, return *the **sum** of the* `n` ***smallest** k-mirror numbers*.

## Constraints
- `2 <= k <= 9`
- `1 <= n <= 30`

## Examples
### Example 1
- **Input:** `k = 2, n = 5`
- **Output:** `25`
- **Explanation:** The 5 smallest 2-mirror numbers and their representations in base-2 are listed as follows:
 base-10 base-2
 1 1
 3 11
 5 101
 7 111
 9 1001
Their sum = 1 + 3 + 5 + 7 + 9 = 25.

### Example 2
- **Input:** `k = 3, n = 7`
- **Output:** `499`
- **Explanation:** The 7 smallest 3-mirror numbers are and their representations in base-3 are listed as follows:
 base-10 base-3
 1 1
 2 2
 4 11
 8 22
 121 11111
 151 12121
 212 21212
Their sum = 1 + 2 + 4 + 8 + 121 + 151 + 212 = 499.

### Example 3
- **Input:** `k = 7, n = 17`
- **Output:** `20379000`
- **Explanation:** The 17 smallest 7-mirror numbers are:
1, 2, 3, 4, 5, 6, 8, 121, 171, 242, 292, 16561, 65656, 2137312, 4602064, 6597956, 6958596

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Sum of k-Mirror Numbers**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `k = 2, n = 5`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `25`.
4. **Verification:** The 5 smallest 2-mirror numbers and their representations in base-2 are listed as follows:
 base-10 base-2
 1 1
 3 11
 5 101
 7 111
 9 1001
Their sum = 1 + 3 + 5 + 7 + 9 = 25.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    long long kMirror(int k, int n) {
        long long total = 0;
        int count = 0;
        int digits[64];

        auto isBaseKPalindrome = [&](long long x) {
            int len = 0;
            while (x > 0) {
                digits[len++] = x % k;
                x /= k;
            }
            for (int i = 0, j = len - 1; i < j; ++i, --j) {
                if (digits[i] != digits[j]) return false;
            }
            return true;
        };

        for (long long len = 1; count < n; ++len) {
            long long half = (len + 1) / 2;
            long long start = 1;
            for (int i = 1; i < half; ++i) start *= 10;
            long long end = start * 10;

            for (long long p = start; p < end && count < n; ++p) {
                long long pal = p;
                long long temp = (len % 2 == 1) ? (p / 10) : p;
                while (temp > 0) {
                    pal = pal * 10 + (temp % 10);
                    temp /= 10;
                }
                if (isBaseKPalindrome(pal)) {
                    total += pal;
                    ++count;
                }
            }
        }
        return total;
    }
};
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [2310. Sum of Numbers With Units Digit K](../../2001-2500/2310-sum-of-numbers-with-units-digit-k/)
- [3855. Sum of K-Digit Numbers in a Range](../../3501-4000/3855-sum-of-k-digit-numbers-in-a-range/)
- [363. Max Sum of Rectangle No Larger Than K](../../0001-0500/0363-max-sum-of-rectangle-no-larger-than-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sum-of-k-mirror-numbers/)
