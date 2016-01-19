Given a 2d array of 'x's (land) and '.'s (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally 
or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

xx.x.
.x..x
xx...
.....
Answer: 3

Example 2:

.x...
.x...
..x..
...xx
Answer: 3


def num_islands(array):
    if array == []:
        return 0
    row = len(array)
    col = len(array[0])
    visited = [[False for j in range(col)] for i in range(row)]

    count = 0
    for i in range(row):
        for j in range(col):
            if array[i][j] == 'x' and not visited[i][j]:
                dfs(array, visited, row, col, i, j)
                count += 1
    return count

def dfs( array, visited, row, col, i, j):
    if array[i][j] != 'x' or visited[i][j]:
        return
    visited[i][j] = True

    if i > 0:
        dfs(array, visited, row, col, i - 1, j)
    if i < row - 1:
        dfs(array, visited, row, col, i + 1, j)
    if j > 0:
        dfs(array, visited, row, col, i, j - 1)
    if j < col - 1:
        dfs(array, visited, row, col, i, j + 1)


print num_islands([['x','.','x','.','x'],
                  ['x','x','.','x','x'],
                  ['x','.','x','.','x']]) #4

print num_islands([['x','.','.','x','.'],
                  ['.','x','.','x','x'],
                  ['.','.','x','x','.']]) #3 

print num_islands([['x','x','.','.','.'],
                  ['x','.','x','.','.'],
                  ['.','.','.','.','x']]) #3 

print num_islands([['x','.','.','x','.'],
                  ['x','x','.','x','x'],
                  ['x','.','x','.','x']]) #3

print num_islands([['.','.','x','.'],
                  ['x','x','x','.'],
                  ['.','.','.','x']]) #2

print num_islands([['.','.','.','x'],
                  ['.','x','x','x'],
                  ['x','.','.','.']]) #2

print num_islands([]) #0

print num_islands([['.','x','.','.','x'],
                  ['x','x','.','x','x'],
                  ['.','.','x','.','.']]) #3

print num_islands([['x','.','x','.','x'],
                  ['.','.','.','x','x'],
                  ['x','.','x','.','.']]) #5

print num_islands([['x','.','x','.','.'],
                  ['.','.','x','.','x'],
                  ['.','.','x','x','x'],
                  ['.','.','x','.','x'],
                  ['.','.','x','x','x'],
                  ['x','x','x','.','.']]) #6
