def add(a, b):
    return a + b

addfunc = add # Save 'add' function
print('addfunc(100, 200):', addfunc(100, 200))

def f(g, a, b): # Pass 'g' function
    return g(a, b)
print('f(add, 200, 300):',f(add, 200, 300))