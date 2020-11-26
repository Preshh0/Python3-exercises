#2D LIST
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[2][1]) #to print out elements in a list inside a list you treat it like a matrix. The first [] is for the row, the second [] is for the column.

#Nested_for_loops

for row in number_grid:
    #print(row)
    for col in row:
        print(col)