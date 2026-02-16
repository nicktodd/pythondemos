from pyspark import SparkContext

sc = SparkContext("local[*]", "GroupByKey KV Transformation Demo")

pairRdd = sc.parallelize( [ ["UK", "London"], ["UK", "Belfast"], ["No", "Tromso"], ["No", "Oslo"] ] )

groupedRdd = pairRdd.groupByKey()
result = groupedRdd.collect() 

print("result: %s" % result)

sc.stop()
