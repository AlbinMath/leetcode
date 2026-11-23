# LeetCode 2434: Using a Robot to Print the Lexicographically Smallest String

**LeetCode Problem #2434 — Using a Robot to Print the Lexicographically Smallest String**
Solve LeetCode Using a Robot to Print the Lexicographically Smallest String using C++ and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Using a Robot to Print the Lexicographically Smallest String |
| LeetCode | #2434 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string `s` and a robot that currently holds an empty string `t`. Apply one of the following operations until `s` and `t` **are both empty**:

Remove the **first** character of a string `s` and give it to the robot. The robot will append this character to the string `t`. 
 Remove the **last** character of a string `t` and give it to the robot. The robot will write this character on paper.

Return *the lexicographically smallest string that can be written on the paper.*

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists of only English lowercase letters.

## Examples
### Example 1
- **Input:** `s = "zza"`
- **Output:** `"azz"`
- **Explanation:** Let p denote the written string.
Initially p="", s="zza", t="".
Perform first operation three times p="", s="", t="zza".
Perform second operation three times p="azz", s="", t="".

### Example 2
- **Input:** `s = "bac"`
- **Output:** `"abc"`
- **Explanation:** Let p denote the written string.
Perform first operation twice p="", s="c", t="ba". 
Perform second operation twice p="ab", s="c", t="". 
Perform first operation p="ab", s="", t="c". 
Perform second operation p="abc", s="", t="".

### Example 3
- **Input:** `s = "bdda"`
- **Output:** `"addb"`
- **Explanation:** Let p denote the written string.
Initially p="", s="bdda", t="".
Perform first operation four times p="", s="", t="bdda".
Perform second operation four times p="addb", s="", t="".

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Using a Robot to Print the Lexicographically Smallest String**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "zza"`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"azz"`.
4. **Verification:** Let p denote the written string.
Initially p="", s="zza", t="".
Perform first operation three times p="", s="", t="zza".
Perform second operation three times p="azz", s="", t="".

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
#include <string>
using namespace std;

class Solution {
public:
    string robotWithString(string s) {
        int n = s.length();
        int freq[26] = {0};
        for (char c : s) {
            freq[c - 'a']++;
        }
        
        string t;
        t.reserve(n);
        string res;
        res.reserve(n);
        
        int min_char = 0; // 0 represents 'a'
        
        for (char c : s) {
            t.push_back(c);
            freq[c - 'a']--;
            
            // Advance min_char to the smallest character still remaining in s
            while (min_char < 26 && freq[min_char] == 0) {
                min_char++;
            }
            
            // Pop from stack t while its top is <= smallest remaining character in s
            while (!t.empty() && (t.back() - 'a') <= min_char) {
                res.push_back(t.back());
                t.pop_back();
            }
        }
        
        return res;
    }
};
```

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1061. Lexicographically Smallest Equivalent String](../../1001-1500/1058-lexicographically-smallest-equivalent-string/)
- [1625. Lexicographically Smallest String After Applying Operations](../../1501-2000/1747-lexicographically-smallest-string-after-applying-operations/)
- [2904. Shortest and Lexicographically Smallest Beautiful String](../../3001-3500/3150-shortest-and-lexicographically-smallest-beautiful-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/)
