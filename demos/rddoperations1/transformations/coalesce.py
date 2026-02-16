from pyspark import SparkContext

sc = SparkContext()

numbers = sc.parallelize(range(1 ,100))

numbersWithOnePartition = numbers.coalesce(1)
result = numbersWithOnePartition.collect()

print("result: %s" % result)
