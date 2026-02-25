from pyspark import SparkContext
sc = SparkContext("local[*]", "FlatMap Transformation Demo")

# Read lines from the text file into an RDD. Each element is a line from the file.
lines = sc.textFile("Macbeth.txt")
    
# Use flatMap to split each line into words. This flattens the lists of words into a single RDD of words.
words = lines.flatMap(lambda line: line.split(" "))
    
# Collect all words into a list.
result = words.collect()

print("The result is %s" % result)

sc.stop()

