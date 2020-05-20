# Descriptors are classess which have get, set nad del methods also 
# descriptor follows descriptor protocol that says that it has get,set and del method

class Name(object):
    def __get__(self, instance, owner):
        print "Fetching name"
        return instance._name
    def __set__(self, instance, value):
        print "Setting name"
        if value.isalpha():
            instance._name = value
        else:
            raise AttributeError("is not alphabet")
    def __del__(self, instance):
        del instance._name

class Person(object):
    def __init__(self,name):
        if name.isalpha():
            self._name = name
        else:
            raise AttributeError("is not alphabet")
    name = Name()

if __name__ == "__main__":
    p =Person("12")
    print p.name
