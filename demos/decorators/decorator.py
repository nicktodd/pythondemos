# defining a decorator
def hello_decorator(function_to_be_decorated):
 
    def decorating_function():
        # here is some decoration!
        print("Here is some prefunction decoration!")
        function_to_be_decorated()
        # some more decoration
        print("Here is some post function decoration!")
    return decorating_function
 
 
# defining a function, to be called inside wrapper
@hello_decorator
def function_to_be_decorated():
    print("This is inside the function that is going to be decorated!!")
 
 
# passing 'function_to_be_decorated' inside the
# decorator to control its behaviour
#function_to_be_decorated = hello_decorator(function_to_be_decorated)
 
print(function_to_be_decorated())
 
