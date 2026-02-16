from pyspark import SparkContext
from element import Element

sc = SparkContext("local[*]", "RDD Operations Part 1 - Exercise 3")
sc.setLogLevel("WARN")

# Read all the lines of element data.
lines = sc.textFile("elements.txt")

# In each of the following statements, replace "None" with a suitable call to a PySpark API function...

# Map each line into an Element object. 
elements = None
                        
# Group elements by period.
groupedByPeriod = None
print("Elements grouped by period: %s" % groupedByPeriod)

# Create a dict, where the key is the element symbol, and the value is the element itself.
keyedBySymbol = None
print("Elements keyed by symbol: %s" % keyedBySymbol)

# Sort elements by name.
sortedByName = None
print("Elements sorted by name: %s" % sortedByName)

# Repartition elements into 5 partitions, and then add code to save in a directory named "partitionedElements".
repartitionedElements = None

sc.stop()
