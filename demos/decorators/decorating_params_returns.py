# defining a decorator
def string_uppercase_decorator(function_to_be_decorated):
    def decorating_function(*args, **kwargs):
        # here is some decoration!
        print("Upper case!")
        return_value = function_to_be_decorated(*args, **kwargs)
        # some more decoration
        print("Upper case complete!")
        return return_value
    return decorating_function
 
 
# defining a function, to be called inside wrapper
@string_uppercase_decorator # this does the decoration for us
def function_to_be_decorated(some_text):
    print("This is inside the function that is going to be decorated!!")
    return some_text
 
 
 
# calling the function
function_to_be_decorated("hello")
