from pyspark import SparkContext
sc = SparkContext("local[*]", "Filter Transformation Demo")

# Load the text file into an RDD where each element is a single line
lines = sc.textFile("Macbeth.txt")
# filter() keeps only the elements where the condition returns True
# Here we keep only lines with more than 50 characters
longLines = lines.filter(lambda line: len(line) > 50)
result = longLines.collect()

print("The result is %s" % result)

sc.stop()
