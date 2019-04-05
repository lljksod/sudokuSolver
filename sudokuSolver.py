import sys
sys.setrecursionlimit(1004)
class sudokuSolver():

    def __init__(self):
        self.puzzle = [[0 for i in range(9)] for j in range(9)]
        

    def endOfGrid(self):
        for i in range(9):
            for j in range(9):
                if self.puzzle[i][j] == 0:
                    return False
        return True

    def gridIsValid(self):
        # check if rows have a repeated number
        for row in self.puzzle:
            
            for i in range(1,10):
                if row.count(i) > 1:
                    return False

        #check if columns have a repeated number
        for column in range(9):
            col = []
            for row in range(9):
                col.append(self.puzzle[row][column])
            for i in range(1,10):
                if col.count(i) > 1:
                    return False

        #check each grid for a repeated number
        # rows 0 1 2 cols 0 1 2
        grid = []
        for i in range(3):
            for j in range(3):
                grid.append(self.puzzle[i][j])
        for i in range(1,10):
            if grid.count(i) > 1:
                return False
        

        # rows 0 1 2 cols 3 4 5
        grid.clear()
        for i in range(3):
            for j in range(3,6):
                grid.append(self.puzzle[i][j])
        for i in range(1,10):
            if grid.count(i) > 1:
                return False
        

        #rows 0 1 2 cols 6 7 8
        grid.clear()
        for i in range(3):
            for j in range(6,9):
                grid.append(self.puzzle[i][j])
        for i in range(1,10):
            if grid.count(i) > 1:
                return False
        
        # rows 3 4 5 cols 0 1 2
        grid.clear()
        for i in range(3,6):
            for j in range(3):
                grid.append(self.puzzle[i][j])
        for i in range(1,10):
            if grid.count(i) > 1:
                return False

        # rows 3 4 5 cols 3 4 5
        grid.clear()
        for i in range(3,6):
            for j in range(3,6):
                grid.append(self.puzzle[i][j])
        for i in range(1,10):
            if grid.count(i) > 1:
                return False

        #rows 3 4 5 cols 6 7 8
        grid.clear()
        for i in range(3,6):
            for j in range(6,9):
                grid.append(self.puzzle[i][j])
        for i in range(1,10):
            if grid.count(i) > 1:
                return False

        # rows 6 7 8 cols 0 1 2
        grid.clear()
        for i in range(6,9):
            for j in range(3):
                grid.append(self.puzzle[i][j])
        for i in range(1,10):
            if grid.count(i) > 1:
                return False

        # rows 6 7 8 cols 3 4 5
        grid.clear()
        for i in range(6,9):
            for j in range(3,6):
                grid.append(self.puzzle[i][j])
        for i in range(1,10):
            if grid.count(i) > 1:
                return False

        #rows 6 7 8 cols 6 7 8
        grid.clear()
        for i in range(6,9):
            for j in range(6,9):
                grid.append(self.puzzle[i][j])
        for i in range(1,10):
            if grid.count(i) > 1:
                return False

        return True




    def solve(self, row, column):
        if self.endOfGrid():
            return True

        nextRow, nextColumn = self.nextPosition(row, column)
        for x in range(1,10):
            self.puzzle[row][column] = x
            if self.gridIsValid():
                if self.solve(nextRow, nextColumn):
                    return True

        self.puzzle[row][column] = 0
        return False

    def nextPosition(self, row, column):
        while True:
            if column < 8:
                column += 1
            elif column == 8 and row < 8:
                column = 0
                row += 1

            if self.puzzle[row][column] == 0 or self.countZeroes() == 1:
                break

        return row, column

    def countZeroes(self):
        zeroes = 0
        for i in range(9):
            for j in range(9):
                if self.puzzle[i][j] == 0:
                    zeroes += 1

        return zeroes




def main():
    test = sudokuSolver()
    test.puzzle[0] = [0,3,0,0,0,4,0,2,0]
    test.puzzle[1] = [0,0,2,5,0,0,6,3,0]
    test.puzzle[2] = [0,0,8,0,0,2,0,0,5]
    test.puzzle[3] = [2,0,0,9,5,0,0,1,0]
    test.puzzle[4] = [1,0,3,2,4,7,5,0,6]
    test.puzzle[5] = [0,5,0,0,3,8,0,0,2]
    test.puzzle[6] = [3,0,0,4,0,0,9,0,0]
    test.puzzle[7] = [0,1,5,0,0,9,7,0,0]
    test.puzzle[8] = [0,4,0,7,0,0,0,5,0]

    row, column = test.nextPosition(0,0)

    test.solve(row, column)
    for i in range(9):
        print(test.puzzle[i])


if __name__ == '__main__':
    main()


