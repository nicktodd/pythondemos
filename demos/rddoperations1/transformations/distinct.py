from pyspark import SparkContext
sc = SparkContext()

lines3 = sc.textFile("file3.txt")
distinctLines = lines3.distinct()
result = distinctLines.collect()

print("The result is %s" % result)
