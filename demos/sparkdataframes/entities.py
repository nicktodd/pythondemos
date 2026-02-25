class Customer:
    def __init__(self, cId, name, age, gender):
        self.cId = cId
        self.name = name
        self.age = age
        self.gender = gender

    def __repr__(self):
        return "%d | %s | %d | %s" % (self.cId, self.name, self.age, self.gender)


class Product:
    def __init__(self, pId, name, price):
        self.pId = pId
        self.name = name
        self.price = price

    def __repr__(self):
        return "%d | %s | %f" % (self.pId, self.name, self.price)

        
class Home:
    def __init__(self, city, size, bedrooms, price):
        self.city = city
        self.size = size
        self.bedrooms = bedrooms
        self.price = price

    def __repr__(self):
        return "%s | %d | %d | %f" % (self.city, self.size, self.bedrooms, self.price)

        
class SalesByCity:
    def __init__(self, year, city, country, revenue):
        self.year = year
        self.city = city
        self.country = country
        self.revenue = revenue

    def __repr__(self):
        return "%d | %s | %s | %f" % (self.year, self.city, self.country, self.revenue)

        
class Email:
    def __init__(self, sender, recipient, subject, body):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body

    def __repr__(self):
        return "%s | %s | %s | %s" % (self.sender, self.recipient, self.subject, self.body)

        
class Transaction:
    def __init__(self, tId, custId, prodId, date, city):
        self.tId = tId
        self.custId = custId
        self.prodId = prodId
        self.date = date
        self.city = city

    def __repr__(self):
        return "%d | %d | %d | %s | %s" % (self.tId, self.custId, self.prodId, self.date, self.city)
