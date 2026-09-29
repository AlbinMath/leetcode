# Word Frequency

## Problem Explanation
Write a bash script to calculate the frequency of each word in a text file `words.txt`. The output should be sorted by descending frequency, with the word and its count on each line.

## How the Code Works
The solution chains four Unix commands together using pipes:
1. `tr -s ' ' '\n'`: Translates (replaces) all spaces with newlines, splitting the text into one word per line. The `-s` flag squeezes consecutive spaces into a single newline.
2. `sort`: Sorts the words alphabetically. This is necessary for the next step.
3. `uniq -c`: Counts consecutive identical lines (which is why sorting first is essential), producing a count followed by the word.
4. `sort -nr`: Sorts the output numerically (`-n`) in reverse order (`-r`), putting the most frequent words first.
5. `awk '{print $2, $1}'`: Swaps the column order so the word comes before the count (since `uniq -c` outputs count first).
