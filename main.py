from select import select

from Input import Input
import LU_decompose
from Gaussian_elimination import Gaussian_elimination
from Gaussian_elimination_with_partial_pivoting import Gaussian_elimination_with_partial_pivoting


def Print_solution(result):
    print("The solution of the system is:")
    for i in range(len(result)):
        print('X' + str(i+1) + " = " + str(result[i]))


print("Please select from the following: ")
print("1. Solving System of Linear Equation")
print("2. Finding Inverse Matrix")

selection = int(input('You selected: '))

if selection == 1:
    print("Choose a method for solving equation: ")
    print("1. Naive Gaussian Elimination")
    print("2. Gaussian Elimination with Partial Pivoting")
    second_selection = int(input("Your method: "))
    if (second_selection == 1):
        co_efficient_matrix = Input()
        Print_solution(Gaussian_elimination(co_efficient_matrix))
    elif second_selection == 2:
        co_efficient_matrix = Input()
        Print_solution(Gaussian_elimination_with_partial_pivoting(co_efficient_matrix))
    else:
        raise Exception("Invalid choice!")
elif selection == 2:
    LU_decompose.find_inverse()
else:
    raise Exception("Invalid choice!")
