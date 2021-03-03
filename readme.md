# Python sudoku solver (no backtracking)

This script can solve a sudoku game without using backtracking\

## Usage

To represent a sodoku board use a code of 81 numbers representing the values in each cell, from left to right & up to down

_Example:_ 530070000600195000098000060800060003400803001700020006060000280000419005000080079

```
5 3 0 | 0 7 0 | 0 0 0
6 0 0 | 1 9 5 | 0 0 0
0 9 8 | 0 0 0 | 0 6 0
---------------------
8 0 0 | 0 6 0 | 0 0 3
4 0 0 | 8 0 3 | 0 0 1
7 0 0 | 0 2 0 | 0 0 6
---------------------
0 6 0 | 0 0 0 | 2 8 0
0 0 0 | 4 1 9 | 0 0 5
0 0 0 | 0 8 0 | 0 7 9
```

In main.py

```
solve("530070000600195000098000060800060003400803001700020006060000280000419005000080079")
```
