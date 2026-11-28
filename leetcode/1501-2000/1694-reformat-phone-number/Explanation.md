# LeetCode 1694: Reformat Phone Number

**LeetCode Problem #1694 — Reformat Phone Number**
Solve LeetCode Reformat Phone Number using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Reformat Phone Number |
| LeetCode | #1694 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a phone number as a string `number`. `number` consists of digits, spaces `' '`, and/or dashes `'-'`.

You would like to reformat the phone number in a certain manner. Firstly, **remove** all spaces and dashes. Then, **group** the digits from left to right into blocks of length 3 **until** there are 4 or fewer digits. The final digits are then grouped as follows:

2 digits: A single block of length 2. 
 3 digits: A single block of length 3. 
 4 digits: Two blocks of length 2 each.

The blocks are then joined by dashes. Notice that the reformatting process should **never** produce any blocks of length 1 and produce **at most** two blocks of length 2.

Return *the phone number after formatting.*

## Constraints
- `2 <= number.length <= 100`
- `number` consists of digits and the characters `'-'` and `' '`.
- There are at least **two** digits in `number`.

## Examples
### Example 1
- **Input:** `number = "1-23-45 6"`
- **Output:** `"123-456"`
- **Explanation:** The digits are "123456".
Step 1: There are more than 4 digits, so group the next 3 digits. The 1st block is "123".
Step 2: There are 3 digits remaining, so put them in a single block of length 3. The 2nd block is "456".
Joining the blocks gives "123-456".

### Example 2
- **Input:** `number = "123 4-567"`
- **Output:** `"123-45-67"`
- **Explanation:** The digits are "1234567".
Step 1: There are more than 4 digits, so group the next 3 digits. The 1st block is "123".
Step 2: There are 4 digits left, so split them into two blocks of length 2. The blocks are "45" and "67".
Joining the blocks gives "123-45-67".

### Example 3
- **Input:** `number = "123 4-5678"`
- **Output:** `"123-456-78"`
- **Explanation:** The digits are "12345678".
Step 1: The 1st block is "123".
Step 2: The 2nd block is "456".
Step 3: There are 2 digits left, so put them in a single block of length 2. The 3rd block is "78".
Joining the blocks gives "123-456-78".

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Reformat Phone Number**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `number = "1-23-45 6"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"123-456"`.
4. **Verification:** The digits are "123456".
Step 1: There are more than 4 digits, so group the next 3 digits. The 1st block is "123".
Step 2: There are 3 digits remaining, so put them in a single block of length 3. The 2nd block is "456".
Joining the blocks gives "123-456".

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
    string reformatNumber(string number) {
        string digits = "";

        // Remove spaces and dashes
        for (char c : number) {
            if (isdigit(c)) {
                digits += c;
            }
        }

        string result = "";
        int i = 0;
        int n = digits.size();

        // Create blocks of 3 while more than 4 digits remain
        while (n - i > 4) {
            result += digits.substr(i, 3) + "-";
            i += 3;
        }

        // Handle the remaining digits
        int remaining = n - i;

        if (remaining == 4) {
            result += digits.substr(i, 2) + "-" + digits.substr(i + 2, 2);
        } else {
            result += digits.substr(i, remaining);
        }

        return result;
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
- [17. Letter Combinations of a Phone Number](../../0001-0500/0017-letter-combinations-of-a-phone-number/)
- [1179. Reformat Department Table](../../1001-1500/1179-reformat-department-table/)
- [1417. Reformat The String](../../1001-1500/1417-reformat-the-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/reformat-phone-number/)
