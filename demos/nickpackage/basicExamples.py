print "hello"
x = 5
if x ==5:
    print x

myList = [];
myList.append(1)
myList.append(2)
myList.append(3)

for x in myList:
    print x

if x==6:
    print 'x is 6'
elif x==7:
    print 'x=7'
else:
    print 'x is not 6 or 7'

for i in xrange(1,10):
    print i
else:
    print 'finished'


def myPrintFunction(toBePrinted) :
    print toBePrinted

myPrintFunction('hello')


class Person:
    name = 'Default Name'

    def sayHello(self):
        print 'hi from ' + self.name


me = Person()
me.sayHello()
