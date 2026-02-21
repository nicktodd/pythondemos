#---Start of decorator---------------------------------------------------
def parameterizedDecorator(prefix, suffix) :

    # Define "outer" inner function, which just wraps a function.
    def innerFunc1(func) :
    
        # Define "inner" inner function, which decorates/calls target function.
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


# Some function, which we now decorate explicitly.
@parameterizedDecorator("HELLO", "GOODBYE")
def myfunc1(firstName, lastName, nationality) :
    return "Hi %s %s, your nationality is %s" % (firstName, lastName, nationality)
  
  
  
#---Client code, just calls myfunc1 directly now-------------------------

res1 = myfunc1("Kari", "Nordmann", "Norsk")
print(res1)

res2 = myfunc1(nationality="Cymraeg", lastName="Olsen", firstName="Andy")
print(res2)