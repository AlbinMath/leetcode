# LeetCode 482: License Key Formatting

**LeetCode Problem #482 — License Key Formatting**
Solve LeetCode License Key Formatting using JavaScript, Python and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | License Key Formatting |
| LeetCode | #482 |
| Difficulty | Easy |
| Language | JavaScript, Python |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a license key represented as a string `s` that consists of only alphanumeric characters and dashes. The string is separated into `n + 1` groups by `n` dashes. You are also given an integer `k`.

We want to reformat the string `s` such that each group contains exactly `k` characters, except for the first group, which could be shorter than `k` but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

Return *the reformatted license key*.

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists of English letters, digits, and dashes `'-'`.
- `1 <= k <= 10^4`

## Examples
### Example 1
- **Input:** `s = "5F3Z-2e-9-w", k = 4`
- **Output:** `"5F3Z-2E9W"`
- **Explanation:** The string s has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.

### Example 2
- **Input:** `s = "2-5g-3-J", k = 2`
- **Output:** `"2-5G-3J"`
- **Explanation:** The string s has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **License Key Formatting**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "5F3Z-2e-9-w", k = 4`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"5F3Z-2E9W"`.
4. **Verification:** The string s has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### JavaScript
```javascript
var licenseKeyFormatting = function(s, k) {
    s = s.replace(/-/g, "").toUpperCase();

    let result = [];

    for (let i = s.length; i > 0; i -= k) {
        result.push(s.substring(Math.max(0, i - k), i));
    }

    return result.reverse().join("-");
};
```

### Python
```python
class Solution:
    def licenseKeyFormatting(self, s, k):
        # Remove dashes and convert to uppercase
        s = s.replace("-", "").upper()

        result = []

        # Start from the right
        i = len(s)

        while i > 0:
            start = max(0, i - k)
            result.append(s[start:i])
            i = start

        # Groups were created from right to left
        result.reverse()

        return "-".join(result)
```

## Why This Works
By utilizing **Math & Logic**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [981. Time Based Key-Value Store](../../0501-1000/0981-time-based-key-value-store/)
- [1409. Queries on a Permutation With Key](../../1001-1500/1409-queries-on-a-permutation-with-key/)
- [1604. Alert Using Same Key-Card Three or More Times in a One Hour Period](../../1501-2000/1604-alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/license-key-formatting/)
