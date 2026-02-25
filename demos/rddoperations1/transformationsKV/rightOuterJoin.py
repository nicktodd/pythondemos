from pyspark import SparkContext

sc = SparkContext()

# Two key-value RDDs with country codes as keys and cities as values
pairRdd1 = sc.parallelize( [ ["UK", "London"], ["NO", "Stavanger"], ["SA", "Joburg"] ] )
pairRdd2 = sc.parallelize( [ ["NO", "Bergen"], ["SA", "Durban"],    ["SG", "Singapore"] ] )

# rightOuterJoin() keeps ALL keys from the RIGHT RDD (pairRdd2)
# For keys in pairRdd2 not found in pairRdd1 (SG), the left value is None
# Keys only in pairRdd1 (UK) are excluded entirely
rightOuterJoinRdd = pairRdd1.rightOuterJoin(pairRdd2)
result = rightOuterJoinRdd.collect() 

print("result: %s" % result)
