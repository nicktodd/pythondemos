from pyspark import SparkContext
from element import Element

sc = SparkContext()
sc.setLogLevel("WARN")

# Read all the lines of element data.
lines = sc.textFile("elements.txt")

# Map each line into an Element object. 
elements = lines.map(lambda line: Element(line)) 
                        
# Group elements by period.
groupedByPeriod = elements.groupBy(lambda e: e.period).collect()
print("Elements grouped by period: %s" % groupedByPeriod)

# Create a dict, where the key is the element symbol, and the value is the element itself.
keyedBySymbol = elements.keyBy(lambda e: e.symbol).collect()
print("Elements keyed by symbol: %s" % keyedBySymbol)

# Sort elements by name.
sortedByName = elements.sortBy(lambda e: e.name).collect()
print("Elements sorted by name: %s" % sortedByName)

# Repartition elements into 5 partitions, and save in a directory named "partitionedElements".
repartitionedElements = elements.repartition(5)
repartitionedElements.saveAsTextFile("partitionedElements")
