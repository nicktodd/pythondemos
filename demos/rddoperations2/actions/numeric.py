from pyspark import SparkContext

sc = SparkContext()

numbers = sc.parallelize([1, 2, 3, 5])

sum      = numbers.sum()
mean     = numbers.mean()
stdev    = numbers.stdev()
variance = numbers.variance()

print("sum %f, mean %f, stdev %f, variance %f" % (sum, mean, stdev, variance))

