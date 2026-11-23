# LeetCode 4104: Count Valid Substrings II

**LeetCode Problem #4104 — Count Valid Substrings II**
Solve LeetCode Count Valid Substrings II using C++ and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Valid Substrings II |
| LeetCode | #4104 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s` consisting only of the characters `'a'`, `'b'`, and `'c'`.

A string is called **valid** if it does not contain `"abc"` as a ** subsequence **.

Return the number of **valid substrings ** in `s`. Substrings with different starting or ending indices are counted separately.

## Constraints
- `1 <= s.length <= 10^5`​​​​​​​
- `s` only consists of `'a'`, `'b'`, and `'c'` characters.

## Examples
### Example 1
- **Input:** `s = "abac"`
- **Output:** `9`
- **Explanation:** The following substrings don't contain `"abc"`​​​​​​​ as a subsequence: 

 
 `s[0..0] = "a"` 
 `s[0..1] = "ab"` 
 `s[0..2] = "aba"` 
 `s[1..1] = "b"` 
 `s[1..2] = "ba"` 
 `s[1..3] = "bac"` 
 `s[2..2] = "a"` 
 `s[2..3] = "ac"` 
 `s[3..3] = "c"` 
 

 Thus, the answer is 9.

### Example 2
- **Input:** `s = "abc"`
- **Output:** `5`
- **Explanation:** The following substrings don't contain `"abc"`​​​​​​​ as a subsequence: 

 
 `s[0..0] = "a"` 
 `s[0..1] = "ab"` 
 `s[1..1] = "b"` 
 `s[1..2] = "bc"` 
 `s[2..2] = "c"`​​​​​​​ 
 

 Thus, the answer is 5.

### Example 3
- **Input:** `s = "ac"`
- **Output:** `3`
- **Explanation:** All substrings in `s` don't contain `"abc"`​​​​​​​ as a subsequence. Thus, the answer is 3.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Count Valid Substrings II**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abac"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `9`.
4. **Verification:** The following substrings don't contain `"abc"`​​​​​​​ as a subsequence: 

 
 `s[0..0] = "a"` 
 `s[0..1] = "ab"` 
 `s[0..2] = "aba"` 
 `s[1..1] = "b"` 
 `s[1..2] = "ba"` 
 `s[1..3] = "bac"` 
 `s[2..2] = "a"` 
 `s[2..3] = "ac"` 
 `s[3..3] = "c"` 
 

 Thus, the answer is 9.

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
#include <string>
using namespace std;

class Solution {
public:
    long long countValidSubstrings(string s) {
        long long total = 0;
        int last_a = -1;
        int last_ab = -1;
        int invalid_start = -1; // Latest index i such that s[i..right] has subsequence "abc"
        
        for (int right = 0; right < (int)s.length(); ++right) {
            if (s[right] == 'a') {
                last_a = right;
            } else if (s[right] == 'b') {
                if (last_a != -1) {
                    last_ab = last_a;
                }
            } else if (s[right] == 'c') {
                if (last_ab != -1) {
                    invalid_start = last_ab;
                }
            }
            // Valid substrings ending at `right` start from (invalid_start + 1) to right
            total += (right - invalid_start);
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
- [4102. Count Valid Substrings I](../../4001-4500/4467-count-valid-substrings-i/)
- [696. Count Binary Substrings](../../0501-1000/0696-count-binary-substrings/)
- [828. Count Unique Characters of All Substrings of a Given String](../../0501-1000/0855-count-unique-characters-of-all-substrings-of-a-given-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-valid-substrings-ii/)
