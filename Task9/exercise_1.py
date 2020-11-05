# Implement a function which receives a string and replaces all `"` symbols with `'` and vise versa.

def replace_quote(expr: str) -> str:
    single_quote = "'"
    double_quote = '"'
    swappp = 'swappp'
    expr = expr.replace(single_quote, swappp)
    expr = expr.replace(double_quote, single_quote)
    expr = expr.replace(swappp, double_quote)
    return expr


if __name__ == "__main__":
    expr = """
    "On election night, I think it's very likely the market declares the winner before the news networks," 
    Ed Mills, policy analyst at Raymond James, told CNN Business.
    """
    print(f"Original text: \n{expr}")
    print(f"Modified text: \n{replace_quote(expr)}")
