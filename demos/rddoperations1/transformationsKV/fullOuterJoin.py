from pyspark import SparkContext

sc = SparkContext("local[*]", "FullOuterJoin KV Transformation Demo")

# Two key-value RDDs with country codes as keys and cities as values
pairRdd1 = sc.parallelize( [ ["UK", "London"], ["NO", "Stavanger"], ["SA", "Joburg"] ] )
pairRdd2 = sc.parallelize( [ ["NO", "Bergen"], ["SA", "Durban"],    ["SG", "Singapore"] ] )

# fullOuterJoin() includes all keys from BOTH RDDs
# Where a key exists in only one RDD, the missing side's value is None
# UK (only in rdd1) -> ("London", None), SG (only in rdd2) -> (None, "Singapore")
# NO and SA appear in both, so both values are present
fullOuterJoinRdd = pairRdd1.fullOuterJoin(pairRdd2)
result = fullOuterJoinRdd.collect() 

print("result: %s" % result)

sc.stop()
