from pyspark import SparkContext

sc = SparkContext("local[*]", "First Min Max Action Demo")

numbers = sc.parallelize( [1, 2, 3, 1, 1, 2, 3, 1, 2, 1, 2, 2, 3, 4] )

first = numbers.first()
min   = numbers.min()
max   = numbers.max()

print("first: %d, min: %d, max: %d" % (first, min, max))

sc.stop()

