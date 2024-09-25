from sympy import *
from sympy.parsing.sympy_parser import parse_expr


def convert_to_sympy(user_input):
    user_input = user_input.strip()
    try:
        sympy_expr = parse_expr(user_input, transformations = "all")
        return sympy_expr
    except Exception as e:
        return f"Error in parsing expression: {e}"

def display_output(expression, header = "Expression:", constant = ''):
    print(header)
    if (constant == ''):
        pprint(expression, use_unicode=true)
    else:
        pprint(expression + symbols(constant), use_unicode=true)

def function_variables(expression):
    return set(expression.free_symbols)

def create_function():
    uinput = input("Enter the expression: ")
    sympy_output = convert_to_sympy(uinput)
    display_output(sympy_output)
    print("Variables used:", function_variables(sympy_output))
    return sympy_output

def user_function(prev_function, prev_eval_function):
    print("1. Use previous base function")
    print("2. Use previous evaluated function")
    print("3. New function")
    choice = int(input("Enter choice: "))
    if choice == 1:
        display_output(prev_function)
        print("Variables used:", function_variables(prev_function))
        return prev_function
    elif choice == 2:
        display_output(prev_eval_function)
        print("Variables used:", function_variables(prev_eval_function))
        return prev_eval_function
    else:
        return create_function()

def differentiate_function(prev_function, prev_eval_function):
    func = user_function(prev_function, prev_eval_function)
    var = [func]
    iter = function_variables(func)
    for i in iter:
        print("How many times to differentiate wrt", i, "?")
        var.append(i)
        var.append(int(input()))
    uneval_diff_func = Derivative(*tuple(var))
    display_output(uneval_diff_func, "Derivative:")
    eval_diff_func = uneval_diff_func.doit()
    print("------------------------------------------")
    display_output(eval_diff_func, "Evaluated Derivative:")
    return eval_diff_func

def indef_int_function(prev_function, prev_eval_function):
    func = user_function(prev_function, prev_eval_function)
    iter = function_variables(func)
    nvar = len(iter)
    
    if (nvar == 1):
        uneval_int = Integral(func, iter.pop())
    elif (nvar == 0):
        uneval_int = Integral(func, symbols('x'))
    else:
        var = [func]
        for i in iter:
            print("Integrate wrt", i, "? [y/n]")
            choice = input()
            if (choice == 'y'):
                var.append(i)
        if (var == [func]):
            uneval_int = Integral(func, iter.pop())
        else:
            uneval_int = Integral(*tuple(var))
    
    display_output(uneval_int, "Integral:")
    eval_int = uneval_int.doit()
    print("------------------------------------------")
    display_output(eval_int, "Evaluated Integral:", 'C')
    return eval_int

def def_int_function(prev_function, prev_eval_function):
    func = user_function(prev_function, prev_eval_function)
    iter = function_variables(func)
    nvar = len(iter)
    
    if nvar == 1:
        llim = sympify(input("Enter lower limit: "))
        ulim = sympify(input("Enter upper limit: "))
        uneval_int = Integral(func, (iter.pop(), llim, ulim))
    elif nvar == 0:
        llim = sympify(input("Enter lower limit: "))
        ulim = sympify(input("Enter upper limit: "))
        uneval_int = Integral(func, (symbols("x"), llim, ulim))
    else:
        var = [func]
        for i in iter:
            print("Integrate wrt", i, "? [y/n]")
            choice = input()
            if choice == "y":
                llim = sympify(input("Enter lower limit: "))
                ulim = sympify(input("Enter upper limit: "))
                var.append((i, llim, ulim))
        if var == [func]:
            llim = sympify(input("Enter lower limit: "))
            ulim = sympify(input("Enter upper limit: "))
            uneval_int = Integral(func, (iter.pop(), llim, ulim))
        else:
            uneval_int = Integral(*tuple(var))
    
    display_output(uneval_int, "Integral:")
    eval_int = uneval_int.doit()
    print("------------------------------------------")
    display_output(eval_int, "Evaluated Integral:")
    return eval_int

def lim_function(prev_function, prev_eval_function):
    func = user_function(prev_function, prev_eval_function)
    iter = function_variables(func)
    nvar = len(iter)

    if nvar == 0:
        return func
    elif nvar == 1:
        var = iter.pop()
        print("Enter what", var, "tends to: ")
        con = sympify(input())
        print("1. Right limit")
        print("2. Left limit")
        print("3. Normal limit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            uneval_lim = Limit(func, var, con, '+')
        elif choice == 2:
            uneval_lim = Limit(func, var, con, '-')
        else: 
            uneval_lim = Limit(func, var, con)
    else:
        print("Enter order of execution of limits [first is innermost]")
        order = []
        j = input()
        k = 0
        for i in j:
            if i != ' ':
                order.append(sympify(i))
            k += 1
        
        uneval_lim = func
        for i in order:
            print("Enter what", i, "tends to: ")
            con = sympify(input())
            print("1. Right limit")
            print("2. Left limit")
            print("3. Normal limit")
            choice = int(input("Enter choice: "))
            if choice == 1:
                uneval_lim = Limit(uneval_lim, i, con, "+")
            elif choice == 2:
                uneval_lim = Limit(uneval_lim, i, con, "-")
            else:
                uneval_lim = Limit(uneval_lim, i, con)

    display_output(uneval_lim, "Limit:")
    eval_lim = uneval_lim.doit()
    print("------------------------------------------")
    display_output(eval_lim, "Evaluated Limit:")
    return eval_lim
