from testhelper import test

def sudoku_box_checker(box):
    numbers = set()
    
    for row in box:
        for num in row:
            numbers.add(num)
    
    return numbers == {1, 2, 3, 4, 5, 6, 7, 8, 9}

test("Sudoku box checker 1", True, sudoku_box_checker([[1,2,3], [4,5,6], [7,8,9]]))
test("Sudoku box checker 2", True, sudoku_box_checker([[1,3,2], [9,8,7], [5,6,4]]))
test("Sudoku box checker 3", False, sudoku_box_checker([[1,2,3], [1,5,6], [7,8,9]]))
test("Sudoku box checker 4", False, sudoku_box_checker([[1,9,3], [4,5,6], [7,8,9]]))


