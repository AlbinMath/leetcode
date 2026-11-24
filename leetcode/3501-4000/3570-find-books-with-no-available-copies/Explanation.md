# LeetCode 3570: Find Books with No Available Copies

**LeetCode Problem #3570 — Find Books with No Available Copies**
Solve LeetCode Find Books with No Available Copies using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Books with No Available Copies |
| LeetCode | #3570 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Table: `library_books`

+------------------+---------+
| Column Name | Type |
+------------------+---------+
| book_id | int |
| title | varchar |
| author | varchar |
| genre | varchar |
| publication_year | int |
| total_copies | int |
+------------------+---------+
book_id is the unique identifier for this table.
Each row contains information about a book in the library, including the total number of copies owned by the library.

Table: `borrowing_records`

+---------------+---------+
| Column Name | Type |
+---------------+---------+
| record_id | int |
| book_id | int |
| borrower_name | varchar |
| borrow_date | date |
| return_date | date |
+---------------+---------+
record_id is the unique identifier for this table.
Each row represents a borrowing transaction and return_date is NULL if the book is currently borrowed and hasn't been returned yet.

Write a solution to find **all books** that are **currently borrowed (not returned)** and have **zero copies available** in the library.

A book is considered **currently borrowed** if there exists a** **borrowing record with a **NULL** `return_date`

Return *the result table ordered by current borrowers in **descending** order, then by book title in **ascending** order.*

The result format is in the following example.

## Examples
Consider the standard input for **Find Books with No Available Copies**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find Books with No Available Copies**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
Applying **In-Place Array Traversal & Index Mapping** step by step to the input yields the expected result.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
import pandas as pd

def find_books_with_no_available_copies(
    library_books: pd.DataFrame,
    borrowing_records: pd.DataFrame
) -> pd.DataFrame:

    # Keep only currently borrowed books
    current = borrowing_records[
        borrowing_records["return_date"].isna()
    ]

    # Count current borrowers for each book
    borrowers = (
        current.groupby("book_id")
        .size()
        .reset_index(name="current_borrowers")
    )

    # Join with library books
    result = library_books.merge(
        borrowers,
        on="book_id",
        how="inner"
    )

    # Zero copies available:
    # total_copies - current_borrowers = 0
    result = result[
        result["total_copies"] == result["current_borrowers"]
    ]

    # Sort by borrowers DESC, title ASC
    return result[
        [
            "book_id",
            "title",
            "author",
            "genre",
            "publication_year",
            "current_borrowers"
        ]
    ].sort_values(
        ["current_borrowers", "title"],
        ascending=[False, True]
    ).reset_index(drop=True)
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
- [3642. Find Books with Polarized Opinions](../../3501-4000/3642-find-books-with-polarized-opinions/)
- [363. Max Sum of Rectangle No Larger Than K](../../0001-0500/0363-max-sum-of-rectangle-no-larger-than-k/)
- [1042. Flower Planting With No Adjacent](../../1001-1500/1042-flower-planting-with-no-adjacent/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-books-with-no-available-copies/)
