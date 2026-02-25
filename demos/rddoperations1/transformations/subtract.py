from pyspark import SparkContext
sc = SparkContext()

# Read two text files into separate RDDs
lines1 = sc.textFile("file1.txt")
lines2 = sc.textFile("file2.txt")
# subtract() returns elements that are in lines1 but NOT in lines2
# This is equivalent to a set difference: lines1 - lines2
unionLines = lines1.subtract(lines2)
result = unionLines.collect()

print("The result is %s" % result)
