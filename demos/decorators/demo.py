def say_hello():
    return "hello world"

# takes in a function and runs it!
def run_whatever(some_function):
    return some_function()

print(run_whatever(say_hello))
