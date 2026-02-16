from pyspark import SparkContext

sc = SparkContext("local[*]", "Map Transformation Demo")

lines = sc.textFile("Macbeth.txt")
lengths = lines.map(lambda line: len(line))
result = lengths.collect()

print("The result is %s" % result)

sc.stop()