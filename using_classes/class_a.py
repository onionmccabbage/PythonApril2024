
# we declare a class
class Person:
    '''This class encapsulates features of a person
    name will be a non-empty string
    age will be a positive integer'''
    # we declare an initializer for this class
    # NB every method of a class MUST take 'self' as an argument
    def __init__(self, n, a): # we can pass in any arguments we like
        # we assign the incoming arguments to 'self'
        # NB when we write self.name it will actually call self.name()
        self.name = n # 'name' and 'age' are now properties of thsi class
        self.age = a  # this will call the setter function for 'age'
    # we can delare functions as methods of tis class
    @property # we declare that 'name' is a property of this class
    def name(self): # this is a property 'getter' accessor
        # double-underscore is called 'name mangling'
        # it is used to avoid direct access to internal properties
        return self.__name # __name is the actual property we are storing
    @name.setter # without this, the property is read-only
    def name(self, new_name): # this is a property 'setter' mutator
        # we can validate the incoming argument
        if type(new_name)==str and new_name !='':
            self.__name=new_name
        else:
            raise TypeError
    @property
    def age(self):
        return self.__age # return the name-mangled value
    @age.setter
    def age(self, new_age):
        if type(new_age)==int and new_age >=0:
            self.__age = new_age
        else:
            self.__age = 12 # we choose a sensible default

if __name__ == '__main__':
    # we make instances of our class
    eth = Person('Ethel', 32)
    tim = Person('Timnit', 43)
    tim.name = 'Timnit Gebru'
    eth.age = -99 # this will end up using the default age of 12
    # we cannot access mangled properties directly
    # print(eth.__name) # this fails - we cannot access mangled members of the class
    print(eth.age, tim.name)
    # we always have access to built-in parts of any object
    print(  Person.__doc__, Person.__dict__ )


