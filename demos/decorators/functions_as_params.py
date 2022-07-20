def shout(text):
    print(text.upper())
 
shout('Hello')
 
# assign another variable to the function
yell = shout

# now use the new variable
yell('Hello')


# this function takes in a function as a paramter to invoke
def function_caller(func_to_call, message):
    func_to_call(message)


# pass a function as a parameter
function_caller(yell, "hello world")

