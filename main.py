import sympy as sp

limit_symbol = sp.symbols('x')

x_neighborhood = input("Enter the value of x for neighborhood (or 'oo' for infinity): ")
x_neighborhood = sp.oo if x_neighborhood == 'oo' else -sp.oo if x_neighborhood == '-oo' else int(x_neighborhood)
r = sp.limit(2*limit_symbol - 7, limit_symbol, x_neighborhood)

print(f"{r} is {'Infinite' if r == sp.oo or r == -sp.oo else 'not Infinite'}")