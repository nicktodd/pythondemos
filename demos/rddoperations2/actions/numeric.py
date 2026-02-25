from pyspark import SparkContext

sc = SparkContext("local[*]", "Numeric Action Demo")

numbers = sc.parallelize([1, 2, 3, 5])

# Numeric actions compute statistical summaries on an RDD of numbers
sum      = numbers.sum()       # Total of all elements
mean     = numbers.mean()      # Average (arithmetic mean)
stdev    = numbers.stdev()     # Population standard deviation
variance = numbers.variance()  # Population variance

print("sum %f, mean %f, stdev %f, variance %f" % (sum, mean, stdev, variance))

sc.stop()

