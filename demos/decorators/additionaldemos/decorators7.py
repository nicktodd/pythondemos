def singleton(cls):

    def innerFunc(*args, **kwargs):
        
        # Check if a singleton instance has been created yet. If not, create it now...
        if innerFunc.instance is None:
            innerFunc.instance = cls(*args, **kwargs)
        
        # Return the singleton instance.
        return innerFunc.instance

    # innerFunc is a closure, and we can add attributes to it. We use the instance attribute to store the singleton instance.
    # We initialize it to None, which indicates that the singleton instance has not been created yet.
    # Note that we don't use a global variable to store the singleton instance, which keeps the implementation clean and encapsulated.
    innerFunc.instance = None

    return innerFunc


@singleton
class MyConnectionManager:

    # The __init__ method is called only once, when the singleton instance is created. Subsequent attempts to create an instance will return the same instance, and the __init__ method will not be called again.
    # This means that the print statement in the __init__ method will only execute once, even if we try to create multiple instances of MyConnectionManager.
    def __init__(self, authKey):
        print(f"**** MyDatabaseConnectionManager instance created with {authKey} ****")

    def get_connection(self, connStr):
        print(f"Getting connection to {connStr}...")


ref1 = MyConnectionManager("wibble")
ref2 = MyConnectionManager("wibble")
ref3 = MyConnectionManager("wibble")

print(f"id of ref1 is {id(ref1)}")
print(f"id of ref2 is {id(ref2)}")
print(f"id of ref3 is {id(ref3)}")