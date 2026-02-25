from pyspark import SparkContext

sc = SparkContext("local[*]", "Map Transformation Demo")

# Load each line of the text file as an element in the RDD
lines = sc.textFile("Macbeth.txt")
# map() applies the function to every element and returns a new RDD
# Here each line is transformed into its character length
# Result: an RDD of integers (one per line)
lengths = lines.map(lambda line: len(line))
result = lengths.collect()

print("The result is %s" % result)

sc.stop()