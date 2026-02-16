print("Hello World\n")

from pyspark import SparkContext
sc = SparkContext()

lines = sc.textFile("Macbeth.txt")

numLines = lines.count()
print("Number of lines: %d" % numLines)

firstLine = lines.first()
print("First line: %s" % firstLine)

witchLines = lines.filter(lambda line: "Witch" in line)
print("Witch lines: %s" % witchLines)

witchLines.saveAsTextFile("witches")

