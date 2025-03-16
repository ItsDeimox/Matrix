from random import randint
import math

class Matrix:
    def __init__(self):
        self.pi = math.pi
        self.hpi = math.pi / 2
    
    def create(self, x: int = 3, y: int = 3, cellValue: int = 0) -> list:
        matrix = [[cellValue for _ in range(y)] for _ in range(x)]
        return matrix
    
    def createRandomMatrix(self, minX: int = 1, maxX: int = 10, minY: int = 1, maxY: int = 10, minCell: int = 0, maxCell: int = 10) -> list:
        matrixX = randint(minX, maxX)
        matrixY = randint(minY, maxY)
        matrix = [[randint(minCell, maxCell) for _ in range(matrixY)] for _ in range(matrixX)]
        return matrix
    
    def createRandomValueMatrix(self, x: int = 3, y: int = 3, min: int = 0, max: int = 10) -> list:
        matrix = [[randint(min, max) for _ in range(y)] for _ in range(x)]
        return matrix
    
    def createLinearIncraseMatrix(self, x: int = 3, y: int = 3) -> list:
        i = 0
        matrix = []
        for line in range(x):
            matrix.append([])
            for _ in range(y):
                i += 1
                matrix[line].append(i)
        return matrix
    
    def getMatrixSize(self, matrix: list) -> tuple:
        w = self.getLineSize(matrix)
        h = self.getColSize(matrix)
        return (w, h)
    
    def compareMatrices(self, A: list, B: list) -> bool:
        w1, h1 = self.getMatrixSize(A)
        w2, h2 = self.getMatrixSize(B)
        if w1 != w2 or h1 != h2:
            print('<AVISO> As matrizes devem ser do mesmo tamanho')
            return False
        return True
    
    def cloneMatrix(self, matrix: list) -> list:
        clone = []
        width, height = self.getMatrixSize(matrix)
        for y in range(height):
            clone.append([])
            for x in range(width):
                clone[y].append(matrix[y][x])
        return clone
    
    def sumMatrices(self, A: list, B: list) -> list:
        if not self.compareMatrices(A, B): return
        
        matrix = self.cloneMatrix(A)
        width, heiht = self.getMatrixSize(matrix)
        for y in range(heiht):
            for x in range(width):
                matrix[y][x] += B[y][x]
        return matrix
    
    def getMatrixSum(self, matrix: list) -> int:
        s = 0
        for y in range(len(matrix)):
            s += self.sumLine(matrix, y)
        return s
    
    def sumLine(self, matrix: list, line: int) -> int:
        s = 0
        for l in matrix[line]:
            s += l
        return s
    
    def sumCol(self, matrix: list, col: int) -> int:
        s = 0
        for l in matrix:
            s += l[col]
        return s
    
    def sumLines(self, A: list, B: list, ALine: int, BLine: int) -> int:
        s1 = self.sumLine(A, ALine)
        s2 = self.sumLine(B, BLine)
        s = s1 + s2
        return s
    
    def composeCompare(self, A: list, B:  list) -> bool:
        lineA = self.getLineSize(A)
        colB = self.getColSize(B)
        if lineA != colB:
            print('<AVISO> O tamanho da linha A deve ser igual ao tamanho da coluna B')
            return False
        return True
    
    def composeLineWithCol(self, A: list, B: list, ALine: int, BCol: int) -> int:
        if not self.composeCompare(A, B): return
        
        s = 0
        Bheight = self.getColSize(B)
        for y in range(Bheight):
            s += A[ALine][y] * B[y][BCol]
        return s
    
    def getBiggerLineValue(self, A: list, B: list) -> int:
        ah = self.getLineSize(A)
        bh = self.getLineSize(B)
        return ah if ah > bh else bh

    def getBiggerColValue(self, A: list, B: list) -> int:
        aw = self.getColSize(A)
        bw = self.getColSize(B)
        return aw if aw > bw else bw
    
    def getMinorLineValue(self, A: list, B: list) -> int:
        ah = self.getLineSize(A)
        bh = self.getLineSize(B)
        return ah if ah < bh else bh

    def getMinorColValue(self, A: list, B: list) -> int:
        aw = self.getColSize(A)
        bw = self.getColSize(B)
        return aw if aw < bw else bw

    def getBiggerMatrixLine(self, A: list, B: list) -> list:
        aw = self.getLineSize(A)
        bw = self.getLineSize(B)
        return A if aw > bw else B
    
    def getBiggerMatrixCol(self, A: list, B: list) -> list:
        aw = self.getColSize(A)
        bw = self.getColSize(B)
        return A if aw > bw else B
    
    def compose(self, A: list, B: list) -> list:
        if not self.composeCompare(A, B): return

        line = self.getLineSize(B)
        col = self.getColSize(A)
        matrix = self.create(col, line)
        for y in range(col):
            for x in range(line):
                matrix[y][x] = self.composeLineWithCol(A, B, y, x)
        return matrix
    
    def getMatrixCenter(self, matrix: list) -> tuple:
        a = 1 if len(matrix) > 3 else 0
        hx = (self.getLineSize(matrix) + a) / 2
        hy = (self.getColSize(matrix) + a) / 2
        return (hx, hy)
    
    def firstQuadReduction(self, angle: float) -> float:
        return angle - self.hpi * angle // math.pi
    
    def degToRad(self, deg: float) -> float:
        return deg / 180 * math.pi
    
    def radToDeg(self, rad: float) -> float:
        return rad / math.pi * 180
    
    def rotate(self, matrix: list, t: int = 1) -> list:
        t = t % 4
        if t == 0: return matrix
        
        mx, my = self.getMatrixSize(matrix)
        newMatrix = self.create(mx, my)
        
        for y in range(my):
            for x in range(mx):
                newMatrix[x][y] = matrix[y][x]
        newMatrix = newMatrix[::-1]
        
        if t > 0: return self.rotate(newMatrix, t - 1)
        return newMatrix
    
    def getCompositionValue(self, A: list, B: list) -> int:
        s = 0
        composition = self.compose(A, B)
        for y in composition:
            for x in y:
                s += x
        return s
    
    def getDistance(self, position1: tuple, position2: tuple, squared: bool = False) -> float:
        dx = (position1[0] - position2[0])
        dy = (position1[1] - position2[1])
        distance = (dx ** 2 + dy ** 2)
        if not squared: distance = distance ** (1/2)
        return distance
    
    def getAngle(self, cat: float, rad: float) -> float:
        if rad == 0: return 0
        return math.asin(cat/rad)
    
    def getPositionByAngle(self, angle: float, rad: float) -> tuple:
        return (math.sin(angle) * rad, math.cos(angle) * rad)
    
    def getLineSize(self, matrix: list) -> int:
        return len(matrix[0])
    
    def getColSize(self, matrix: list) -> int:
        return len(matrix)
    
    def show(self, matrix: list) -> None:
        if not matrix: return
        w = len(matrix[0])
        h = len(matrix)
        print(f'\nMatriz({h}X{w})')
        for y in matrix:
            print(y)
        print()
        print(f'Soma dos elementos: {self.getMatrixSum(matrix)}')
        print()
    
    def showMatrices(self, *matrices: list) -> None:
        for matrix in matrices:
            self.show(matrix)