# LeetCode 1700: Number of Students Unable to Eat Lunch

**LeetCode Problem #1700 — Number of Students Unable to Eat Lunch**
Solve LeetCode Number of Students Unable to Eat Lunch using C++, JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Students Unable to Eat Lunch |
| LeetCode | #1700 |
| Difficulty | Easy |
| Language | C++, JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers `0` and `1` respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.

The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a **stack**. At each step:

If the student at the front of the queue **prefers** the sandwich on the top of the stack, they will **take it** and leave the queue. 
 Otherwise, they will **leave it** and go to the queue's end.

This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

You are given two integer arrays `students` and `sandwiches` where `sandwiches[i]` is the type of the `i^​​​​​​th` sandwich in the stack (`i = 0` is the top of the stack) and `students[j]` is the preference of the `j^​​​​​​th` student in the initial queue (`j = 0` is the front of the queue). Return *the number of students that are unable to eat.*

## Constraints
- `1 <= students.length, sandwiches.length <= 100`
- `students.length == sandwiches.length`
- `sandwiches[i]` is `0` or `1`.
- `students[i]` is `0` or `1`.

## Examples
### Example 1
- **Input:** `students = [1,1,0,0], sandwiches = [0,1,0,1]`
- **Output:** `0`
- **Explanation:** - Front student leaves the top sandwich and returns to the end of the line making students = [1,0,0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [0,0,1,1].
- Front student takes the top sandwich and leaves the line making students = [0,1,1] and sandwiches = [1,0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [1,1,0].
- Front student takes the top sandwich and leaves the line making students = [1,0] and sandwiches = [0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [0,1].
- Front student takes the top sandwich and leaves the line making students = [1] and sandwiches = [1].
- Front student takes the top sandwich and leaves the line making students = [] and sandwiches = [].
Hence all students are able to eat.

### Example 2
- **Input:** `students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]`
- **Output:** `3`

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Number of Students Unable to Eat Lunch**, we observe the problem requirements and utilize the **Stack & Queue** technique. We iterate through the inputs using **Stack Push / Pop Parsing**, leveraging a **Stack** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Stack**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `students = [1,1,0,0], sandwiches = [0,1,0,1]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `0`.
4. **Verification:** - Front student leaves the top sandwich and returns to the end of the line making students = [1,0,0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [0,0,1,1].
- Front student takes the top sandwich and leaves the line making students = [0,1,1] and sandwiches = [1,0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [1,1,0].
- Front student takes the top sandwich and leaves the line making students = [1,0] and sandwiches = [0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [0,1].
- Front student takes the top sandwich and leaves the line making students = [1] and sandwiches = [1].
- Front student takes the top sandwich and leaves the line making students = [] and sandwiches = [].
Hence all students are able to eat.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
C++, JavaScript

## Source Code
- [solution.cpp](./solution.cpp)
- [solution.js](./solution.js)


### C++
```cpp
class Solution {
public:
    int countStudents(vector<int>& students, vector<int>& sandwiches) {
        int count0 = 0, count1 = 0;

        // Count student preferences
        for (int student : students) {
            if (student == 0)
                count0++;
            else
                count1++;
        }

        // Process sandwiches from the top
        for (int sandwich : sandwiches) {
            if (sandwich == 0) {
                if (count0 == 0)
                    return count1;
                count0--;
            } else {
                if (count1 == 0)
                    return count0;
                count1--;
            }
        }

        return 0;
    }
};
```

### JavaScript
```javascript
var countStudents = function(students, sandwiches) {
    let count0 = 0;
    let count1 = 0;

    // Count students who prefer each sandwich type
    for (let student of students) {
        if (student === 0) {
            count0++;
        } else {
            count1++;
        }
    }

    // Process sandwiches from the top of the stack
    for (let sandwich of sandwiches) {
        if (sandwich === 0) {
            if (count0 === 0) return count1;
            count0--;
        } else {
            if (count1 === 0) return count0;
            count1--;
        }
    }

    return 0;
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
- [1553. Minimum Number of Days to Eat N Oranges](../../1501-2000/1553-minimum-number-of-days-to-eat-n-oranges/)
- [1450. Number of Students Doing Homework at a Given Time](../../1001-1500/1450-number-of-students-doing-homework-at-a-given-time/)
- [1744. Can You Eat Your Favorite Candy on Your Favorite Day?](../../1501-2000/1744-can-you-eat-your-favorite-candy-on-your-favorite-day/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/)
