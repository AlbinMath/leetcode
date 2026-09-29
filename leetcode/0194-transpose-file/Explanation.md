# Transpose File

## Problem Explanation
Given a text file `file.txt`, transpose its content. The first column becomes the first row, the second column becomes the second row, and so on.

## How the Code Works
The solution uses a single `awk` command:
1. `for(i=1;i<=NF;i++) a[i]=a[i]" "$i`: For each line, it iterates through all fields (words). It appends the `i`th field of the current line to an accumulator string `a[i]`. This effectively groups all values from column `i` together.
2. `END{for(i=1;i<=NF;i++) print substr(a[i],2)}`: After processing all lines, it prints each accumulated string. `substr(a[i], 2)` removes the leading space that was prepended during concatenation.
