from pyspark import SparkContext
sc = SparkContext()

animals = sc.parallelize(["ant", "bat", "cat"])
# zipWithIndex() pairs each element with its zero-based position index
# Result: [("ant", 0), ("bat", 1), ("cat", 2)]
animalsWithIndex = animals.zipWithIndex()
result = animalsWithIndex.collect()

print("The result is %s" % result)
