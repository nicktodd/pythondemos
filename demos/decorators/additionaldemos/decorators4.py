#---Start of decorator---------------------------------------------------
def returnAwareDecorator(func) :

    # Define an inner function, wraps the decorated func.
    def innerFunc(*args, **kwargs) :
        print("Start of returnAwareDecorator()")    
        returnValueFromFunc = func(*args, **kwargs)
        print("End of returnAwareDecorator()")
        return returnValueFromFunc
        
    # Return the inner function.
    return innerFunc

#---End of decorator-----------------------------------------------------


# Some function that returns a result.
@returnAwareDecorator
def myfunc1(firstName, lastName, nationality) :
    return "Hi %s %s, your nationality is %s" % (firstName, lastName, nationality)
  
  
  
#---Client code----------------------------------------------------------

print("###Invoke myfunc1() and pass positional parameters, and get the result")
res1 = myfunc1("Kari", "Nordmann", "Norsk")
print(res1)

print("###Invoke myfunc1() and pass keyword parameters, and get the result")
res2 = myfunc1(nationality="Cymraeg", lastName="Olsen", firstName="Andy")
print(res2)