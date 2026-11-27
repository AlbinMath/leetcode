# LeetCode 1291: Sequential Digits

**LeetCode Problem #1291 — Sequential Digits**
Solve LeetCode Sequential Digits using C++ and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sequential Digits |
| LeetCode | #1291 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
An integer has *sequential digits* if and only if each digit in the number is one more than the previous digit.

Return a **sorted** list of all the integers in the range `[low, high]` inclusive that have sequential digits.

## Constraints
- `10 <= low <= high <= 10^9`

## Examples
### Example 1
- **Input:** `low = 100, high = 300`
- **Output:** `[123,234]`

### Example 2
- **Input:** `low = 1000, high = 13000`
- **Output:** `[1234,2345,3456,4567,5678,6789,12345]`

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code generates all possible sequential digit numbers and filters those within the range.

1. It starts from each digit `1` through `9` as the first digit.
2. For each starting digit, it builds numbers by appending the next consecutive digit (e.g., starting from `1`: `1 → 12 → 123 → 1234 → ...`).
3. If a generated number falls within `[low, high]`, it's added to the result.
4. The generation stops when the next digit exceeds `9` or the number exceeds `high`.
5. The result is sorted before returning.

Since there are at most 36 sequential-digit numbers (9 possible lengths × varying starts), this runs in $O(1)$ time.

## Algorithm
1. Initialize state variables / data structure (**Prefix Array**).
2. Process elements sequentially using **Prefix Sum Precomputation**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `low = 100, high = 300`.
2. **Processing Steps:** We apply **Prefix Sum Precomputation** using our **Prefix Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[123,234]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Prefix Array.

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
- Array

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    vector<int> sequentialDigits(int low, int high) {
        vector<int> ans;

        for (int start = 1; start <= 9; start++) {
            int num = 0;

            for (int digit = start; digit <= 9; digit++) {
                num = num * 10 + digit;

                if (num >= low && num <= high) {
                    ans.push_back(num);
                }
            }
        }

        sort(ans.begin(), ans.end());
        return ans;
    }
};
```

## Why This Works
By utilizing **Prefix Sum**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2453. Destroy Sequential Targets](../../2001-2500/2453-destroy-sequential-targets/)
- [2996. Smallest Missing Integer Greater Than Sequential Prefix Sum](../../2501-3000/2996-smallest-missing-integer-greater-than-sequential-prefix-sum/)
- [258. Add Digits](../../0001-0500/0258-add-digits/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sequential-digits/)
