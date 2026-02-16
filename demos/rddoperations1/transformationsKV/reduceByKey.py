from pyspark import SparkContext

sc = SparkContext()

perksRdd = sc.parallelize( [ ["Joe", 1000], ["Sam", 100], ["Joe", 2000], ["Sam", 200] ] )

sumRdd = perksRdd.reduceByKey(lambda x, y:  x + y)
result = sumRdd.collect()

print("result: %s" % result)
 
