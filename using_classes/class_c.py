class Equipment(object): # we may choose to explicitly inherit
    '''a class which has properties for frequency (a positive float) and on/off (a boolean)
    use get/set methods and mangle the property names'''
    def __init__(self, freq, state):
        self.freq = freq
        self.state = state
    @property
    def freq(self):
        # usually we DO use similar identifier for the mangled name as for the get/set methods
        return self.__f # the mangled name does not bear any relationship to the get/set
    @freq.setter
    def freq(self, new_freq):
        if type(new_freq) == float and new_freq>0: # probably ok to be 'int' also
            self.__f = new_freq
        else:
            raise TypeError
    @property
    def state(self):
        return self.__state
    @state.setter
    def state(self, new_state):
        if type(new_state) == bool:
            self.__state = new_state
        else:
            raise TypeError


class Mast(Equipment):
    '''this class has inherited EVEYTHING from the equipment class'''
    # we can have properties (and methods) that belong to the class (rahter than to instances)
    num_instances = 0
    # it is a good idea to declare the poermitted slots for this class
    __slots__ = ['__f', '__state', '__height']
    # in Python there is only ONE __init__
    def __init__(self, freq, state, height):
        # be careful - we need these brackets!!
        super().__init__(freq, state) # call the __init__ method of the parent class
        self.height = height
        Mast.num_instances += 1
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, h):
        if type(h) in (int, float):
            self.__height = h
   
if __name__ == '__main__':
    eq1 = Equipment(888.66, True) # this calls the __init__ function (lkike a constructor)
    m1 = Mast(443.777, False, 33)
    m2 = Mast(443.777, False, 33)
    m3 = Mast(443.777, False, 33)
    m4 = Mast(443.777, False, 33)
    m5 = Mast(443.777, False, 33)
    print(Mast.num_instances)
    print(m1.freq, m1.state, m1.height)
    # by default we can add ANY arbitrary property to any object, such as a class
    m1.__wibbly = 'this is nonsense'
    m1.__wobbly = [3,6,78,4,2,5,9,6,3,True]
    print(m1.wibbly, m1.wobbly)
