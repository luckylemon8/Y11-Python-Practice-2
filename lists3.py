from testhelper import test

# Write a function that checks if a single sudoku square is valid. 
# The input is a 2D list of numbers representing the square.abs
# Returns True if the square contains all numbers 1-9, no duplicates
# Returns False otherwise
#
# Valid input could be: [[1,2,3], [4,5,6], [7,8,9]]
# or [[1,3,2], [9,8,7], [5,6,4]]

def sudoku_box_checker(box):
    return False # Replace with your code


### TESTS - Run the code that calls the function to check it works.
test("Sudoku box checker 1",True, sudoku_box_checker([[1,2,3], [4,5,6], [7,8,9]]))
test("Sudoku box checker 2",True, sudoku_box_checker([[1,3,2], [9,8,7], [5,6,4]]))
test("Sudoku box checker 3",False, sudoku_box_checker([[1,2,3], [1,5,6], [7,8,9]]))
test("Sudoku box checker 4",False, sudoku_box_checker([[1,9,3], [4,5,6], [7,8,9]]))


