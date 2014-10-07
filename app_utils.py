def check_for_asterisks(equation):
    i = 0
    while i < len(equation):
        if equation[i].isalpha():
            if i != 0 and equation[i-1] != "*":
                if equation[i-1].isalnum():
                    equation = equation[:i] + "*" + equation[i:]
                    i += 1
            if i+1 != len(equation) and equation[i+1] != "*":
                if equation[i+1].isalnum():
                    equation = equation[:i+1] + "*"  + equation[i+1:]
                    i += 1
        elif equation[i] == "(":
            if i != 0 and equation[i-1] != "*":
                if equation[i-1].isalnum():
                    equation = equation[:i] + "*" + equation[i:]
                    i += 1
        elif equation[i] == ")":
            if i+1 != len(equation) and equation[i+1] != "*":
                if equation[i+1].isalnum():
                    equation = equation[:i+1] + "*" + equation[i+1:]
                    i += 1
        i += 1
    return equation
