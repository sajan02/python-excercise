class PropSquar(object):
    def __init__(self,value):
        self._value = value
    
    def squaredVal(self):
        return self._value**2

    def setValue(self,value):
        self._value = value

    def delValue(self):
        del self._value

    x = property(squaredVal,setValue,delValue,"computed attribute example")

if __name__ == "__main__":
    p = PropSquar(5)
    print "square of number : {}".format(p.x)