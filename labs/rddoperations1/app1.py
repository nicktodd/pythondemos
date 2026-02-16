from pyspark import SparkContext
sc = SparkContext("local[*]", "RDD Operations Part 1 - Exercise 1")
sc.setLogLevel("WARN")

klmAirports = sc.textFile("klm.txt")
norAirports = sc.textFile("norwegian.txt")

# In each of the following statements, replace "None" with a suitable call to a PySpark API function...
# We've done the first one for you, to get you started...

# Get KLM airports in uppercase.
klmUpperCaseAirports = klmAirports.map(lambda airport: airport.upper()).collect()
print("\nKLM airports in uppercase: %s" % klmUpperCaseAirports)

# Get KLM airports that start with "L" (hint, Python strings have a startswith() method).
klmLAirports = None
print("\nKLM airports that start with 'L': %s" % klmLAirports)

# Get the union of all airports.
allAirports = None
print("\nUnion of all airports: %s" % allAirports)

# Get all distinct airports.
distinctAirports = None
print("\nAll distinct airports: %s" % distinctAirports)

# Get airports in common.
commonAirports = None
print("\nAirports in common: %s" % commonAirports)

# Get airports served by KLM but not Norwegian.
klmOnlyAirports = None
print("\nAirports served by KLM but not Norwegian: %s" % klmOnlyAirports)

sc.stop()

