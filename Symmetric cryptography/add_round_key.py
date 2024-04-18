import numpy
state = numpy.array( [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
])

round_key = numpy.array( [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
])


def add_round_key(s, k):
        return s ^ k
        
def matrix2bytes(matrix):
    
    return matrix.tobytes()


print(matrix2bytes(add_round_key(state, round_key)).decode())

