class Element:
    def __init__(self, str):
        arr = str.split("\t") 
        self.atomicNumber = int(arr[0])
        self.atomicMass = float(arr[1])
        self.group = int(arr[2])
        self.period = int(arr[3])
        self.symbol = arr[4]
        self.name = arr[5]

    def __repr__(self):
        return "%d | %f | %d | %d | %s | %s" % (self.atomicNumber, self.atomicMass, self.group, self.period, self.symbol, self.name)
