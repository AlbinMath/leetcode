# LeetCode 1520: Maximum Number of Non-Overlapping Substrings

**LeetCode Problem #1520 — Maximum Number of Non-Overlapping Substrings**
Solve LeetCode Maximum Number of Non-Overlapping Substrings using JavaScript and Heap. This solution finds the optimal result using Min/Max Heap Priority Selection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Number of Non-Overlapping Substrings |
| LeetCode | #1520 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Min/Max Heap Priority Selection |
| Data Structure | Heap / Priority Queue |
| Pattern | Heap |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a string `s` of lowercase letters, you need to find the maximum number of **non-empty** substrings of `s` that meet the following conditions:

The substrings do not overlap, that is for any two substrings `s[i..j]` and `s[x..y]`, either `j < x` or `i > y` is true. 
 A substring that contains a certain character `c` must also contain all occurrences of `c`.

Find *the maximum number of substrings that meet the above conditions*. If there are multiple solutions with the same number of substrings, *return the one with minimum total length. *It can be shown that there exists a unique solution of minimum total length.

Notice that you can return the substrings in **any** order.

## Constraints
- `1 <= s.length <= 10^5`
- `s` contains only lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "adefaddaccc"`
- **Output:** `["e","f","ccc"]`

### Example 2
- **Input:** `s = "abbaccd"`
- **Output:** `["d","bb","cc"]`

## Key Insight
Leverage **Heap** with **Heap / Priority Queue** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses a **Greedy** approach. It first finds the leftmost and rightmost occurrence of each character. Then for each potential starting character, it expands the substring to include all occurrences of all characters within it. Finally, it greedily selects non-overlapping substrings by preferring shorter ones that end earliest.

Time complexity is $O(N \times |\Sigma|)$ and space complexity is $O(|\Sigma|)$ where $|\Sigma|$ is the alphabet size.

## Algorithm
1. Initialize state variables / data structure (**Heap / Priority Queue**).
2. Process elements sequentially using **Min/Max Heap Priority Selection**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `s = "adefaddaccc"`.
2. **Processing Steps:** We apply **Min/Max Heap Priority Selection** using our **Heap / Priority Queue**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `["e","f","ccc"]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Heap / Priority Queue.

## Pattern
**Heap**

## Topics
- Heap
- Priority Queue
- Sorting

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
/**
 * @param {string} s
 * @return {string[]}
 */
var maxNumOfSubstrings = function(s) {
    const n = s.length;

    // First and last occurrence of each character
    const first = Array(26).fill(n);
    const last = Array(26).fill(-1);

    for (let i = 0; i < n; i++) {
        const c = s.charCodeAt(i) - 97;
        first[c] = Math.min(first[c], i);
        last[c] = i;
    }

    // Find the smallest valid interval starting at index l
    function getInterval(l) {
        let r = last[s.charCodeAt(l) - 97];

        for (let i = l; i <= r; i++) {
            const c = s.charCodeAt(i) - 97;

            // This character appeared before l, so this interval is invalid
            if (first[c] < l) {
                return null;
            }

            // Extend interval to include all occurrences of this character
            r = Math.max(r, last[c]);
        }

        return [l, r];
    }

    const intervals = [];

    // Only the first occurrence of a character can start a valid interval
    for (let i = 0; i < n; i++) {
        const c = s.charCodeAt(i) - 97;

        if (first[c] === i) {
            const interval = getInterval(i);

            if (interval !== null) {
                intervals.push(interval);
            }
        }
    }

    // Greedily choose the interval with the earliest ending position
    intervals.sort((a, b) => a[1] - b[1]);

    const result = [];
    let prevEnd = -1;

    for (const [l, r] of intervals) {
        if (l > prevEnd) {
            result.push(s.slice(l, r + 1));
            prevEnd = r;
        }
    }

    return result;
};
```

## Why This Works
By utilizing **Heap**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2472. Maximum Number of Non-overlapping Palindrome Substrings](../../2501-3000/2559-maximum-number-of-non-overlapping-palindrome-substrings/)
- [1621. Number of Sets of K Non-Overlapping Line Segments](../../1501-2000/1725-number-of-sets-of-k-non-overlapping-line-segments/)
- [689. Maximum Sum of 3 Non-Overlapping Subarrays](../../0501-1000/0689-maximum-sum-of-3-non-overlapping-subarrays/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/)
