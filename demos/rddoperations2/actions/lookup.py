from pyspark import SparkContext

sc = SparkContext("local[*]", "Lookup Action Demo")

# Key-value RDD with country codes as keys and cities as values
# Note UK has two associated cities
kvRdd = sc.parallelize( [ ["UK","London"], ["FR","Paris"], ["UK","Leeds"], ["SA","Joburg"] ] )

# lookup() returns a list of all values associated with the given key
# Here it returns all cities for "UK": ["London", "Leeds"]
lookupResult = kvRdd.lookup("UK")

print("lookupResult: %s" % lookupResult)

sc.stop()


