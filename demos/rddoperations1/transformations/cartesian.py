from pyspark import SparkContext
sc = SparkContext("local[*]", "Cartesian")

animals = sc.parallelize(["ant", "bat", "cat"])
foods   = sc.parallelize(["apple", "banana", "carrot"])

cartesianProduct = foods.cartesian(animals)
result = cartesianProduct.collect()

print("The result is %s" % result)

sc.stop()

