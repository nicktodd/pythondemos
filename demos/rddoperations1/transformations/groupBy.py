from pyspark import SparkContext
from person import Person

sc = SparkContext()
# Read person records from a CSV file
lines = sc.textFile("persons.txt")

# Map each CSV line to a Person object
persons = lines.map(lambda line: Person(line, ","))
# groupBy() groups elements by the result of the key function
# Returns an RDD of (key, iterable) pairs - here each zipcode maps to its group of people
groupByZipcode = persons.groupBy(lambda person: person.zipcode)
result = groupByZipcode.collect()

print("The result is %s" % result)

