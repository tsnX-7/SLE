from back_substitution import back_substitution_upper

def Gaussian_elimination_with_partial_pivoting(co_efficient_matrix):
    for i in range(len(co_efficient_matrix) - 1):
        mx_row = i
        mx_val = co_efficient_matrix[i][i]

        for j in range(i+1, len(co_efficient_matrix)):
            if abs(co_efficient_matrix[j][i]) > mx_val:
                mx_val = abs(co_efficient_matrix[j][i])
                mx_row = j

        co_efficient_matrix[i], co_efficient_matrix[mx_row] = co_efficient_matrix[mx_row], co_efficient_matrix[i]

        for k in range(i+1, len(co_efficient_matrix)):
            multiplier = co_efficient_matrix[k][i]/co_efficient_matrix[i][i]
            for j in range(len(co_efficient_matrix[k])):
                co_efficient_matrix[k][j] = co_efficient_matrix[k][j] -  co_efficient_matrix[i][j]*multiplier

    return back_substitution_upper(co_efficient_matrix)
