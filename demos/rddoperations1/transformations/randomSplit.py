from pyspark import SparkContext

sc = SparkContext()

# Create an RDD of numbers 1 to 99
numbers = sc.parallelize(range(1 ,100))
# randomSplit() splits the RDD into multiple RDDs using the provided weights
# Weights [0.05, 0.15, 0.8] roughly correspond to ~5%, ~15%, and ~80% of the elements
# The actual split sizes are approximate due to random sampling
splits = numbers.randomSplit([0.05, 0.15, 0.8])

result0 = splits[0].collect()
result1 = splits[1].collect()
result2 = splits[2].collect()

print("result0: %s" % result0)
print("result1: %s" % result1)
print("result2: %s" % result2)
