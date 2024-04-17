class Point(): # by default every class inherits from object
    '''we encapsulate a point defined by x and y
    we then derive the hypotenuse'''
    def __init__(self, x, y):
        self.x = x
        self.y = y
    @property # here is the property getter
    def x(self):
        return self.__x
    @x.setter
    def x(self, new_x): # here is the property setter
        if type(new_x) in (int, float):
            self.__x = new_x
        else:
            self.__x = 3
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, new_y):
        if type(new_y) in (int, float):
            self.__y = new_y
        else:
            self.__y = 4
    # we can derive the hypotenuse
    def getHyp(self):
        h = (self.__x**2 + self.__y**2)**0.5
        return h
    def __str__(self): # remember, any print statement will make use of __str__
        '''we can override the built-in __str__ method with our own'''
        #              we can call the getter self.x and self.y
        return f'The point at x:{self.x} y:{self.y} has h:{self.getHyp()}'
    def __repr__(self):
        '''we may also choose to override __repr__ (for output in immediate mode python)'''
        return f'{self.x} and {self.y} give h={self.getHyp()}'
    
if __name__ == '__main__':
    p1 = Point(3,4)
    p1.x = False # this will set the default value
    # p1.x will call the getter method to retrieve __x
    print(p1.x, p1.y, p1.getHyp() ) # 3, 4, 5.0
    print(p1) # by default, just shows the class name. Or use our __str__ method