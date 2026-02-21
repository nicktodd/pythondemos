#---Start of decorator---------------------------------------------------
def parameterizedDecorator(prefix, suffix) :

    # Define an "outer" inner function, which just wraps a function.
    def innerFunc1(func) :
    
        # Define an "inner" inner function, which invokes the wrapped function in a decorated kinda way.
        def innerFunc2(*args, **kwargs) :
            print(prefix)    
            returnValueFromFunc = func(*args, **kwargs)
            print(suffix)
            return returnValueFromFunc
            
        # Return innerFunc2, i.e. the "inner" inner function.    
        return innerFunc2
        
    # Return innerFunc1, i.e. the "outer" inner function.
    return innerFunc1

#---End of decorator-----------------------------------------------------


# Some other function, which we don't decorate explicitly here.
def myfunc1(firstName, lastName, nationality) :
    return "Hi %s %s, your nationality is %s" % (firstName, lastName, nationality)
  
  
  
#---Client code----------------------------------------------------------

print("###Call the decorator function with parameters. This returns a pointer to innerFunc1.")
pointerToInnerFunc1 = parameterizedDecorator("HELLO", "GOODBYE")

print("###Call innerFunc1 and tell it to wrap myfunc1. This returns a pointer to innerFunc2.")
pointerToInnerFunc2 = pointerToInnerFunc1(myfunc1)

print("###Call innerFunc2 with actual parameters. This will call myfunc1 with these parameters.")
res = pointerToInnerFunc2("Per", "Nordmann", "Norsk")
print(res)


  


