from pyspark import SparkContext

sc = SparkContext("local[*]", "Reduce Action Demo")

numbers = sc.parallelize( [1, 2, 3, 1, 1, 2, 3, 1, 2, 1, 2, 2, 3, 4] )

# reduce() aggregates all elements in the RDD using the given function
# The function must be commutative and associative (order of operations may vary)
# Here we sum all elements together by repeatedly applying x + y
reduceResult = numbers.reduce(lambda x, y: x + y)

print("reduceResult: %s" % reduceResult)

sc.stop()


