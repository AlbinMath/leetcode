# Tenth Line

## Problem Explanation
Given a file `file.txt`, print just the 10th line of the file.

## How the Code Works
The solution uses `sed -n '10p'`:
- `sed` is a stream editor that processes text line by line.
- `-n` suppresses the default output (which would print every line).
- `'10p'` tells `sed` to **p**rint only line number 10.

This is a concise and efficient one-liner.
