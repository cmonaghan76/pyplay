import re

class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = [[int(i) for i in re.split(" +", row)] for row in re.split("\n+", matrix_string)]

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        return [row[index-1] for row in self.matrix]