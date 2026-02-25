from pyspark import SparkContext

sc = SparkContext("local[*]", "Coalesce")

# Create an RDD of numbers 1 to 99. Spark will partition this across
# multiple partitions based on the number of available CPU cores.
numbers = sc.parallelize(range(1 ,100))
print("Partitions before coalesce:", numbers.getNumPartitions())

# coalesce() reduces the number of partitions without a full shuffle.
# It is more efficient than repartition() when reducing partition count.
# Here we merge all partitions down to 1.
numbersWithOnePartition = numbers.coalesce(1)
print("Partitions after coalesce:", numbersWithOnePartition.getNumPartitions())
result = numbersWithOnePartition.collect()

print("result: %s" % result)

sc.stop()
