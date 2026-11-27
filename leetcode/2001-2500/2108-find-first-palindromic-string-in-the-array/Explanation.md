# LeetCode 2108: Find First Palindromic String in the Array

**LeetCode Problem #2108 — Find First Palindromic String in the Array**
Solve LeetCode Find First Palindromic String in the Array using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find First Palindromic String in the Array |
| LeetCode | #2108 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array of strings `words`, return *the first **palindromic** string in the array*. If there is no such string, return *an **empty string** *`""`.

A string is **palindromic** if it reads the same forward and backward.

## Constraints
- `1 <= words.length <= 100`
- `1 <= words[i].length <= 100`
- `words[i]` consists only of lowercase English letters.

## Examples
### Example 1
- **Input:** `words = ["abc","car","ada","racecar","cool"]`
- **Output:** `"ada"`
- **Explanation:** The first string that is palindromic is "ada".
Note that "racecar" is also palindromic, but it is not the first.

### Example 2
- **Input:** `words = ["notapalindrome","racecar"]`
- **Output:** `"racecar"`
- **Explanation:** The first and only string that is palindromic is "racecar".

### Example 3
- **Input:** `words = ["def","ghi"]`
- **Output:** `""`
- **Explanation:** There are no palindromic strings, so the empty string is returned.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Find First Palindromic String in the Array**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `words = ["abc","car","ada","racecar","cool"]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"ada"`.
4. **Verification:** The first string that is palindromic is "ada".
Note that "racecar" is also palindromic, but it is not the first.

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
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var firstPalindrome = function(words) {
    for (const word of words) {
        let left = 0;
        let right = word.length - 1;
        let isPalindrome = true;

        while (left < right) {
            if (word[left] !== word[right]) {
                isPalindrome = false;
                break;
            }

            left++;
            right--;
        }

        if (isPalindrome) {
            return word;
        }
    }

    return "";
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
- [28. Find the Index of the First Occurrence in a String](../../0001-0500/0028-find-the-index-of-the-first-occurrence-in-a-string/)
- [34. Find First and Last Position of Element in Sorted Array](../../0001-0500/0034-find-first-and-last-position-of-element-in-sorted-array/)
- [387. First Unique Character in a String](../../0001-0500/0387-first-unique-character-in-a-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-first-palindromic-string-in-the-array/)
