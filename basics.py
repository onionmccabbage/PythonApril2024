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

# there are several built in collections in Python
# tuples, lists, sets and dictionaries
# a tuple is an immutable indexed collection of any type
t = (7 , 4, 9, True, s, 'this is clever') # () declare a tuple
print(t[3]) # True
# a list is an indexed collection of any type - can be mutated
l = ['is', 'it', 'coffee', 'yet'] # [] declares a list (members may be of ANY types)
l.append('?') # append as the last member
l.pop() # remove the last member
print(l[2])

# we can use slicing in any indexed collection
print(t[3:6])

# we also have a 'set' - a collection of unique members of any type
values = {3,4,4,5,8,2,3} # we can use {} to declare a set
values.add(9)
values.remove(4)
print(values)

# in conclusion: string and tuple are IMMUTABLE
# list and set are MUTABLE

# we aim to use tuples, since they use less resources (immutable)

# a dict (dictionary) is a NON INDEXED mutable collection of any type
# in Python the key may be of ANY data type, but we tend to use strings (even mixed key types)
unusual = {1:'wow', True:'really?', 3.456:'pi'} # this is legal but not recommended
# duplicate keys take the LAST-defined value
d = {'fn':'Timnit', 'fn':'alternative', 'ln':'Gebru', 'age':43, 'other':l} # {} can also be used to declare a dict:a collection of name:value pairs
print(d)