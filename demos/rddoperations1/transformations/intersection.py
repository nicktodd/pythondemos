from pyspark import SparkContext
sc = SparkContext()

# Read two text files into separate RDDs
lines1 = sc.textFile("file1.txt")
lines2 = sc.textFile("file2.txt")
# intersection() returns only the elements that appear in BOTH RDDs
# Elements unique to either RDD are excluded
unionLines = lines1.intersection(lines2)
result = unionLines.collect()

print("The result is %s" % result)
