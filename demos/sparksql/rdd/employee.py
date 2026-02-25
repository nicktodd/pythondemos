class Employee:
    def __init__(self, id, name, age, salary):
        self.id = id
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return "%s | %d | %s | %s" % (self.id, self.name, self.age, self.salary)
