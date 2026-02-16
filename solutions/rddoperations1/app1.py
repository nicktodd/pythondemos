from pyspark import SparkContext
sc = SparkContext()
sc.setLogLevel("WARN")

klmAirports = sc.textFile("klm.txt")
norAirports = sc.textFile("norwegian.txt")

# Get KLM airports in uppercase.
klmUpperCaseAirports = klmAirports.map(lambda airport: airport.upper()).collect()
print("\nKLM airports in uppercase: %s" % klmUpperCaseAirports)

# Get KLM airports that start with "L".
klmLAirports = klmAirports.filter(lambda airport: airport.startswith("L")).collect()
print("\nKLM airports that start with 'L': %s" % klmLAirports)

# Get the union of all airports.
allAirports = klmAirports.union(norAirports).collect()
print("\nUnion of all airports: %s" % allAirports)

# Get all distinct airports.
distinctAirports = klmAirports.union(norAirports).distinct().collect()
print("\nAll distinct airports: %s" % distinctAirports)

# Get airports in common.
commonAirports = klmAirports.intersection(norAirports).collect()
print("\nAirports in common: %s" % commonAirports)

# Get airports served by KLM but not Norwegian.
klmOnlyAirports = klmAirports.subtract(norAirports).collect()
print("\nAirports served by KLM but not Norwegian: %s" % klmOnlyAirports)

