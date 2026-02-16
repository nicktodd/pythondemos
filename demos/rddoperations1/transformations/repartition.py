from pyspark import SparkContext

sc = SparkContext()

numbers = sc.parallelize(range(1 ,100))

numbersWithFourPartitions = numbers.repartition(4)
result = numbersWithFourPartitions.collect()

print("result: %s" % result)


