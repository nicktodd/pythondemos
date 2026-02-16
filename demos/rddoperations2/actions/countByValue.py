from pyspark import SparkContext

sc = SparkContext()

numbers = sc.parallelize( [1, 2, 3, 1, 1, 2, 3, 1, 2, 1, 2, 2, 3, 4])

countByValueResult = numbers.countByValue()

print("countByValueResult: %s" % countByValueResult)


