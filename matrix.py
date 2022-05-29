


class Matrix:

    def __init__(self, inper):
        self.rows, self.columns = inper.split()

    def create(self):
        self.matrix = [[float(n) for n in input().split()] for _row in range(int(self.rows))]

    def add(self, mtx):
        if self.rows == mtx.rows and self.columns == mtx.columns:
            result = [[self.matrix[i][j] + mtx.matrix[i][j] for j in range(len(self.matrix[0]))] for i in
                      range(len(self.matrix))]
            for row in result:
                for number in row:
                    print(number, end=" ")
                print()
        else:
            print("ERROR")

    def multiply(self, number):
        result = [[self.matrix[i][j] * number for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
        for row in result:
            for number in row:
                print(round(number, 4), end=" ")
            print()

  

    def printer(self):
        for row in self.matrix:
            for number in row:
                print(int(number), end=" ")
            print()

    def multiply_matrices(self, mtx):
        if self.columns != mtx.rows:
            print("The operation cannot be performed.")
        else:
            result = [[sum([self.matrix[i][k] * mtx.matrix[j][k] for k in range(len(mtx.matrix[0]))]) for j in
                       range(len(mtx.matrix))] for i in range(len(self.matrix))]

            for row in result:
                for number in row:
                    print(round(number, 2), end=" ")
                print()
                
    @staticmethod        
    def determinant(mtx):
        if len(mtx) == 1:
            return mtx[0][0]
        elif len(mtx) == 2:
            det = mtx[0][0] * mtx[1][1] - mtx[1][0] * mtx[0][1]
            return det
        else:
            recur = 0
            for i, e in enumerate(mtx):
                rex = mtx[0][i] * Matrix.determinant([[el for ind, el in enumerate(matx) if ind != i] for matx in mtx[1:]])
                if i % 2 == 0:
                    recur += rex
                else:
                    recur -= rex
            return recur
            
   
            
def menu():
    while True:
        print("1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n4. Calculate a determinant\n0. Exit\n\nEnter your choice")
        choice = input()
        if choice == "1":
            print("Enter size of first matrix: ")
            matrix_a = Matrix(input())
            print("Enter first matrix: ")
            matrix_a.create()

            print("Enter size of second matrix: ")
            matrix_b = Matrix(input())
            print("Enter second matrix: ")
            matrix_b.create()

            print("The result is:")
            matrix_a.add(matrix_b)

        elif choice == "2":
            print("Enter size of matrix: ")
            matrix_a = Matrix(input())
            print("Enter matrix: ")
            matrix_a.create()

            const = int(input("Enter constant: "))
            print("The result is:")
            matrix_a.multiply(const)

        elif choice == "3":
            print("Enter size of first matrix: ")
            matrix_a = Matrix(input())
            print("Enter first matrix: ")
            matrix_a.create()

            print("Enter size of second matrix: ")
            matrix_b = Matrix(input())
            print("Enter second matrix: ")
            matrix_b.create()
            print("The result is:")
            matrix_a.multiply_matrices(matrix_b)

      
        elif choice == "4":
            print("Enter size of matrix: ")
            matrix_a = Matrix(input())
            print("Enter matrix: ")
            matrix_a.create()
            print("The result is:")
            print(matrix_a.determinant(matrix_a.matrix))
        
       
        else:
            break


menu()
