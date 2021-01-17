class Matrix:
    def __init__(self, list):
        self.list = list

    def __add__(self, other):
        result = []
        for i in range(len(self.list)):
            result.append([])
            for j in range(len(self.list[0])):
                result[i].append(self.list[i][j] + other.list[i][j])
        return '\n'.join(map(str, result))

    def __str__(self):
        return '\n'.join(map(str, self.list))


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[7, 8], [9, 10], [11, 12]])
print(matrix_1 + matrix_2)