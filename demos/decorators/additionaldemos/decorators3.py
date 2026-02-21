#---Start of decorator---------------------------------------------------
def parameterAwareDecorator(func) :

    # Define an inner function, wraps the decorated func.
    def innerFunc(*args, **kwargs) :
        print("Start of parameterAwareDecorator()")    
        func(*args, **kwargs)
        print("End of parameterAwareDecorator()")
   
    # Return the inner function.
    return innerFunc

#---End of decorator-----------------------------------------------------


# Some function that receives parameters.
@parameterAwareDecorator
def myfunc1(firstName, lastName, nationality) :
    print("Hi %s %s, your nationality is %s" % (firstName, lastName, nationality))
  
  
  
#---Client code----------------------------------------------------------

print("###Invoke myfunc1() and pass positional parameters")
myfunc1("Ola", "Nordmann", "Norsk")

print("###Invoke myfunc1() and pass keyword parameters")
myfunc1(nationality="Cymraeg", lastName="Olsen", firstName="Jayne")