from pyspark import SparkContext

sc = SparkContext()

pairRdd1 = sc.parallelize( [ ["UK", "London"], ["NO", "Stavanger"], ["SA", "Joburg"] ] )
pairRdd2 = sc.parallelize( [ ["NO", "Bergen"], ["SA", "Durban"],    ["SG", "Singapore"] ] )

subtractRdd = pairRdd1.subtractByKey(pairRdd2)
result = subtractRdd.collect()

print("result: %s" % result)
