from pyspark import SparkContext
from person import Person

sc = SparkContext()
lines = sc.textFile("persons.txt")

persons = lines.map(lambda line: Person(line, ","))
sortedByAge = persons.sortBy(lambda person: person.age)
result = sortedByAge.collect()

print("The result is %s" % result)
