# LeetCode 2351: First Letter to Appear Twice

**LeetCode Problem #2351 — First Letter to Appear Twice**
Solve LeetCode First Letter to Appear Twice using Java and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | First Letter to Appear Twice |
| LeetCode | #2351 |
| Difficulty | Easy |
| Language | Java |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string `s` consisting of lowercase English letters, return *the first letter to appear **twice***.

**Note**:

A letter `a` appears twice before another letter `b` if the **second** occurrence of `a` is before the **second** occurrence of `b`. 
 `s` will contain at least one letter that appears twice.

## Constraints
- `2 <= s.length <= 100`
- `s` consists of lowercase English letters.
- `s` has at least one repeated letter.

## Examples
### Example 1
- **Input:** `s = "abccbaacz"`
- **Output:** `"c"`
- **Explanation:** The letter 'a' appears on the indexes 0, 5 and 6.
The letter 'b' appears on the indexes 1 and 4.
The letter 'c' appears on the indexes 2, 3 and 7.
The letter 'z' appears on the index 8.
The letter 'c' is the first letter to appear twice, because out of all the letters the index of its second occurrence is the smallest.

### Example 2
- **Input:** `s = "abcdd"`
- **Output:** `"d"`
- **Explanation:** The only letter that appears twice is 'd' so we return 'd'.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **First Letter to Appear Twice**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abccbaacz"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"c"`.
4. **Verification:** The letter 'a' appears on the indexes 0, 5 and 6.
The letter 'b' appears on the indexes 1 and 4.
The letter 'c' appears on the indexes 2, 3 and 7.
The letter 'z' appears on the index 8.
The letter 'c' is the first letter to appear twice, because out of all the letters the index of its second occurrence is the smallest.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Java

## Source Code
- [solution.java](./solution.java)


```java
class Solution {
    public char repeatedCharacter(String s) {
        boolean[] seen = new boolean[26];
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (seen[ch - 'a']) {
                return ch;
            }
            seen[ch - 'a'] = true;
        }
        return ' ';
    }
}
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3158. Find the XOR of Numbers Which Appear Twice](../../3001-3500/3428-find-the-xor-of-numbers-which-appear-twice/)
- [3374. First Letter Capitalization II](../../3501-4000/3711-first-letter-capitalization-ii/)
- [1967. Number of Strings That Appear as Substrings in Word](../../2001-2500/2099-number-of-strings-that-appear-as-substrings-in-word/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/first-letter-to-appear-twice/)
