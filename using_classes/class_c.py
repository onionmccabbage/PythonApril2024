
class Equipment():
    '''a class which has properties for frequency (a positive float) and on/off (a boolean)
    use get/set methods and mangle the property names'''
    def __init__(self, freq, state):
        self.freq = freq
        self.state = state
    @property
    def freq(self):
        return self.__freq
    @freq.setter
    def freq(self, new_freq):
        if type(new_freq) == float and new_freq>0:
            self.__freq = new_freq
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
    
if __name__ == '__main__':
    eq1 = Equipment(888.66, True))