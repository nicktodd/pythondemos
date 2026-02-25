from pyspark import SparkContext

sc = SparkContext()

# Two key-value RDDs with country codes as keys and cities as values
pairRdd1 = sc.parallelize( [ ["UK", "London"], ["NO", "Stavanger"], ["SA", "Joburg"] ] )
pairRdd2 = sc.parallelize( [ ["NO", "Bergen"], ["SA", "Durban"],    ["SG", "Singapore"] ] )

# leftOuterJoin() keeps ALL keys from the LEFT RDD (pairRdd1)
# For keys in pairRdd1 not found in pairRdd2 (UK), the right value is None
# Keys only in pairRdd2 (SG) are excluded entirely
leftOuterJoinRdd = pairRdd1.leftOuterJoin(pairRdd2)
result = leftOuterJoinRdd.collect() 

print("result: %s" % result)

