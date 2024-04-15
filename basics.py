# comments look like this
# we write python code in modules (which are just text files)

a = 3   # integer
b = 7.2 # floating point value

d = a/b # the type of the result respects the matematical operation
f = b**a # ** means raise to the power

# the print statement MUST have brackets
print( type(a), type(b), d, type(f) )

# other mathematical operators
g = b//a # integer division (modulo)
g2 = 12//a
print("the result is", g2, type(g2))
h = b%a # show the remainder (and possibly a calculation error (epsilon) )
print(g, type(g))
print(h)


