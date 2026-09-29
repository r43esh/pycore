"""
Q9 ●●●○○○○○○○ 3/10 [copying, nested lists]
Create a 3x3 grid with [[0]*3]*3, set grid[0][0] = 1 and print it. Explain the bug and give three
different correct ways to build the grid.
"""
grid=[[0]*3]*3
grid[0][0]=1
print(repr(grid))
ans="""
it is because it makes a linear list just increased 3 time pointing to same pt 
"""

grid =[[0]*3 for i in range(3)]
print(grid)
grid[0][0]=1
print(grid)

grid =[[0,0,0],[0,0,0],[0,0,0]]
grid[0][0]=1

grid=[]
for i in range(3):
    grid.append([0]*3)
grid[0][0]=1
print(grid)