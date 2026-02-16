from pyspark import SparkContext

sc = SparkContext()

kvRdd = sc.parallelize( [ ["UK","London"], ["FR","Paris"], ["UK","Leeds"], ["SA","Joburg"] ] )

lookupResult = kvRdd.lookup("UK")

print("lookupResult: %s" % lookupResult)


