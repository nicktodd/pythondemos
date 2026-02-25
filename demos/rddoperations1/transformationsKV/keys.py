from pyspark import SparkContext

sc = SparkContext()

# Key-value RDD with country codes as keys and international dialing codes as values
rdd = sc.parallelize( [ ["SG", "65"], ["SA", "27"], ["NO", "47"], ["UK", "44"] ] )

# keys() extracts only the keys from a key-value RDD, discarding the values
# Result: ["SG", "SA", "NO", "UK"]
keysRdd = rdd.keys()
result = keysRdd.collect()

print("result: %s" % result)

