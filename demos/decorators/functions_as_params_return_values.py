# This example is the same as functions_as_params but with return values

def shout(text):
    return text.upper()
 
print(shout('Hello'))
 
# assign another variable to the function
yell = shout

# now use the new variable
print(yell('Hello'))


# this function takes in a function as a paramter to invoke
def function_caller(func_to_call, message):
    result = func_to_call(message)
    return result


# pass a function as a parameter
print(function_caller(yell, "hello world"))

