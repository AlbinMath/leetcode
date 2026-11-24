# LeetCode 4102: Count Valid Substrings I

**LeetCode Problem #4102 — Count Valid Substrings I**
Solve LeetCode Count Valid Substrings I using C++ and Sliding Window. This solution finds the optimal result using Dynamic Sliding Window Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Valid Substrings I |
| LeetCode | #4102 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Dynamic Sliding Window Traversal |
| Data Structure | Array / Hash Set |
| Pattern | Sliding Window |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s` consisting only of the characters `'a'`, `'b'`, and `'c'`.

A string is called **valid** if it does not contain `"abc"` as a ** substring **.

Return the number of **valid substrings** in `s`. Substrings with different starting or ending indices are counted separately.

## Constraints
- `1 <= s.length <= 10^5`​​​​​​​
- `s` only consists of `'a'`, `'b'`, and `'c'` characters.

## Examples
### Example 1
- **Input:** `s = "abac"`
- **Output:** `10`
- **Explanation:** The following substrings don't contain `"abc"`​​​​​​​ as a substring: 

 
 `s[0..0] = "a"` 
 `s[0..1] = "ab"` 
 `s[0..2] = "aba"` 
 `s[0..3] = "abac"`​​​​​​​ 
 `s[1..1] = "b"` 
 `s[1..2] = "ba"` 
 `s[1..3] = "bac"` 
 `s[2..2] = "a"` 
 `s[2..3] = "ac"` 
 `s[3..3] = "c"` 
 

 Thus, the answer is 10.

### Example 2
- **Input:** `s = "abc"`
- **Output:** `5`
- **Explanation:** The following substrings don't contain `"abc"`​​​​​​​ as a substring: 

 
 `s[0..0] = "a"` 
 `s[0..1] = "ab"` 
 `s[1..1] = "b"` 
 `s[1..2] = "bc"` 
 `s[2..2] = "c"`​​​​​​​ 
 

 Thus, the answer is 5.

### Example 3
- **Input:** `s = "ac"`
- **Output:** `3`
- **Explanation:** All substrings in `s` don't contain `"abc"` as a substring​​​​​​​. Thus, the answer is 3.

## Key Insight
Maintain a dynamic contiguous window with two pointers (`left` and `right`), expanding to include new elements and shrinking when window invariants are violated.

## Approach
To solve **Count Valid Substrings I**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abac"`.
2. **Processing Steps:** We apply **Dynamic Sliding Window Traversal** using our **Array / Hash Set**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `10`.
4. **Verification:** The following substrings don't contain `"abc"`​​​​​​​ as a substring: 

 
 `s[0..0] = "a"` 
 `s[0..1] = "ab"` 
 `s[0..2] = "aba"` 
 `s[0..3] = "abac"`​​​​​​​ 
 `s[1..1] = "b"` 
 `s[1..2] = "ba"` 
 `s[1..3] = "bac"` 
 `s[2..2] = "a"` 
 `s[2..3] = "ac"` 
 `s[3..3] = "c"` 
 

 Thus, the answer is 10.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array / Hash Set.

## Pattern
**Sliding Window**

## Topics
- Sliding Window
- Two Pointers
- Subarrays

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
        int left = 0;
        int n = s.length();
        
        for (int right = 0; right < n; ++right) {
            // If the last 3 characters form "abc", shrink the window
            if (right >= 2 && s[right - 2] == 'a' && s[right - 1] == 'b' && s[right] == 'c') {
                left = right - 1;
            }
            // All substrings starting between left and right and ending at right are valid
            total += (right - left + 1);
        }
        
        return total;
    }
};
```

## Why This Works
By utilizing **Sliding Window**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Shrinking the window too late or missing invalid state checks.
2. Forgetting to update window metrics (e.g. char counts) during contraction.
3. Misinterpreting fixed vs variable window requirements.

## Interview Notes
- **Tests:** Two-pointer window management, state tracking, and contiguous subarray analysis.
- **Follow-up:** How do you handle non-positive integer values in subarray sum windows?

## Related Problems
- [4104. Count Valid Substrings II](../../4001-4500/4468-count-valid-substrings-ii/)
- [1359. Count All Valid Pickup and Delivery Options](../../1001-1500/1461-count-all-valid-pickup-and-delivery-options/)
- [2267.  Check if There Is a Valid Parentheses String Path](../../2001-2500/2349-check-if-there-is-a-valid-parentheses-string-path/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-valid-substrings-i/)
