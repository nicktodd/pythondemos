from pyspark import SparkContext

sc = SparkContext()

# Key-value RDD with country codes as keys and international dialing codes as values
rdd = sc.parallelize( [ ["SG", "65"], ["SA", "27"], ["NO", "47"], ["UK", "44"] ] )

# mapValues() applies a function only to the values, leaving the keys unchanged
# Here each dialing code is reformatted as +(code), e.g. "65" becomes "+(65)"
formattedRdd = rdd.mapValues(lambda cc: "+(" + cc + ")" )
result = formattedRdd.collect()

print("result: %s" % result)
