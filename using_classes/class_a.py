
# we declare a class
class Person:
    '''This class encapsulates features of a person
    name will be a non-empty string
    age will be a positive integer'''
    # we declare an initializer for this class
    # NB every method of a class MUST take 'self' as an argument
    def __init__(self, n, a): # we can pass in any arguments we like
        # we assign the incoming arguments to 'self'
        self.name = n # 'name' and 'age' are now properties of thsi class
        self.age = a
    # we can delare functions as methods of tis class
    @property # we declare that 'name' is a property of this class
    def name(self): # this is a property 'getter' accessor
        # double-underscore is called 'name mangling'
        # it is used to avoid direct access to internal properties
        return self.__name
    @name.setter # without this, the property is read-only
    def name(self, new_name): # this is a property 'setter' mutator
        # we can validate the incoming argument
        if type(new_name)==str and new_name !='':
            self.__name=new_name
        else:
            raise TypeError

if __name__ == '__main__':
    # we make instances of our class
    eth = Person('Ethel', 32)
    tim = Person('Timnit', 43)
    tim.name = 'Timnit Gebru'
    # we cannot access mangled properties directly
    print(eth.__name)
    print(eth.age, tim.name)


