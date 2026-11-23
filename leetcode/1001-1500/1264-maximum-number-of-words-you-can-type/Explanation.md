# LeetCode 1935: Maximum Number of Words You Can Type

**LeetCode Problem #1935 — Maximum Number of Words You Can Type**
Solve LeetCode Maximum Number of Words You Can Type using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Number of Words You Can Type |
| LeetCode | #1935 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is a malfunctioning keyboard where some letter keys do not work. All other keys on the keyboard work properly.

Given a string `text` of words separated by a single space (no leading or trailing spaces) and a string `brokenLetters` of all **distinct** letter keys that are broken, return *the **number of words** in* `text` *you can fully type using this keyboard*.

## Constraints
- `1 <= text.length <= 10^4`
- `0 <= brokenLetters.length <= 26`
- `text` consists of words separated by a single space without any leading or trailing spaces.
- Each word only consists of lowercase English letters.
- `brokenLetters` consists of **distinct** lowercase English letters.

## Examples
### Example 1
- **Input:** `text = "hello world", brokenLetters = "ad"`
- **Output:** `1`
- **Explanation:** We cannot type "world" because the 'd' key is broken.

### Example 2
- **Input:** `text = "leet code", brokenLetters = "lt"`
- **Output:** `1`
- **Explanation:** We cannot type "leet" because the 'l' and 't' keys are broken.

### Example 3
- **Input:** `text = "leet code", brokenLetters = "e"`
- **Output:** `0`
- **Explanation:** We cannot type either word because the 'e' key is broken.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Number of Words You Can Type**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `text = "hello world", brokenLetters = "ad"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** We cannot type "world" because the 'd' key is broken.

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
    int canBeTypedWords(string text, string brokenLetters) {
        bool broken[26] = {false};

        for (char c : brokenLetters) {
            broken[c - 'a'] = true;
        }

        int count = 0;
        bool canType = true;

        for (int i = 0; i < text.size(); i++) {
            if (text[i] == ' ') {
                if (canType) {
                    count++;
                }
                canType = true;
            } else if (broken[text[i] - 'a']) {
                canType = false;
            }
        }

        if (canType) {
            count++;
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
- [1561. Maximum Number of Coins You Can Get](../../1501-2000/1683-maximum-number-of-coins-you-can-get/)
- [2071. Maximum Number of Tasks You Can Assign](../../2001-2500/2180-maximum-number-of-tasks-you-can-assign/)
- [1298. Maximum Candies You Can Get from Boxes](../../1001-1500/1424-maximum-candies-you-can-get-from-boxes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-number-of-words-you-can-type/)
