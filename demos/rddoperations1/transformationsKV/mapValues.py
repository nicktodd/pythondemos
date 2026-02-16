from pyspark import SparkContext

sc = SparkContext()

rdd = sc.parallelize( [ ["SG", "65"], ["SA", "27"], ["NO", "47"], ["UK", "44"] ] )

formattedRdd = rdd.mapValues(lambda cc: "+(" + cc + ")" )
result = formattedRdd.collect()

print("result: %s" % result)
