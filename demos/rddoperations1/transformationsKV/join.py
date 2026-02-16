from pyspark import SparkContext

sc = SparkContext("local[*]", "Join KV Transformation Demo")

pairRdd1 = sc.parallelize( [ ["UK", "London"], ["NO", "Stavanger"], ["SA", "Joburg"] ] )
pairRdd2 = sc.parallelize( [ ["NO", "Bergen"], ["SA", "Durban"],    ["SG", "Singapore"] ] )

joinRdd = pairRdd1.join(pairRdd2)
result = joinRdd.collect() 

print("result: %s" % result)

sc.stop()
