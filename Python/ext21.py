def add(a, b):
    print "%d + %d" %(a, b)
    return a + b

def subtract(a, b):
    print "%d - %d" %(a, b)
    return a - b

def multiply(a, b):
    print "%d * %d" %(a, b)
    return a * b
def divide(a, b):
    print "%d / %d" %(a, b)
    return a / b

age = add(20, 7)
height = subtract(190, 12)
weight = multiply(80, 2)
iq = divide(100, 2)

print "age: %d, height: %d, weight : %d, iq: %d" %(age, height,weight,iq)

print add(age, subtract(height, multiply(weight, divide(iq, 2))))