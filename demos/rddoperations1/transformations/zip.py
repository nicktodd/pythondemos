from pyspark import SparkContext
sc = SparkContext()

animals = sc.parallelize(["ant", "bat", "cat"])
foods   = sc.parallelize(["apple", "banana", "carrot"])

zippedPairs = foods.zip(animals)
result = zippedPairs.collect()

print("The result is %s" % result)
