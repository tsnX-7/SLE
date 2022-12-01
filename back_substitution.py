def back_substitution_lower(lower_matrix):
    result = [0]*(len(lower_matrix))
    for i in range(len(lower_matrix)):
        sum = 0
        for j in range(i):
            sum += lower_matrix[i][j]*result[j]
        result[i] = (lower_matrix[i][len(lower_matrix)] - sum)/lower_matrix[i][i]
    return result

def back_substitution_upper(co_efficient_matrix):
    result = [0]*(len(co_efficient_matrix))
    for i in range(len(co_efficient_matrix)-1, -1, -1):
        sum = 0
        for j in range(len(co_efficient_matrix)-1, i, -1):
            sum += co_efficient_matrix[i][j]*result[j]
        result[i] = (co_efficient_matrix[i][len(co_efficient_matrix)] - sum)/co_efficient_matrix[i][i]
    return result
