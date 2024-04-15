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

# using strings (we can encode new line as \n and tab as \t)
s = 'is it coffee\n time yet' # python can use single or double quotes
s2 = '''we can use triple quotes (or triple double quotes) 
which will preseve new lines                and other formating features'''
# strings are an indexed collection of characters, accessible by slicing
print(s2[0]) # we can access zero-based members of the collection
print(s2[3:12]) # we can use slicing: [start:stop-before:step]
j = s+s2
k = s*4
print(j, k)
# more commonly we use join
r = s.join('-')
print(r)