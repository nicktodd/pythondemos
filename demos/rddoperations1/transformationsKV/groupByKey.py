from pyspark import SparkContext

sc = SparkContext("local[*]", "GroupByKey KV Transformation Demo")

# Key-value RDD with country codes as keys and cities as values
# Note there are multiple cities per country
pairRdd = sc.parallelize( [ ["UK", "London"], ["UK", "Belfast"], ["No", "Tromso"], ["No", "Oslo"] ] )

# groupByKey() groups all values with the same key into an iterable
# Result: [("UK", <iterable: ["London", "Belfast"]>), ("No", <iterable: ["Tromso", "Oslo"]>)]
groupedRdd = pairRdd.groupByKey()
result = groupedRdd.collect() 

print("result: %s" % result)

sc.stop()
