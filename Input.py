# from finding_LU_matrix import Finding_LU
# from gaussian_elimination_with_partial_pivoting import Gaussian_elimination_with_partial_pivoting
# from gaussian_elimination import Gaussian_elimination
#

def Input():
    number_of_unknown = int(input("Enter no. of unknowns in the system of linear equation: "))

    co_efficient_matrix = []
    for i in range(number_of_unknown):
        print("Input the coefficients of equation- " + str(i+1))

        for i in range(number_of_unknown+1):
            if i == number_of_unknown:
                print(chr(i+97), end='\n')
            elif i == number_of_unknown - 1:
                print(f'{chr(i+97)}x{i + 1}', end=' = ')
            else:
                print(f'{chr(i+97)}x{i + 1}', end=' + ')

        co_efficient = list(map(float, input().split()))

        if len(co_efficient) != number_of_unknown + 1:
            raise Exception('Input error!!!')

        co_efficient_matrix.append(co_efficient)
    return co_efficient_matrix
