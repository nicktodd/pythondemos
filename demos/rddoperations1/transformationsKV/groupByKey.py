from pyspark import SparkContext

sc = SparkContext()

pairRdd = sc.parallelize( [ ["UK", "London"], ["UK", "Belfast"], ["No", "Tromso"], ["No", "Oslo"] ] )

groupedRdd = pairRdd.groupByKey()
result = groupedRdd.collect() 

print("result: %s" % result)
