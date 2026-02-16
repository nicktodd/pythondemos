from pyspark import SparkContext
sc = SparkContext()

animals = sc.parallelize(["ant", "bat", "cat"])
animalsWithIndex = animals.zipWithIndex()
result = animalsWithIndex.collect()

print("The result is %s" % result)
