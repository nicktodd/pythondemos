from pyspark import SparkContext

sc = SparkContext("local[*]", "Count Action Demo")

numbers = sc.parallelize( [1, 2, 3, 1, 1, 2, 3, 1, 2, 1, 2, 2, 3, 4])

count = numbers.count()

print("count: %d" % count)

sc.stop()
