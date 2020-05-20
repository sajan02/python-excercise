
class Person(object):
    def __init__(self,name):
        self._name = name
    
    def fget(self):
        """
        Hello I'm getter method
        """
        print "Fetch name"
        return self._name
    
    def fset(self,name):
        print "Set name"
        self._name = name

    def fdel(self):
        print "Deleting name attributes"
        del self._name

    name = property(fget,fset,fdel,"here we go")

class Employee(Person):
    pass

if __name__ == "__main__":
    person = Person('Sajan')
    print "Docstring for person's name attribute: {}".format(Person.name.__doc__)
    print "Person name is {}".format(person.name)
    person.name = "Vishal"
    print "Person name is {}".format(person.name)
    del person.name
    # returns error : no attribute
    # print "Person name is {}".format(person.name)
    print "------------------------->"
    emp = Employee("Hari")
    print emp.name
    print "------------------------->"
    print type(emp)
    print type(Person.name)
    print dir(Person.name)