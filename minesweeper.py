# Define function count_mines

def count_mines(grid):
    
    ### Given a grid of # and - characters, replace each - with a digit indicating how many mines are immediately adjacent to that spot.
    # The function first determines the number of rows and columns in the grid, then initializes a new 2D list result with the same number
    # of rows and columns as the input grid.
    # Next, the function iterates over each cell in the grid and checks if it is a mine (represented by "#") or not. If it is a mine, the 
    # corresponding cell in the result grid is set to "#". Otherwise, the function counts the number of mines surrounding the current cell 
    # by iterating over a range of cells surrounding it. The max and min functions are used to ensure that the iteration does not go outside 
    # the bounds of the grid.
    
    rows = len(grid)
    cols = len(grid[0])
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            if grid[i][j] == "#":
                row.append("#")
            else:
                count = 0
                # check the adjacent cells
                for x in range(max(0, i-1), min(i+2, rows)):
                    for y in range(max(0, j-1), min(j+2, cols)):
                        if grid[x][y] == "#":
                            count += 1
                row.append(str(count))
        result.append("".join(row))
    return result
grid = [
    ["#", "-", "-", "#", "#"],
    ["-", "-", "#", "-", "-"],
    ["#", "-", "-", "-", "-"],
    ["#", "-", "-", "-", "#"],
    ["-", "#", "#", "#", "-"]
]
# Finally, the function sets the value of the corresponding cell in the result grid to a string representation of the count.
#  The function then returns the result grid.
counts = count_mines(grid)

for row in counts:
    print(" ".join(row))