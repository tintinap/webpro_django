class Cookie():
    def __init__(self, shape, size, cookie_type):
        self._shape = shape
        self._size = size
        self.cookie_type = cookie_type
        self.status = 'raw'

    #display text when print object
    def __str__(self):
        return 'My %s Cookie' % self.cookie_type

    #all 3 below use to display boolean
    def __lt__(self, other):
        return self._size < other.size

    def __gt__(self, other):
        return self._size > other.size

    def __eq__(self, other):
        return self._size == other.size

    #like constructor (__init__) but u can call it anytime like
    # x =Foo() #create class with no attribute
    #x(1,,2,3) #this one is __call__
    def __call__(self, shape, size, cookie_type):
        self.shape = shape
        self.size = size
        self.cookie_type = cookie_type
        self.status = 'raw'

    @property
    def shape(self):
        return self._shape

    @shape.setter
    def setshape(self, value):
        self._shape = 'shape of cookie is ' + value

    def bake(self):
        self.status = 'BAKED'

    @staticmethod
    def cut():
        print('The cookie is cut.')


class Brownie(Cookie):
    def __init__(self, shape, size, cookie_type, chocochips):
        Cookie.__init__(self, shape, size, cookie_type)
        self.chocochips = chocochips

    def __lt__(self, other):
        return self.chocochips < other.chocochips

    def __gt__(self, other):
        return self.chocochips > other.chocochips

    def eat(self):
        print('YUM YUM')
        self.chocochips -= 1


brownie1 = Brownie('round', 20, 'Chololate', 10)
brownie2 = Brownie('round', 15, 'Chololate', 15)
print(brownie1.shape)
brownie1.setShape = 'square'
print(brownie1.shape)
brownie1.bake()
brownie1.eat()
print(brownie1.chocochips)

print(brownie1 > brownie2)
