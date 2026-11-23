# LeetCode 3612: Process String with Special Operations I

**LeetCode Problem #3612 — Process String with Special Operations I**
Solve LeetCode Process String with Special Operations I using Java and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Process String with Special Operations I |
| LeetCode | #3612 |
| Difficulty | Medium |
| Language | Java |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s` consisting of lowercase English letters and the special characters: `*`, `#`, and `%`.

Build a new string `result` by processing `s` according to the following rules from left to right:

If the letter is a **lowercase** English letter append it to `result`. 
 A `'*'` **removes** the last character from `result`, if it exists. 
 A `'#'` **duplicates** the current `result` and **appends** it to itself. 
 A `'%'` **reverses** the current `result`.

Return the final string `result` after processing all characters in `s`.

## Constraints
- `1 <= s.length <= 20`
- `s` consists of only lowercase English letters and special characters `*`, `#`, and `%`.

## Examples
### Example 1
- **Input:** `s = "a#b%*"`
- **Output:** `"ba"`
- **Explanation:** `i` 
 `s[i]` 
 Operation 
 Current `result` 
 
 
 
 
 0 
 `'a'` 
 Append `'a'` 
 `"a"` 
 
 
 1 
 `'#'` 
 Duplicate `result` 
 `"aa"` 
 
 
 2 
 `'b'` 
 Append `'b'` 
 `"aab"` 
 
 
 3 
 `'%'` 
 Reverse `result` 
 `"baa"` 
 
 
 4 
 `'*'` 
 Remove the last character 
 `"ba"` 
 
 
 

 Thus, the final `result` is `"ba"`.

### Example 2
- **Input:** `s = "z*#"`
- **Output:** `""`
- **Explanation:** `i` 
 `s[i]` 
 Operation 
 Current `result` 
 
 
 
 
 0 
 `'z'` 
 Append `'z'` 
 `"z"` 
 
 
 1 
 `'*'` 
 Remove the last character 
 `""` 
 
 
 2 
 `'#'` 
 Duplicate the string 
 `""` 
 
 
 

 Thus, the final `result` is `""`.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Process String with Special Operations I**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "a#b%*"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"ba"`.
4. **Verification:** `i` 
 `s[i]` 
 Operation 
 Current `result` 
 
 
 
 
 0 
 `'a'` 
 Append `'a'` 
 `"a"` 
 
 
 1 
 `'#'` 
 Duplicate `result` 
 `"aa"` 
 
 
 2 
 `'b'` 
 Append `'b'` 
 `"aab"` 
 
 
 3 
 `'%'` 
 Reverse `result` 
 `"baa"` 
 
 
 4 
 `'*'` 
 Remove the last character 
 `"ba"` 
 
 
 

 Thus, the final `result` is `"ba"`.

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
Java

## Source Code
- [solution.java](./solution.java)


```java
class Solution {
    public String processStr(String s) {
        StringBuilder result = new StringBuilder();

        for (char c : s.toCharArray()) {
            if (c >= 'a' && c <= 'z') {
                // Append character
                result.append(c);

            } else if (c == '*') {
                // Remove last character if it exists
                if (result.length() > 0) {
                    result.deleteCharAt(result.length() - 1);
                }

            } else if (c == '#') {
                // Duplicate current result
                result.append(result);

            } else if (c == '%') {
                // Reverse current result
                result.reverse();
            }
        }

        return result.toString();
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
- [3614. Process String with Special Operations II](../../3501-4000/3939-process-string-with-special-operations-ii/)
- [761. Special Binary String](../../0501-1000/0763-special-binary-string/)
- [1585. Check If String Is Transformable With Substring Sort Operations](../../1501-2000/1707-check-if-string-is-transformable-with-substring-sort-operations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/process-string-with-special-operations-i/)
