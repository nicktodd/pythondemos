from pyspark import SparkContext

sc = SparkContext("local[*]", "First Min Max Action Demo")

numbers = sc.parallelize( [1, 2, 3, 1, 1, 2, 3, 1, 2, 1, 2, 2, 3, 4] )

# first() returns the first element in the RDD
first = numbers.first()
# min() returns the smallest element in the RDD
min   = numbers.min()
# max() returns the largest element in the RDD
max   = numbers.max()

print("first: %d, min: %d, max: %d" % (first, min, max))

sc.stop()

