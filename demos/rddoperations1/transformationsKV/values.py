from pyspark import SparkContext

sc = SparkContext()

# Key-value RDD with country codes as keys and international dialing codes as values
rdd = sc.parallelize( [ ["SG", "65"], ["SA", "27"], ["NO", "47"], ["UK", "44"] ] )

# values() extracts only the values from a key-value RDD, discarding the keys
# Result: ["65", "27", "47", "44"]
keysRdd = rdd.values()
result = keysRdd.collect()

print("result: %s" % result)

