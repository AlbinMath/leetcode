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

## Problem
The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers  0  and  1  respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Stack Push / Pop Parsing**. By maintaining state efficiently in a **Stack**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Stack**).
2. Process elements sequentially using **Stack Push / Pop Parsing**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Number of Students Unable to Eat Lunch**. Applying **Stack Push / Pop Parsing** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

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
- [1450. Number of Students Doing Homework at a Given Time](../../1501-2000/1560-number-of-students-doing-homework-at-a-given-time/)
- [1553. Minimum Number of Days to Eat N Oranges](../../1501-2000/1676-minimum-number-of-days-to-eat-n-oranges/)
- [596. Classes With at Least 5 Students](../../0501-1000/0596-classes-with-at-least-5-students/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/)
