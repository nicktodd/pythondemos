from pyspark import SparkContext
sc = SparkContext("local[*]", "Cartesian")

# Create two RDDs - one with animals and one with foods
animals = sc.parallelize(["ant", "bat", "cat"])
foods   = sc.parallelize(["apple", "banana", "carrot"])

# cartesian() produces every possible combination of elements from both RDDs
# Result will be: [("apple", "ant"), ("apple", "bat"), ..., ("carrot", "cat")]
cartesianProduct = foods.cartesian(animals)
result = cartesianProduct.collect()

print("The result is %s" % result)

sc.stop()

