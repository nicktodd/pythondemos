# defining a decorator
def string_uppercase_decorator(function_to_be_decorated):
    def decorating_function(string_param):
        # here is some decoration!
        #print("Upper case!")
        return_value = function_to_be_decorated(string_param.upper())
        # some more decoration
        #print("Upper case complete!")
        return return_value
    return decorating_function

def string_lower_case_decorator(function_to_be_decorated):
    def decorating_function(string_param):
        # here is some decoration!
        #print("Lower case!")
        return_value = function_to_be_decorated(string_param.lower())
        # some more decoration
        #print("Lower case complete!")
        return return_value
    return decorating_function

# defining a decorator
def string_add_stars_decorator(function_to_be_decorated):
    def decorating_function(string_param):
        # here is some decoration!
        #print("Stars!")
        return_value = function_to_be_decorated("******" + string_param + "*****")
        # some more decoration
        #print("Stars done!")
        return return_value
    return decorating_function

# defining a function, to be called inside wrapper
@string_lower_case_decorator
@string_uppercase_decorator
# this does the decoration for us
@string_add_stars_decorator
def function_to_be_decorated(some_text):
    return some_text
 
# calling the function
print(function_to_be_decorated("hello"))
