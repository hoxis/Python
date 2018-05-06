class Person(object):
    __slots__ = ("name" ,"age")

xi = Person()
xi.name = "xixi"
print(xi.name)
# xi.address = "China"

class Man(Person):
    pass
mi = Man()
mi.address = "JS"
print(mi.address)