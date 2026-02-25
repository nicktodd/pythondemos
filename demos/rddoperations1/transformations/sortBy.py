from pyspark import SparkContext
from person import Person

sc = SparkContext()
# Read person records from a CSV file
lines = sc.textFile("persons.txt")

# Map each CSV line to a Person object
persons = lines.map(lambda line: Person(line, ","))
# sortBy() sorts the RDD elements using the given key function
# By default sorts in ascending order; pass ascending=False for descending
sortedByAge = persons.sortBy(lambda person: person.age)
result = sortedByAge.collect()

print("The result is %s" % result)
