from datetime import datetime

#---Start of decorator---------------------------------------------------
def timer(func) :

    # Define an inner function, wraps the decorated func.
    def innerFunc() :
        t1 = datetime.now()    
        func()
        t2 = datetime.now()
        print(t2 - t1)
   
    # Return the inner function.
    return innerFunc

#---End of decorator-----------------------------------------------------


# Some function, which we now decorate explicitly.
@timer
def myfunc1() :
    t1
    print("Hi from myfunc1()")
    t2 
  
  
#---Client code----------------------------------------------------------

print("###No need to manually wrap myfunc1 now, just invoke it directly...")
myfunc1()