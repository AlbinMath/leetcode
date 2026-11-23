# LeetCode 2744: Find Maximum Number of String Pairs

**LeetCode Problem #2744 — Find Maximum Number of String Pairs**
Solve LeetCode Find Maximum Number of String Pairs using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Maximum Number of String Pairs |
| LeetCode | #2744 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** array `words` consisting of **distinct** strings.

The string `words[i]` can be paired with the string `words[j]` if:

The string `words[i]` is equal to the reversed string of `words[j]`. 
 `0 <= i < j < words.length`.

Return *the **maximum** number of pairs that can be formed from the array *`words`*.*

Note that each string can belong in **at most one** pair.

## Constraints
- `1 <= words.length <= 50`
- `words[i].length == 2`
- `words` consists of distinct strings.
- `words[i]` contains only lowercase English letters.

## Examples
### Example 1
- **Input:** `words = ["cd","ac","dc","ca","zz"]`
- **Output:** `2`
- **Explanation:** In this example, we can form 2 pair of strings in the following way:
- We pair the 0^th string with the 2^nd string, as the reversed string of word[0] is "dc" and is equal to words[2].
- We pair the 1^st string with the 3^rd string, as the reversed string of word[1] is "ca" and is equal to words[3].
It can be proven that 2 is the maximum number of pairs that can be formed.

### Example 2
- **Input:** `words = ["ab","ba","cc"]`
- **Output:** `1`
- **Explanation:** In this example, we can form 1 pair of strings in the following way:
- We pair the 0^th string with the 1^st string, as the reversed string of words[1] is "ab" and is equal to words[0].
It can be proven that 1 is the maximum number of pairs that can be formed.

### Example 3
- **Input:** `words = ["aa","ab"]`
- **Output:** `0`
- **Explanation:** In this example, we are unable to form any pair of strings.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find Maximum Number of String Pairs**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `words = ["cd","ac","dc","ca","zz"]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** In this example, we can form 2 pair of strings in the following way:
- We pair the 0^th string with the 2^nd string, as the reversed string of word[0] is "dc" and is equal to words[2].
- We pair the 1^st string with the 3^rd string, as the reversed string of word[1] is "ca" and is equal to words[3].
It can be proven that 2 is the maximum number of pairs that can be formed.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var maximumNumberOfStringPairs = function(words) {
    const seen = new Set();
    let pairs = 0;

    for (const word of words) {
        const reversed = word[1] + word[0]; // words[i].length is always 2
        if (seen.has(reversed)) {
            pairs++;
        } else {
            seen.add(word);
        }
    }

    return pairs;
};
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
- [2058. Find the Minimum and Maximum Number of Nodes Between Critical Points](../../2001-2500/2182-find-the-minimum-and-maximum-number-of-nodes-between-critical-points/)
- [3020. Find the Maximum Number of Elements in Subset](../../3001-3500/3299-find-the-maximum-number-of-elements-in-subset/)
- [3113. Find the Number of Subarrays Where Boundary Elements Are Maximum](../../3001-3500/3382-find-the-number-of-subarrays-where-boundary-elements-are-maximum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-maximum-number-of-string-pairs/)
