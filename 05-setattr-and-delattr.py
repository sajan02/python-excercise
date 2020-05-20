class Person(object):
    def __init__(self,name, profession=None):
        self.name = name
        self.profession = profession

    def __setattr__(self,attrname,value):
        print "Intercepting attribute assignment,  attr name '{}'".format(attrname)
        object.__setattr__(self,attrname,value)
        print self.__dict__.keys()

    def __delattr__(self,attrname):
        print "Intercepting attribute deletion, attr name '{}'".format(attrname)
        object.__delattr__(self,attrname)
        print self.__dict__.keys()

if __name__ == "__main__":
    p =Person("sajan","Dev")
    print p.name
    print p.profession
    p.skills = "Python"
    print p.skills