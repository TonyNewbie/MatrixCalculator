class Matrix:
    def __init__(self, rows, columns):
        self.rows = int(rows)
        self.columns = int(columns)
        self.content = [[0 for _ in range(self.columns)] for _ in range(self.rows)]

    def __add__(self, other):
        result = Matrix(self.rows, self.columns)
        if self.rows != other.rows or self.columns != other.columns:
            result.content = 'The operation cannot be performed.\n'
            return result
        else:
            for i in range(self.rows):
                for j in range(self.columns):
                    result.content[i][j] = self.content[i][j] + other.content[i][j]
        return result

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result = Matrix(self.rows, self.columns)
            for i in range(self.rows):
                for j in range(self.columns):
                    result.content[i][j] = self.content[i][j] * other
            return result
        elif isinstance(other, Matrix):
            result = Matrix(self.rows, other.columns)
            if self.columns != other.rows:
                result.content = 'The operation cannot be performed.\n'
            else:
                for i in range(self.rows):
                    for j in range(other.columns):
                        for k in range(self.columns):
                            result.content[i][j] += self.content[i][k] * other.content[k][j]
            return result

    def __str__(self):
        if isinstance(self.content, str):
            return self.content
        else:
            result = 'The result is:\n'
            for i in range(self.rows):
                for j in range(self.columns):
                    if self.content[i][j].is_integer():
                        self.content[i][j] = int(self.content[i][j])
                    else:
                        self.content[i][j] = self.content[i][j]
            for i in range(self.rows):
                result += f'{" ".join([str(item) for item in self.content[i]])} \n'
            return result

    def matrix_input(self):
        self.content = [[float(j) for j in input().split()] for _ in range(self.rows)]

    def main_transpose(self):
        result = Matrix(self.columns, self.rows)
        for i in range(self.rows):
            for j in range(self.columns):
                result.content[j][i] = self.content[i][j]
        return result

    def side_transpose(self):
        result = Matrix(self.columns, self.rows)
        for i in range(self.rows):
            for j in range(self.columns):
                result.content[j][i] = self.content[self.rows - i - 1][self.columns - j - 1]
        return result

    def vertical_transpose(self):
        result = Matrix(self.columns, self.rows)
        for i in range(self.rows):
            for j in range(self.columns):
                result.content[i][j] = self.content[i][self.columns - j - 1]
        return result

    def horizontal_transpose(self):
        result = Matrix(self.columns, self.rows)
        for i in range(self.rows):
            for j in range(self.columns):
                result.content[i][j] = self.content[self.rows - i - 1][j]
        return result

    def get_minor(self, row_index, column_index):
        minor = []
        i_bias = 0
        for i in range(self.rows - 1):
            row = []
            j_bias = 0
            if i == row_index:
                i_bias = 1
            for j in range(self.columns - 1):
                if j == column_index:
                    j_bias = 1
                row.append(self.content[i + i_bias][j + j_bias])
            minor.append(row)
        return minor

    def determinant(self):
        if self.rows == 1:
            return self.content[0][0]
        if self.rows == 2:
            return self.content[0][0] * self.content[1][1] - self.content[0][1] * self.content[1][0]
        else:
            k = 1
            det = 0
            for i in range(self.rows):
                minor = Matrix(self.rows - 1, self.rows - 1)
                minor.content = self.get_minor(i, 0)
                det += k * self.content[i][0] * minor.determinant()
                k = -k
            return det

    def inverse(self):
        result = Matrix(self.rows, self.columns)
        if self.determinant() == 0:
            result.content = "This matrix doesn't have an inverse.\n"
        else:
            for i in range(self.rows):
                for j in range(self.columns):
                    minor = Matrix(self.rows - 1, self.rows - 1)
                    minor.content = self.get_minor(i, j)
                    result.content[i][j] = pow(-1, i + j) * minor.determinant()
            result = result.main_transpose()
            result = result * (1 / self.determinant())
        return result


class MatrixCalculator:
    @staticmethod
    def run_calculation():
        menu = ('1. Add matrices\n'
                '2. Multiply matrix by a constant\n'
                '3. Multiply matrices\n'
                '4. Transpose matrix\n'
                '5. Calculate a determinant\n'
                '6. Inverse matrix\n'
                '0. Exit')
        transpose_menu = ('1. Main diagonal\n'
                          '2. Side diagonal\n'
                          '3. Vertical line\n'
                          '4. Horizontal line')
        print(menu)
        operation = input('Your choice: ')
        while operation != '0':
            if operation == '1':
                matrix_a_rows, matrix_a_columns = input('Enter size of first matrix: ').split()
                matrix_a = Matrix(matrix_a_rows, matrix_a_columns)
                print('Enter first matrix: ')
                matrix_a.matrix_input()
                matrix_b_rows, matrix_b_columns = input('Enter size of second matrix: ').split()
                matrix_b = Matrix(matrix_b_rows, matrix_b_columns)
                print('Enter second matrix: ')
                matrix_b.matrix_input()
                print(matrix_a + matrix_b)
            elif operation == '2':
                matrix_a_rows, matrix_a_columns = input('Enter size of matrix: ').split()
                matrix_a = Matrix(matrix_a_rows, matrix_a_columns)
                print('Enter matrix: ')
                matrix_a.matrix_input()
                constant = float(input('Enter constant: '))
                print(matrix_a * constant)
            elif operation == '3':
                matrix_a_rows, matrix_a_columns = input('Enter size of first matrix: ').split()
                matrix_a = Matrix(matrix_a_rows, matrix_a_columns)
                print('Enter first matrix: ')
                matrix_a.matrix_input()
                matrix_b_rows, matrix_b_columns = input('Enter size of second matrix: ').split()
                matrix_b = Matrix(matrix_b_rows, matrix_b_columns)
                print('Enter second matrix: ')
                matrix_b.matrix_input()
                print(matrix_a * matrix_b)
            elif operation == '4':
                print(transpose_menu)
                transpose_option = input('Your choice: ')
                matrix_a_rows, matrix_a_columns = input('Enter matrix size: ').split()
                matrix_a = Matrix(matrix_a_rows, matrix_a_columns)
                print('Enter matrix: ')
                matrix_a.matrix_input()
                if transpose_option == '1':
                    print(matrix_a.main_transpose())
                elif transpose_option == '2':
                    print(matrix_a.side_transpose())
                elif transpose_option == '3':
                    print(matrix_a.vertical_transpose())
                elif transpose_option == '4':
                    print(matrix_a.horizontal_transpose())
            elif operation == '5':
                matrix_a_rows, matrix_a_columns = input('Enter matrix size: ').split()
                matrix_a = Matrix(matrix_a_rows, matrix_a_columns)
                print('Enter matrix: ')
                matrix_a.matrix_input()
                print(matrix_a.determinant())
            elif operation == '6':
                matrix_a_rows, matrix_a_columns = input('Enter matrix size: ').split()
                matrix_a = Matrix(matrix_a_rows, matrix_a_columns)
                print('Enter matrix: ')
                matrix_a.matrix_input()
                print(matrix_a.inverse())
            else:
                print('There is no such operation!\n')
            print(menu)
            operation = input('Your choice: ')


calculator = MatrixCalculator()
calculator.run_calculation()
