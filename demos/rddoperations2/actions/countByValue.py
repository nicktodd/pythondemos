from pyspark import SparkContext

sc = SparkContext("local[*]", "CountByValue Action Demo")

numbers = sc.parallelize( [1, 2, 3, 1, 1, 2, 3, 1, 2, 1, 2, 2, 3, 4])

# countByValue() returns a dictionary with the occurrence count of each distinct value
# Result: {1: 5, 2: 5, 3: 3, 4: 1}
countByValueResult = numbers.countByValue()

print("countByValueResult: %s" % countByValueResult)

sc.stop()


