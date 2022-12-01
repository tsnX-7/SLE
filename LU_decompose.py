from back_substitution import back_substitution_lower
from back_substitution import back_substitution_upper
from copy import deepcopy

def Find_LU(UTM):
    n = len(UTM)
    LTM = deepcopy(UTM)
    for i in range(len(LTM)):
        for j in range(len(LTM[i])):
            if i == j:
                LTM[i][j] = 1
            elif j > i:
                LTM[i][j] = 0
    for i in range(len(UTM) - 1):
        for k in range(i+1, len(UTM)):
            multiplier = UTM[k][i] / UTM[i][i]
            LTM[k][i] = multiplier
            for j in range(len(UTM[k])):
                UTM[k][j] = UTM[k][j] - UTM[i][j]*multiplier
    return UTM, LTM

def find_inverse():
    order = int(input("Order of the square matrix for finding inverse: "))
    if order < 1:
        raise Exception("Invalid order!")

    matrix = []

    for i in range(order):
        print("Please enter the row number " + str(i+1) + ": ")
        temp_list = list(map(float, input().split()))
        if len(temp_list) != order:
            raise Exception("Input error!!!")
        matrix.append(temp_list)
    Upper, Lower = Find_LU(matrix)
    for row in Lower:
        row.append(0)
    for j in range(order):
        Upper[j].append(0)
    Inverse = []
    for i in range(order):
        Lower[i][len(Lower)] = 1

        # [L][Z]=[C]
        Z = back_substitution_lower(Lower)

        for j in range(order):
            Upper[j][len(Upper)] = Z[j]
        result = back_substitution_upper(Upper)

        # later it will be transposed
        Inverse.append(result)
        Lower[i][len(Lower)] = 0
    for i in range(order):
        for j in range(i+1):
            Inverse[i][j], Inverse[j][i] = round(
                Inverse[j][i], 5), round(Inverse[i][j], 5)
    print("The inverse of the given matrix is:")

    format_row = "{:>12}" * (len(Inverse[0]))
    for row in Inverse:
        print(format_row.format(*row))
