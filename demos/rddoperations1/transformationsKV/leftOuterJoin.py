from pyspark import SparkContext

sc = SparkContext()

pairRdd1 = sc.parallelize( [ ["UK", "London"], ["NO", "Stavanger"], ["SA", "Joburg"] ] )
pairRdd2 = sc.parallelize( [ ["NO", "Bergen"], ["SA", "Durban"],    ["SG", "Singapore"] ] )

leftOuterJoinRdd = pairRdd1.leftOuterJoin(pairRdd2)
result = leftOuterJoinRdd.collect() 

print("result: %s" % result)

