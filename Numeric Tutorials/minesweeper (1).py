
def mines_adj(grid):
    
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            mines = 0
            if grid[row][col] != "#":
                #checking for bounds
                #east
                if col + 1 < len(grid[row]):
                    if grid[row][col + 1] == "#":
                        mines += 1
                #west
                if col - 1 >= 0:
                    if grid[row][col - 1] == "#":
                        mines += 1
                #nort
                if row - 1 >= 0:
                    if grid[row - 1][col] == "#":
                        mines += 1
                if row - 1 >= 0 and col + 1 < len(grid[row]):
                    if grid[row - 1][col + 1] == "#":
                        mines += 1
                if row - 1 >= 0 and col - 1 >= 0:
                    if grid[row - 1][col - 1] == "#":
                        mines += 1
                #south 
                if row + 1 < len(grid):
                    if grid[row + 1][col] == "#":
                        mines += 1
                if row + 1 < len(grid) and col + 1 < len(grid[row]):
                    if grid[row + 1][col + 1] == "#":
                        mines += 1
                if row + 1 < len(grid) and col - 1 >= 0:
                    if grid[row + 1][col - 1] == "#":
                        mines += 1
                grid[row][col] = mines
    return(grid)
    
                   
                

grid = [["-", "-", "-", "#", "#"],
        ["-", "#", "-", "-", "-"],
        ["-", "-", "#", "-", "-"],
        ["-", "#", "#", "-", "-"],
        ["-", "-", "-", "-", "-"]]

print(mines_adj(grid))

#Hi, thank you for looking through my task
#I am not sure on how to arrange the new number replaced grid in the same 2D list format as the dash-hash original grid