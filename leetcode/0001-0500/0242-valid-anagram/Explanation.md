# LeetCode 242: Valid Anagram

**LeetCode Problem #242 — Valid Anagram**
Solve LeetCode Valid Anagram using PHP and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Valid Anagram |
| LeetCode | #242 |
| Difficulty | Easy |
| Language | PHP |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

## Constraints
- `1 <= s.length, t.length <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "anagram", t = "nagaram"`
- **Output:** `true`

### Example 2
- **Input:** `s = "rat", t = "car"`
- **Output:** `false`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Valid Anagram**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "anagram", t = "nagaram"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
PHP

## Source Code
- [solution.php](./solution.php)


```php
class Solution {
    function isAnagram($s, $t) {
        if (strlen($s) !== strlen($t)) {
            return false;
        }

        $count = array_fill(0, 26, 0);

        // Count characters in s
        for ($i = 0; $i < strlen($s); $i++) {
            $index = ord($s[$i]) - ord('a');
            $count[$index]++;
        }

        // Remove characters using t
        for ($i = 0; $i < strlen($t); $i++) {
            $index = ord($t[$i]) - ord('a');
            $count[$index]--;

            // More occurrences in t than in s
            if ($count[$index] < 0) {
                return false;
            }
        }

        return true;
    }
}
```

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [20. Valid Parentheses](../../0001-0500/0020-valid-parentheses/)
- [32. Longest Valid Parentheses](../../0001-0500/0032-longest-valid-parentheses/)
- [36. Valid Sudoku](../../0001-0500/0036-valid-sudoku/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/valid-anagram/)
