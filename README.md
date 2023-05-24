# leetcode-file-cleaner

This repository contains Python code to help you `create folders` for each LeetCode problem.

With this, you can experiment with the code offline while keeping everything neat and `organised`.

Since Leetcode does not provide a way to use their API to `scrape` each problem, you need to copy the problem `manually`. 

See the input sample in the Example folder.

# Code Explanation

1. leetcodeCleaner.py

Filters the input file with removing unnecessary `info` and problematic `symbols` that could hinder the creation of folders. 

Create `json` file for vscode users. It gives flexibility for those who don't want to open each folder manually when they want to test their code.

It then creates a new file with the filtered data.

Input :
```
1. Two Sum
49.3%
Easy
9. Palindrome Number
53.2%
Easy
13. Roman to Integer
58.2%
Easy
```

Output:
```
1. Two Sum
9. Palindrome Number
13. Roman to Integer
```
___

2. Bulk File Creator.py

Creates mass folders with the names provided in the output file.

Update


