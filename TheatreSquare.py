import math
def theatre_square(M, N, s):

    vertical = math.ceil(N/s)
    horizontal = math.ceil(M/s)
    return vertical * horizontal
