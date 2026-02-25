from pyspark import SparkContext
sc = SparkContext()

# Create two RDDs - both must have the same number of elements and partitions
animals = sc.parallelize(["ant", "bat", "cat"])
foods   = sc.parallelize(["apple", "banana", "carrot"])

# zip() pairs elements from two RDDs by position, creating a key-value RDD
# Result: [("apple", "ant"), ("banana", "bat"), ("carrot", "cat")]
zippedPairs = foods.zip(animals)
result = zippedPairs.collect()

print("The result is %s" % result)
