# LeetCode 205: Isomorphic Strings

**LeetCode Problem #205 — Isomorphic Strings**
Solve LeetCode Isomorphic Strings using PHP and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Isomorphic Strings |
| LeetCode | #205 |
| Difficulty | Easy |
| Language | PHP |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given two strings `s` and `t`, *determine if they are isomorphic*.

Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

## Constraints
- `1 <= s.length <= 5 * 10^4`
- `t.length == s.length`
- `s` and `t` consist of any valid ascii character.

## Examples
### Example 1
- **Input:** `s = "egg", t = "add"`
- **Output:** `true`
- **Explanation:** The strings `s` and `t` can be made identical by: 

 
 Mapping `'e'` to `'a'`. 
 Mapping `'g'` to `'d'`.

### Example 2
- **Input:** `s = "f11", t = "b23"`
- **Output:** `false`
- **Explanation:** The strings `s` and `t` can not be made identical as `'1'` needs to be mapped to both `'2'` and `'3'`.

### Example 3
- **Input:** `s = "paper", t = "title"`
- **Output:** `true`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Isomorphic Strings**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "egg", t = "add"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** The strings `s` and `t` can be made identical by: 

 
 Mapping `'e'` to `'a'`. 
 Mapping `'g'` to `'d'`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
PHP

## Source Code
- [solution.php](./solution.php)


```php
class Solution {
    function isIsomorphic($s, $t) {
        $mapST = [];
        $mapTS = [];

        $length = strlen($s);

        for ($i = 0; $i < $length; $i++) {
            $charS = $s[$i];
            $charT = $t[$i];

            // Check s -> t mapping
            if (isset($mapST[$charS])) {
                if ($mapST[$charS] !== $charT) {
                    return false;
                }
            } else {
                $mapST[$charS] = $charT;
            }

            // Check t -> s mapping
            if (isset($mapTS[$charT])) {
                if ($mapTS[$charT] !== $charS) {
                    return false;
                }
            } else {
                $mapTS[$charT] = $charS;
            }
        }

        return true;
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
- [43. Multiply Strings](../../0001-0500/0043-multiply-strings/)
- [415. Add Strings](../../0001-0500/0415-add-strings/)
- [583. Delete Operation for Two Strings](../../0501-1000/0583-delete-operation-for-two-strings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/isomorphic-strings/)
