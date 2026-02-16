# Exercise 1: Functions as First-Class Citizens

def apply_operation(func, x, y):
    return func(x, y)

def create_multiplier(factor):
    return lambda x: x * factor

# Create a list of functions and apply them to a value
funcs = [lambda x: x**2, lambda x: x*2, lambda x: x+10]
results = [f(3) for f in funcs]
print("List of functions results:", results)  # Should print [9, 6, 13]

# Store functions in a dictionary and call them by key
func_dict = {
    'square': lambda x: x**2,
    'double': lambda x: x*2,
    'add_ten': lambda x: x+10
}
print("Dictionary function 'square':", func_dict['square'](5))  # Should print 25

# Test code
result = apply_operation(lambda x, y: x + y, 3, 4)
print("apply_operation result:", result)  # Should print 7

double = create_multiplier(2)
print("create_multiplier result:", double(5))  # Should print 10
