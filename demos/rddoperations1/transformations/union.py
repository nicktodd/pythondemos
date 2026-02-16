from pyspark import SparkContext
sc = SparkContext()

lines1 = sc.textFile("file1.txt")
lines2 = sc.textFile("file2.txt")
unionLines = lines1.union(lines2)
result = unionLines.collect()

print("The result is %s" % result)
