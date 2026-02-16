from pyspark import SparkContext

sc = SparkContext()

rdd = sc.parallelize( [ ["SG", "65"], ["SA", "27"], ["NO", "47"], ["UK", "44"] ] )

keysRdd = rdd.keys()
result = keysRdd.collect()

print("result: %s" % result)

