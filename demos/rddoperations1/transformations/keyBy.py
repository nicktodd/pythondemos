from pyspark import SparkContext
from person import Person

sc = SparkContext()
lines = sc.textFile("persons.txt")

persons = lines.map(lambda line: Person(line, ","))
keyByZipcode = persons.keyBy(lambda person: person.zipcode)
result = keyByZipcode.collect()

print("The result is %s" % result)
