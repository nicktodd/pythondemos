from pyspark import SparkContext
sc = SparkContext()

lines = sc.textFile("Macbeth.txt")
lengths = lines.map(lambda line: len(line))
result = lengths.collect()

print("The result is %s" % result)