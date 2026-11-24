# LeetCode 1859: Sorting the Sentence

**LeetCode Problem #1859 — Sorting the Sentence**
Solve LeetCode Sorting the Sentence using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sorting the Sentence |
| LeetCode | #1859 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A **sentence** is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of lowercase and uppercase English letters.

A sentence can be **shuffled** by appending the **1-indexed word position** to each word then rearranging the words in the sentence.

For example, the sentence `"This is a sentence"` can be shuffled as `"sentence4 a3 is2 This1"` or `"is2 sentence4 This1 a3"`.

Given a **shuffled sentence** `s` containing no more than `9` words, reconstruct and return *the original sentence*.

## Constraints
- `2 <= s.length <= 200`
- `s` consists of lowercase and uppercase English letters, spaces, and digits from `1` to `9`.
- The number of words in `s` is between `1` and `9`.
- The words in `s` are separated by a single space.
- `s` contains no leading or trailing spaces.

## Examples
### Example 1
- **Input:** `s = "is2 sentence4 This1 a3"`
- **Output:** `"This is a sentence"`
- **Explanation:** Sort the words in s to their original positions "This1 is2 a3 sentence4", then remove the numbers.

### Example 2
- **Input:** `s = "Myself2 Me1 I4 and3"`
- **Output:** `"Me Myself and I"`
- **Explanation:** Sort the words in s to their original positions "Me1 Myself2 and3 I4", then remove the numbers.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Sorting the Sentence**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "is2 sentence4 This1 a3"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"This is a sentence"`.
4. **Verification:** Sort the words in s to their original positions "This1 is2 a3 sentence4", then remove the numbers.

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
    string sortSentence(string s) {
        vector<string> words(10);
        stringstream ss(s);
        string word;

        while (ss >> word) {
            int position = word.back() - '0';
            word.pop_back();

            words[position] = word;
        }

        string result = "";

        for (int i = 1; i <= 9; i++) {
            if (!words[i].empty()) {
                if (!result.empty()) {
                    result += " ";
                }

                result += words[i];
            }
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
- [2089. Find Target Indices After Sorting Array](../../2001-2500/2089-find-target-indices-after-sorting-array/)
- [2826. Sorting Three Groups](../../2501-3000/2826-sorting-three-groups/)
- [1451. Rearrange Words in a Sentence](../../1001-1500/1451-rearrange-words-in-a-sentence/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sorting-the-sentence/)
