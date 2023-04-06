# leetcode-file-cleaner

This repository contains Python code to help you `create folders` for each LeetCode problem.

With this, you can experiment with the code offline while keeping everything neat and `organised`.

Since Leetcode does not provide a way to use their API to `scrape` each problem, you need to copy the problem `manually`. 

See the input sample in the Example folder.

# Code Explanation

1. LC Filter.py

Filters the input file to remove unnecessary info and put it in new output file, so we can use it to create folders.

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
2. Symbols Remover.py

Removes problematic symbols that could hinder the creation of folders. Since Windows and Linux doesn't allow some symbols in folder names.

Symbols that can't be used in folder names:
```
symbols = '/ \ : * ? " < > | '
```

___

3. Bulk File Creator.py

Creates mass folders with the names provided in the output file.

___

4. JSON Adder.py

This Python code is `optional`. It's for `VS Code users` who want more flexibility and don't want to open each folder manually when they want to test their code.

Update json file so user can test their code even when there are in other subfolders.