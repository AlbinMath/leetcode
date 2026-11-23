# LeetCode 2408: Design SQL

**LeetCode Problem #2408 — Design SQL**
Solve LeetCode Design SQL using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Design SQL |
| LeetCode | #2408 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given two string arrays, `names` and `columns`, both of size `n`. The `i^th` table is represented by the name `names[i]` and contains `columns[i]` number of columns.

You need to implement a class that supports the following **operations**:

**Insert** a row in a specific table with an id assigned using an *auto-increment* method, where the id of the first inserted row is 1, and the id of each *new *row inserted into the same table is **one greater** than the id of the **last inserted** row, even if the last row was *removed*. 
 **Remove** a row from a specific table. Removing a row **does not** affect the id of the next inserted row. 
 **Select** a specific cell from any table and return its value. 
 **Export** all rows from any table in csv format.

Implement the `SQL` class:

`SQL(String[] names, int[] columns)`

Creates the `n` tables. 
 
 
 `bool ins(String name, String[] row)`
 
 Inserts `row` into the table `name` and returns `true`. 
 If `row.length` **does not** match the expected number of columns, or `name` is **not** a valid table, returns `false` without any insertion. 
 
 
 `void rmv(String name, int rowId)`
 
 Removes the row `rowId` from the table `name`. 
 If `name` is **not** a valid table or there is no row with id `rowId`, no removal is performed. 
 
 
 `String sel(String name, int rowId, int columnId)`
 
 Returns the value of the cell at the specified `rowId` and `columnId` in the table `name`. 
 If `name` is **not** a valid table, or the cell `(rowId, columnId)` is **invalid**, returns `"<null>"`. 
 
 
 `String[] exp(String name)`
 
 Returns the rows present in the table `name`. 
 If name is **not** a valid table, returns an empty array. Each row is represented as a string, with each cell value (**including** the row's id) separated by a `","`.

## Constraints
- `n == names.length == columns.length`
- `1 <= n <= 10^4`
- `1 <= names[i].length, row[i].length, name.length <= 10`
- `names[i]`, `row[i]`, and `name` consist only of lowercase English letters.
- `1 <= columns[i] <= 10`
- `1 <= row.length <= 10`
- All `names[i]` are **distinct**.
- At most `2000` calls will be made to `ins` and `rmv`.
- At most `10^4` calls will be made to `sel`.
- At most `500` calls will be made to `exp`.

## Examples
### Example 1
- **Input:** ``
- **Output:** ``
- **Explanation:** // Creates three tables.
SQL sql = new SQL(["one", "two", "three"], [2, 3, 1]);

// Adds a row to the table "two" with id 1. Returns True.
sql.ins("two", ["first", "second", "third"]);

// Returns the value "third" from the third column
// in the row with id 1 of the table "two".
sql.sel("two", 1, 3);

// Adds another row to the table "two" with id 2. Returns True.
sql.ins("two", ["fourth", "fifth", "sixth"]);

// Exports the rows of the table "two".
// Currently, the table has 2 rows with ids 1 and 2.
sql.exp("two");

// Removes the first row of the table "two". Note that the second row
// will still have the id 2.
sql.rmv("two", 1);

// Returns the value "fifth" from the second column
// in the row with id 2 of the table "two".
sql.sel("two", 2, 2);

// Exports the rows of the table "two".
// Currently, the table has 1 row with id 2.
sql.exp("two");

### Example 2
- **Input:** ``
- **Output:** ``
- **Explanation:** // Creates three tables.
SQL sQL = new SQL(["one", "two", "three"], [2, 3, 1]); 

// Adds a row to the table "two" with id 1. Returns True. 
sQL.ins("two", ["first", "second", "third"]); 

// Returns the value "third" from the third column 
// in the row with id 1 of the table "two".
sQL.sel("two", 1, 3); 

// Removes the first row of the table "two".
sQL.rmv("two", 1); 

// Returns "<null>" as the cell with id 1 
// has been removed from table "two".
sQL.sel("two", 1, 2); 

// Returns False as number of columns are not correct.
sQL.ins("two", ["fourth", "fifth"]); 

// Adds a row to the table "two" with id 2. Returns True.
sQL.ins("two", ["fourth", "fifth", "sixth"]);

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Design SQL**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with ``.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output ``.
4. **Verification:** // Creates three tables.
SQL sql = new SQL(["one", "two", "three"], [2, 3, 1]);

// Adds a row to the table "two" with id 1. Returns True.
sql.ins("two", ["first", "second", "third"]);

// Returns the value "third" from the third column
// in the row with id 1 of the table "two".
sql.sel("two", 1, 3);

// Adds another row to the table "two" with id 2. Returns True.
sql.ins("two", ["fourth", "fifth", "sixth"]);

// Exports the rows of the table "two".
// Currently, the table has 2 rows with ids 1 and 2.
sql.exp("two");

// Removes the first row of the table "two". Note that the second row
// will still have the id 2.
sql.rmv("two", 1);

// Returns the value "fifth" from the second column
// in the row with id 2 of the table "two".
sql.sel("two", 2, 2);

// Exports the rows of the table "two".
// Currently, the table has 1 row with id 2.
sql.exp("two");

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
Python

## Source Code
- [solution.py](./solution.py)


```python
class SQL:

    def __init__(self, names: list[str], columns: list[int]):
        self.tables = {}
        for name, col_count in zip(names, columns):
            self.tables[name] = {
                "cols": col_count,
                "next_id": 1,
                "rows": {}
            }

    def ins(self, name: str, row: list[str]) -> bool:
        table = self.tables.get(name)
        if not table or len(row) != table["cols"]:
            return False
            
        row_id = table["next_id"]
        table["next_id"] += 1
        table["rows"][row_id] = row
        return True

    def rmv(self, name: str, rowId: int) -> None:
        table = self.tables.get(name)
        if table:
            table["rows"].pop(rowId, None)

    def sel(self, name: str, rowId: int, columnId: int) -> str:
        table = self.tables.get(name)
        if not table or rowId not in table["rows"] or not (1 <= columnId <= table["cols"]):
            return "<null>"
            
        return table["rows"][rowId][columnId - 1]

    def exp(self, name: str) -> list[str]:
        table = self.tables.get(name)
        if not table:
            return []
            
        return [f"{row_id},{','.join(row)}" for row_id, row in table["rows"].items()]
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
- [211. Design Add and Search Words Data Structure](../../0001-0500/0211-design-add-and-search-words-data-structure/)
- [355. Design Twitter](../../0001-0500/0355-design-twitter/)
- [622. Design Circular Queue](../../0501-1000/0860-design-circular-queue/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/design-sql/)
