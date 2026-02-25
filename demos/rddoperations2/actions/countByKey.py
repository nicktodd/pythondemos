from pyspark import SparkContext

sc = SparkContext("local[*]", "CountByKey Action Demo")

# Key-value RDD with country codes as keys and cities as values
# Note UK appears twice
kvRdd = sc.parallelize( [ ["UK","London"], ["FR","Paris"], ["UK","Leeds"], ["SA","Joburg"] ] )

# countByKey() returns a dictionary with the count of values per key
# Result: {"UK": 2, "FR": 1, "SA": 1}
countByKeyResult = kvRdd.countByKey()

print("countByKeyResult: %s" % countByKeyResult)

sc.stop()


