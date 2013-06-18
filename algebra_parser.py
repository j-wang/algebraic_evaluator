# algebra_parser.py
# James Wang and Katherine Ye, 18 Jun 2013

"""Simple algebraic parser (without using eval)"""


def parse(exp):
    """algebra-parser.parse:: parse(String)

    Takes a string and returns the evaluated expression as int.
    Uses Shunting-Yard algorithm.

    Ugly as sin.

    """
    operators = ["-", "+", "*", "/"]
    precedence = {"-": 1, "+": 1, "*": 2, "/": 2}
    op_convert = {"-": lambda x, y: x - y,
                  "+": lambda x, y: x + y,
                  "*": lambda x, y: x * y,
                  "/": lambda x, y: x / y}
    final_exp = []
    operator_stack = []

    def parse_helper(prior, post):
        if not post:  # base case, end of recursion
            final_exp.append(prior)  # out of numbers, put prior into exp
            if operator_stack:
                operator_stack.reverse()
                for item in operator_stack:
                    v2 = final_exp.pop()
                    v1 = final_exp.pop()
                    final_exp.append(op_convert[item](v1, v2))
        else:  # more to go
            _next = post[0]
            if prior:  # prior is not none
                if not _next in operators:  # if is number
                    parse_helper(prior * 10 + int(_next), post[1:])
                else:  # if it is an operator
                    final_exp.append(prior)
                    while (operator_stack and
                           precedence[operator_stack[-1]] >=
                           precedence[_next]):
                        op = operator_stack.pop()
                        v2 = final_exp.pop()
                        v1 = final_exp.pop()
                        final_exp.append(op_convert[op](v1, v2))
                    operator_stack.append(_next)
                    parse_helper(None, post[1:])
            else:
                parse_helper(int(_next), post[1:])

    parse_helper(None, exp)
    return final_exp[0]
