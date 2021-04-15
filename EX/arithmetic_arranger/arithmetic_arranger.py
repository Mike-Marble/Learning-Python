def arithmetic_arranger(problems, solve=False):
    top = ''
    op = ''
    bot = ''
    dash = ''
    solution = ''
    line = ''
    tab = '    '
    #            ***** TOP OF LOOP IS ERROR REPORTING *****
    # check number of problems if more than 5 return error and quit
    if len(problems) > 5:
        return 'Error: Too many problems.'
        quit()
    # split the problems and add them to their respective lists
    for problem in problems:
        p = problem.split()
        first = (p[0])
        operator = (p[1])
        last = (p[2])
        # Check for valid digits
        if not first.isnumeric() or not last.isnumeric():
            return 'Error: Numbers must only contain digits.'
        # check for digit length of 4 or less
        if len(first) > 4 or len(last) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        # Check for valid operators
        if operator == '+':
            value = int(first) + int(last)
        elif operator == '-':
            value = int(first) - int(last)
        else:
            return "Error: Operator must be '+' or '-'."
    #       ***** BOTTOM OF LOOP IS INFO GATHERING *****
            # Gets info for formatting dashes & operator
        if len(first) >= len(last):
            a = len(first) + 2
        else:
            a = len(last) + 2
        if a == 3:
            dash = '---'
        elif a == 4:
            dash = '----'
        elif a == 5:
            dash = '-----'
        else:
            dash = '------'
        # setting variables for final formatting
        top = top + str(first).rjust(a)+tab
        bot = bot + operator + str(last).rjust(a-1)+tab
        line = line + dash.rjust(a) + tab
        solution = solution + str(value).rjust(a) + tab
    # final formatting
    if solve:
        arranged_problems = top.rstrip() + '\n' + bot.rstrip() + '\n' + \
            line.rstrip() + '\n' + solution.rstrip()
    else:
        arranged_problems = top.rstrip() + '\n' + bot.rstrip() + '\n' + line.rstrip()
    # Send it
    return arranged_problems
