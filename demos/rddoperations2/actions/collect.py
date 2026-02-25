from pyspark import SparkContext

sc = SparkContext("local[*]", "Collect Action Demo")

numbers = sc.parallelize( [1, 2, 3, 1, 1, 2, 3, 1, 2, 1, 2, 2, 3, 4] )

# collect() is an action that retrieves ALL elements from the RDD to the driver program as a list
# Use with care on large datasets - all data must fit in driver memory
collectResult = numbers.collect()

print("collectResult: %s" % collectResult)

sc.stop()

