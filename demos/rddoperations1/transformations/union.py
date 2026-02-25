from pyspark import SparkContext
sc = SparkContext()

# Read two text files into separate RDDs
lines1 = sc.textFile("file1.txt")
lines2 = sc.textFile("file2.txt")
# union() combines both RDDs into a single RDD
# Unlike intersection(), all elements from both RDDs are kept, including duplicates
unionLines = lines1.union(lines2)
result = unionLines.collect()

print("The result is %s" % result)
