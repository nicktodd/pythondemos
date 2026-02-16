from pyspark import SparkContext
sc = SparkContext()

lines = sc.textFile("Macbeth.txt")
longLines = lines.filter(lambda line: len(line) > 50)
result = longLines.collect()

print("The result is %s" % result)
