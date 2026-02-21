#---Start of decorator---------------------------------------------------
def simpleDecorator(func) :

    # Define an inner function, which wraps (decorates) the target function.
    def innerFunc() :
        print("Start of simpleDecorator()")    
        func()
        print("End of simpleDecorator()")
   
    # Return the inner function.
    return innerFunc

#---End of decorator-----------------------------------------------------


# Some function that we want to decorate.
def myfunc1() :
    print("Hi from myfunc1()")
    
  
#---Client code----------------------------------------------------------

print("###Manually wrap myfunc1 with simpleDecorator...")
pointerToInnerFunc = simpleDecorator(myfunc1)  

print("###Invoke wrapped myfunc1...")
pointerToInnerFunc()
