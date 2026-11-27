# LeetCode 1773: Count Items Matching a Rule

**LeetCode Problem #1773 — Count Items Matching a Rule**
Solve LeetCode Count Items Matching a Rule using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Items Matching a Rule |
| LeetCode | #1773 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array `items`, where each `items[i] = [type_i, color_i, name_i]` describes the type, color, and name of the `i^th` item. You are also given a rule represented by two strings, `ruleKey` and `ruleValue`.

The `i^th` item is said to match the rule if **one** of the following is true:

`ruleKey == "type"` and `ruleValue == type_i`. 
 `ruleKey == "color"` and `ruleValue == color_i`. 
 `ruleKey == "name"` and `ruleValue == name_i`.

Return *the number of items that match the given rule*.

## Constraints
- `1 <= items.length <= 10^4`
- `1 <= type_i.length, color_i.length, name_i.length, ruleValue.length <= 10`
- `ruleKey` is equal to either `"type"`, `"color"`, or `"name"`.
- All strings consist only of lowercase letters.

## Examples
### Example 1
- **Input:** `items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"`
- **Output:** `1`
- **Explanation:** There is only one item matching the given rule, which is ["computer","silver","lenovo"].

### Example 2
- **Input:** `items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone"`
- **Output:** `2`
- **Explanation:** There are only two items matching the given rule, which are ["phone","blue","pixel"] and ["phone","gold","iphone"]. Note that the item ["computer","silver","phone"] does not match.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Items Matching a Rule**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** There is only one item matching the given rule, which is ["computer","silver","lenovo"].

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    int countMatches(vector<vector<string>>& items, string ruleKey, string ruleValue) {
        int count = 0;
        int index;

        if (ruleKey == "type") {
            index = 0;
        } else if (ruleKey == "color") {
            index = 1;
        } else {
            index = 2;
        }

        for (const auto& item : items) {
            if (item[index] == ruleValue) {
                count++;
            }
        }

        return count;
    }
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
- [3405. Count the Number of Arrays with K Matching Adjacent Elements](../../3001-3500/3405-count-the-number-of-arrays-with-k-matching-adjacent-elements/)
- [10. Regular Expression Matching](../../0001-0500/0010-regular-expression-matching/)
- [44. Wildcard Matching](../../0001-0500/0044-wildcard-matching/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-items-matching-a-rule/)
