from pyspark import SparkContext
sc = SparkContext()

lines = sc.textFile("Macbeth.txt")
words = lines.flatMap(lambda line: line.split(" "))
result = words.collect()

print("The result is %s" % result)

