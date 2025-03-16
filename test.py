from Matrix import Matrix


matrix = Matrix()

A = matrix.createRandomValueMatrix()
B = matrix.createRandomValueMatrix()
C = matrix.sumMatrices(A, B)

matrix.showMatrices(A, B, C)