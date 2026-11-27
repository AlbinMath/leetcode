# LeetCode 3090: Maximum Length Substring With Two Occurrences

**LeetCode Problem #3090 — Maximum Length Substring With Two Occurrences**
Solve LeetCode Maximum Length Substring With Two Occurrences using Swift and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Length Substring With Two Occurrences |
| LeetCode | #3090 |
| Difficulty | Easy |
| Language | Swift |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string `s`, return the **maximum** length of a substring such that it contains *at most two occurrences* of each character.

## Constraints
- `2 <= s.length <= 100`
- `s` consists only of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "bcbbbcba"`
- **Output:** `4`
- **Explanation:** The following substring has a length of 4 and contains at most two occurrences of each character: `"bcbb bcba "`.

### Example 2
- **Input:** `s = "aaaa"`
- **Output:** `2`
- **Explanation:** The following substring has a length of 2 and contains at most two occurrences of each character: `" aa aa"`.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximum Length Substring With Two Occurrences**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "bcbbbcba"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The following substring has a length of 4 and contains at most two occurrences of each character: `"bcbb bcba "`.

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
Swift

## Source Code
- [solution.swift](./solution.swift)


```swift
class Solution {
    func maximumLengthSubstring(_ s: String) -> Int {
        let chars = Array(s)
        var count = [Int](repeating: 0, count: 26)
        
        var left = 0
        var ans = 0
        
        for right in 0..<chars.count {
            let index = Int(chars[right].asciiValue! - Character("a").asciiValue!)
            count[index] += 1
            
            while count[index] > 2 {
                let leftIndex = Int(chars[left].asciiValue! - Character("a").asciiValue!)
                count[leftIndex] -= 1
                left += 1
            }
            
            ans = max(ans, right - left + 1)
        }
        
        return ans
    }
}
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
- [1297. Maximum Number of Occurrences of a Substring](../../1001-1500/1297-maximum-number-of-occurrences-of-a-substring/)
- [1456. Maximum Number of Vowels in a Substring of Given Length](../../1001-1500/1456-maximum-number-of-vowels-in-a-substring-of-given-length/)
- [1960. Maximum Product of the Length of Two Palindromic Substrings](../../1501-2000/1960-maximum-product-of-the-length-of-two-palindromic-substrings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/)
