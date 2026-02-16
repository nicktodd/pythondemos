from pyspark import SparkContext

sc = SparkContext()

pairRdd1 = sc.parallelize( [ ["UK", "London"], ["NO", "Stavanger"], ["SA", "Joburg"] ] )
pairRdd2 = sc.parallelize( [ ["NO", "Bergen"], ["SA", "Durban"],    ["SG", "Singapore"] ] )

rightOuterJoinRdd = pairRdd1.rightOuterJoin(pairRdd2)
result = rightOuterJoinRdd.collect() 

print("result: %s" % result)
