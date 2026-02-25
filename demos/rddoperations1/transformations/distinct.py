from pyspark import SparkContext
sc = SparkContext("local[*]", "Distinct")

# Read all lines from file3.txt into an RDD (may contain duplicates)
lines3 = sc.textFile("file3.txt")
# distinct() removes duplicate elements and returns each unique element once
distinctLines = lines3.distinct()
result = distinctLines.collect()

print("The result is %s" % result)

sc.stop()
