from pyspark import SparkContext

sc = SparkContext()

numbers = sc.parallelize(range(1 ,100))

sampleNumbers = numbers.sample(True, 0.05)
result = sampleNumbers.collect()

print("result: %s" % result)

