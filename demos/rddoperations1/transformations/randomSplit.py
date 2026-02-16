from pyspark import SparkContext

sc = SparkContext()

numbers = sc.parallelize(range(1 ,100))
splits = numbers.randomSplit([0.05, 0.15, 0.8])

result0 = splits[0].collect()
result1 = splits[1].collect()
result2 = splits[2].collect()

print("result0: %s" % result0)
print("result1: %s" % result1)
print("result2: %s" % result2)
