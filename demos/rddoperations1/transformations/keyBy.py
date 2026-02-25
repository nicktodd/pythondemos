from pyspark import SparkContext
from person import Person

sc = SparkContext()
# Read person records from a CSV file
lines = sc.textFile("persons.txt")

# Map each CSV line to a Person object
persons = lines.map(lambda line: Person(line, ","))
# keyBy() creates a key-value RDD using the result of the function as the key
# Each Person becomes a (zipcode, Person) pair
keyByZipcode = persons.keyBy(lambda person: person.zipcode)
result = keyByZipcode.collect()

print("The result is %s" % result)
