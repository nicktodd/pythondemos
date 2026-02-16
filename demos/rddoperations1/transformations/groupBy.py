from pyspark import SparkContext
from person import Person

sc = SparkContext()
lines = sc.textFile("persons.txt")

persons = lines.map(lambda line: Person(line, ","))
groupByZipcode = persons.groupBy(lambda person: person.zipcode)
result = groupByZipcode.collect()

print("The result is %s" % result)

