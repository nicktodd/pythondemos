from pyspark import SparkContext

sc = SparkContext()

# Two key-value RDDs with country codes as keys and cities as values
pairRdd1 = sc.parallelize( [ ["UK", "London"], ["NO", "Stavanger"], ["SA", "Joburg"] ] )
pairRdd2 = sc.parallelize( [ ["NO", "Bergen"], ["SA", "Durban"],    ["SG", "Singapore"] ] )

# subtractByKey() removes all pairs from pairRdd1 whose key also appears in pairRdd2
# NO and SA appear in both RDDs, so only UK (only in pairRdd1) remains
subtractRdd = pairRdd1.subtractByKey(pairRdd2)
result = subtractRdd.collect()

print("result: %s" % result)
