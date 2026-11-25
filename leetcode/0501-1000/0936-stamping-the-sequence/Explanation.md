# LeetCode 936: Stamping The Sequence

**LeetCode Problem #936 — Stamping The Sequence**
Solve LeetCode Stamping The Sequence using JavaScript and Sliding Window. This solution finds the optimal result using Dynamic Sliding Window Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Stamping The Sequence |
| LeetCode | #936 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Dynamic Sliding Window Traversal |
| Data Structure | Array / Hash Set |
| Pattern | Sliding Window |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two strings `stamp` and `target`. Initially, there is a string `s` of length `target.length` with all `s[i] == '?'`.

In one turn, you can place `stamp` over `s` and replace every letter in the `s` with the corresponding letter from `stamp`.

For example, if `stamp = "abc"` and `target = "abcba"`, then `s` is `"?????"` initially. In one turn you can:

place `stamp` at index `0` of `s` to obtain `"abc??"`, 
 place `stamp` at index `1` of `s` to obtain `"?abc?"`, or 
 place `stamp` at index `2` of `s` to obtain `"??abc"`. 
 
 Note that `stamp` must be fully contained in the boundaries of `s` in order to stamp (i.e., you cannot place `stamp` at index `3` of `s`).

We want to convert `s` to `target` using **at most** `10 * target.length` turns.

Return *an array of the index of the left-most letter being stamped at each turn*. If we cannot obtain `target` from `s` within `10 * target.length` turns, return an empty array.

## Constraints
- `1 <= stamp.length <= target.length <= 1000`
- `stamp` and `target` consist of lowercase English letters.

## Examples
### Example 1
- **Input:** `stamp = "abc", target = "ababc"`
- **Output:** `[0,2]`
- **Explanation:** Initially s = "?????".
- Place stamp at index 0 to get "abc??".
- Place stamp at index 2 to get "ababc".
[1,0,2] would also be accepted as an answer, as well as some other answers.

### Example 2
- **Input:** `stamp = "abca", target = "aabcaca"`
- **Output:** `[3,0,1]`
- **Explanation:** Initially s = "???????".
- Place stamp at index 3 to get "???abca".
- Place stamp at index 0 to get "abcabca".
- Place stamp at index 1 to get "aabcaca".

## Key Insight
Maintain a dynamic contiguous window with two pointers (`left` and `right`), expanding to include new elements and shrinking when window invariants are violated.

## Approach
To solve **Stamping The Sequence**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `stamp = "abc", target = "ababc"`.
2. **Processing Steps:** We apply **Dynamic Sliding Window Traversal** using our **Array / Hash Set**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[0,2]`.
4. **Verification:** Initially s = "?????".
- Place stamp at index 0 to get "abc??".
- Place stamp at index 2 to get "ababc".
[1,0,2] would also be accepted as an answer, as well as some other answers.

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
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
/**
 * @param {string} stamp
 * @param {string} target
 * @return {number[]}
 */
var movesToStamp = function (stamp, target) {
    const m = stamp.length, n = target.length;
    const windows = n - m + 1;
    const t = target.split('');

    // todo[i]: set of positions in window i that still need to be blanked
    // (non-matching letters). Window is ready when todo is empty.
    const todoCount = new Array(windows).fill(0);
    const todoSets = new Array(windows);
    const queue = [];
    const visited = new Array(windows).fill(false);
    const blanked = new Array(n).fill(false);

    for (let i = 0; i < windows; i++) {
        const set = new Set();
        for (let j = 0; j < m; j++) {
            if (target[i + j] !== stamp[j]) set.add(i + j);
        }
        todoSets[i] = set;
        if (set.size === 0) {
            queue.push(i);
            visited[i] = true;
        }
    }

    const order = [];
    let head = 0;
    while (head < queue.length) {
        const i = queue[head++];
        order.push(i);
        for (let j = 0; j < m; j++) {
            const p = i + j;
            if (blanked[p]) continue;
            blanked[p] = true;
            // p is now a wildcard: remove it from every window covering it
            const lo = Math.max(0, p - m + 1);
            const hi = Math.min(windows - 1, p);
            for (let w = lo; w <= hi; w++) {
                if (visited[w]) continue;
                todoSets[w].delete(p);
                if (todoSets[w].size === 0) {
                    visited[w] = true;
                    queue.push(w);
                }
            }
        }
    }

    for (let p = 0; p < n; p++) {
        if (!blanked[p]) return [];
    }
    return order.reverse();
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
- [2132. Stamping the Grid](../../2001-2500/2132-stamping-the-grid/)
- [60. Permutation Sequence](../../0001-0500/0060-permutation-sequence/)
- [128. Longest Consecutive Sequence](../../0001-0500/0128-longest-consecutive-sequence/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/stamping-the-sequence/)
