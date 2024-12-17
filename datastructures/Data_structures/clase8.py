#Arrays de dos dimensiones

from clase7 import Array

class Grid():
    def __init__(self, rows, columns, fill_value = None):
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns, fill_value)
    

    def get_height(self):
        return len(self.data)
    

    def get_width(self):
        return len(self.data[0])
    
    def __getitem__(self, index):
        return self.data[index]
    
    def __str__(self):
        result = ""
        for row in range(self.get_height()):
            for col in range (self.get_width()):
                result += str(self.data[row][col]) + " "
            
            result += "\n"
        return str(result)
   

    def __add__(self, item):
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                self.data[row][col] += item
        
"""
matrix = Grid(3 , 3)
print(matrix)

for row in range(matrix.get_height()):
    for column in range(matrix.get_width()):
        matrix[row][column] = row * column


print(matrix)


print(matrix.get_height())

print(matrix.__getitem__(2))

print(matrix.__str__())

matrix.__add__(5)
print(matrix)"""


class Grid2:
    def __init__(self, depth, rows, columns, fill_value = None):
        self.data = Array(depth)
        for d in range(depth):
            self.data[d] = Array(rows)
            for row in range(rows):
                self.data[d][row] = Array(columns, fill_value)
    
    def get_depth(self):
        return len(self.data)
    
    def get_height(self):
        return len(self.data[0])
    
    def get_width(self):
        return len(self.data[0][0])
    
    def __getitem__(self, index):
        return self.data[index]
    
    def __str__(self):
        result = ""
        for d in range(self.get_depth()):
            result += f"Depth {d}:\n"
            for row in range(self.get_height()):
                for col in range(self.get_width()):
                    result += str(self.data[d][row][col]) + " "
                result += "\n"
            result += "\n"
        return str(result)
    
    def __add__(self, item):
        for d in range(self.get_depth()):
            for row in range(self.get_height()):
                for col in range(self.get_width()):
                    self.data[d][row][col] += item

matrix3d = Grid2(2, 3, 3)
print(matrix3d)

for d in range(matrix3d.get_depth()):
    for row in range(matrix3d.get_height()):
        for col in range(matrix3d.get_width()):
            matrix3d[d][row][col] = d * row * col

print(matrix3d)

matrix3d.__add__(5)
print(matrix3d)