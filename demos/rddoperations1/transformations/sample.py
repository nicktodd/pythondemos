from pyspark import SparkContext

sc = SparkContext()

numbers = sc.parallelize(range(1 ,100))

# sample() returns a random subset of the RDD
# First argument (True): sample with replacement (an element can be selected more than once)
# Second argument (0.05): approximate fraction of elements to include (~5%)
sampleNumbers = numbers.sample(True, 0.05)
result = sampleNumbers.collect()

print("result: %s" % result)

