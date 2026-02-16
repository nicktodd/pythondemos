from pyspark import SparkContext

sc = SparkContext()

pairRdd1 = sc.parallelize( [ ["UK", "London"], ["NO", "Stavanger"], ["SA", "Joburg"] ] )
pairRdd2 = sc.parallelize( [ ["NO", "Bergen"], ["SA", "Durban"],    ["SG", "Singapore"] ] )

joinRdd = pairRdd1.join(pairRdd2)
result = joinRdd.collect() 

print("result: %s" % result)
