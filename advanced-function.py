def add(a, b):
    return a + b

addfunc = add # Save 'add' function
print('addfunc(100, 200):', addfunc(100, 200))

def f(g, a, b): # Pass 'g' function
    return g(a, b)
print('f(add, 200, 300):',f(add, 200, 300))
print('')

def deco(type='bold'):
    def italic(s):
        return '<i>' + s + '</i>'
    def bold(s):
        return '<b>' + s + '</b>'
    if type == 'italic':
        return italic    # Return Function
    else:
        return bold    #Return Function
dec = deco()
print('dec=deco(), dec("Hello, Nice to meet you."):', dec("Hello, Nice to meet you."))
dec = deco('italic')
print('dec=deco(), dec("Hello, Nice to meet you."):', dec("Hello, Nice to meet you."))
print('')

l = lambda x, y : x + y
print("lambda x, y : x + y -> l(10, 20):",l(10, 20))