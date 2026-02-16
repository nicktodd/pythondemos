class Person:
    def __init__(self, str, sep):
        fields = str.split(sep)
        self.name = fields[0]
        self.age = int(fields[1])
        self.gender = fields[2]
        self.zipcode = fields[3]

    def __repr__(self):
        return "%s | %d | %s | %s" % (self.name, self.age, self.gender, self.zipcode)
