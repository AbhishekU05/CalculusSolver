from sympy import *
from sympy.parsing.sympy_parser import parse_expr
from sym import *


def show_options():
    print("1. Enter function")
    print("2. Differentiate")
    print("3. Indefinite Integration")
    print("4. Definite Integration")
    print("5. Differential Equation")
    print("6. Limits")
    print("7. Summation")
    print("8. Exit")


sym_function = sympify("x")
sym_eval_function = sym_function
while true:
    show_options()
    choice = int(input("Enter choice: "))
    if choice == 1:
        sym_function = create_function()
    elif choice == 2:
        sym_eval_function = differentiate_function(sym_function, sym_eval_function)
    elif choice == 3:
        sym_eval_function = indef_int_function(sym_function, sym_eval_function)
    elif choice == 4:
        sym_eval_function = def_int_function(sym_function, sym_eval_function)
    elif choice == 5:
        pass
    elif choice == 6:
        sym_eval_function = lim_function(sym_function, sym_eval_function)
    elif choice == 7:
        pass
    else:
        break
    print("------------------------------------------")
    print("##########################################")


print("Thank you for using the application")
