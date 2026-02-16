from pyspark import SparkContext

sc = SparkContext()

pairRdd1 = sc.parallelize( [ ["UK", "London"], ["NO", "Stavanger"], ["SA", "Joburg"] ] )
pairRdd2 = sc.parallelize( [ ["NO", "Bergen"], ["SA", "Durban"],    ["SG", "Singapore"] ] )

fullOuterJoinRdd = pairRdd1.fullOuterJoin(pairRdd2)
result = fullOuterJoinRdd.collect() 

print("result: %s" % result)
