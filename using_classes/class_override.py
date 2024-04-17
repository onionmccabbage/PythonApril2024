# We have operators for + - / * == < > etc
class Word():
    '''Encapsulate a case-blind string'''
    def __init__(self, word):
        self.word = word
    def __eq__(self, otherWord):
        '''here we override the built in equality operator =='''
        return str(self.word).lower() == str(otherWord.word).lower()

# __ne__ not equal
# __gt__ greater than
# __lt__ less than
# __ge__ and __le__ greater-or-equal and less-or-equal
# __add__( self, other ) self + other
# __sub__( self, other ) self - other
# __mul__( self, other ) self * other
# __floordiv__( self, other ) self // other
# __truediv__( self, other ) self / other
# __mod__( self, other ) self % other
# __pow__( self, other ) self ** other
# __len__ is the length of the object

if __name__ == '__main__':
    w1 = Word('hello')
    w2 = Word('Hello')

    print( w1 == w2 ) # True