from back_substitution import back_substitution_upper

def Gaussian_elimination(co_efficient_matrix):
    for i in range(len(co_efficient_matrix) - 1):
        for k in range(i+1, len(co_efficient_matrix)):
            multiplier = co_efficient_matrix[k][i]/co_efficient_matrix[i][i]
            for j in range(len(co_efficient_matrix[k])):
                co_efficient_matrix[k][j] = co_efficient_matrix[k][j] - co_efficient_matrix[i][j]*multiplier
    return back_substitution_upper(co_efficient_matrix)
