from pyspark import SparkContext

sc = SparkContext()

numbers = sc.parallelize(range(1 ,100))

# repartition() redistributes the data into the specified number of partitions
# Unlike coalesce(), it can both increase AND decrease partition count
# It performs a full shuffle of the data across the cluster
numbersWithFourPartitions = numbers.repartition(4)
result = numbersWithFourPartitions.collect()

print("result: %s" % result)


