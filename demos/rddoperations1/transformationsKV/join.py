from pyspark import SparkContext

sc = SparkContext("local[*]", "Join KV Transformation Demo")

# Two key-value RDDs with country codes as keys and cities as values
pairRdd1 = sc.parallelize( [ ["UK", "London"], ["NO", "Stavanger"], ["SA", "Joburg"] ] )
pairRdd2 = sc.parallelize( [ ["NO", "Bergen"], ["SA", "Durban"],    ["SG", "Singapore"] ] )

# join() is an inner join - only includes keys that exist in BOTH RDDs
# UK (only in rdd1) and SG (only in rdd2) are excluded from the result
joinRdd = pairRdd1.join(pairRdd2)
result = joinRdd.collect() 

print("result: %s" % result)

sc.stop()
