from pyspark import SparkContext

sc = SparkContext("local[*]", "Lookup Action Demo")

kvRdd = sc.parallelize( [ ["UK","London"], ["FR","Paris"], ["UK","Leeds"], ["SA","Joburg"] ] )

lookupResult = kvRdd.lookup("UK")

print("lookupResult: %s" % lookupResult)

sc.stop()


