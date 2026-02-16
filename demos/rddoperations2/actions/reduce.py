from pyspark import SparkContext

sc = SparkContext()

numbers = sc.parallelize( [1, 2, 3, 1, 1, 2, 3, 1, 2, 1, 2, 2, 3, 4] )

reduceResult = numbers.reduce(lambda x, y: x + y)

print("reduceResult: %s" % reduceResult)


