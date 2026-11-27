# LeetCode 4105: Repeated String Match II

**LeetCode Problem #4105 — Repeated String Match II**
Solve LeetCode Repeated String Match II using JavaScript and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Repeated String Match II |
| LeetCode | #4105 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given two strings `a` and `b` consisting of lowercase English letters, and two integers `x` and `y`.

Return `true` if the string formed by repeating `b` **exactly** `y` times (`b * y`) is a ** substring ** of the string formed by repeating `a` **exactly** `x` times (`a * x`). Otherwise, return `false`.

## Constraints
- `1 <= a.length <= 100`
- `1 <= b.length <= 100`
- `1 <= x <= 10^9`
- `1 <= y <= 10^9`​​​​​​​
- `a` and `b` consist of lowercase English letters.

## Examples
### Example 1
- **Input:** `a = "ab", b = "abab", x = 2, y = 1`
- **Output:** `true`
- **Explanation:** `a * x = "ab" * 2 = "abab"` 
 `b * y = "abab" * 1 = "abab"` 
 They are identical, so `b * y` is a substring of `a * x`. Thus, the answer is `true`.

### Example 2
- **Input:** `a = "abc", b = "bc", x = 2, y = 3`
- **Output:** `false`
- **Explanation:** `a * x = "abc" * 2 = "abcabc"` 
 `b * y = "bc" * 3 = "bcbcbc"` 
 The answer is `false` as `b * y = "bcbcbc"` is not a substring of `a * x = "abcabc"`.

### Example 3
- **Input:** `a = "abcd", b = "cdab", x = 2, y = 1`
- **Output:** `true`
- **Explanation:** `a * x = "abcd" * 2 = "abcdabcd"` 
 `b * y = "cdab"` appears in `a * x = "abcdabcd"` at indices `[2..5]`. Thus, the answer is `true`.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Repeated String Match II**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `a = "ab", b = "abab", x = 2, y = 1`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** `a * x = "ab" * 2 = "abab"` 
 `b * y = "abab" * 1 = "abab"` 
 They are identical, so `b * y` is a substring of `a * x`. Thus, the answer is `true`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Tree / Graph / Grid.

## Pattern
**Tree & Graph**

## Topics
- Tree
- Graph
- DFS
- BFS

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var repeatedStringMatch = function(a, b, x, y) {
    const la = a.length;
    const lb = b.length;
    const totalA = BigInt(la) * BigInt(x);
    const totalB = BigInt(lb) * BigInt(y);

    if (totalB > totalA) return false;
    const minRepsB = Math.ceil((la + lb) / lb) + 1;
    const effY = Math.min(y, minRepsB);
    const pattern = b.repeat(effY);
    const maxOffset = Number(totalA - totalB < BigInt(la - 1) ? totalA - totalB : BigInt(la - 1));
    const neededLenA = maxOffset + pattern.length;
    const effX = Math.min(x, Math.ceil(neededLenA / la));
    const text = a.repeat(effX);
    const firstMatch = text.indexOf(pattern);
    return firstMatch !== -1 && BigInt(firstMatch) <= totalA - totalB;
};
```

## Why This Works
By utilizing **Tree & Graph**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [686. Repeated String Match](../../0501-1000/0686-repeated-string-match/)
- [942. DI String Match](../../0501-1000/0942-di-string-match/)
- [187. Repeated DNA Sequences](../../0001-0500/0187-repeated-dna-sequences/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/repeated-string-match-ii/)
