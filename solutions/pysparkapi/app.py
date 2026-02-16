import shutil
import os

# Clean up from previous runs
if os.path.exists("witches"):
    shutil.rmtree("witches")

print("Hello World\n")

from pyspark import SparkContext
sc = SparkContext("local[*]", "PySpark API Lab")

lines = sc.textFile("Macbeth.txt")

numLines = lines.count()
print("Number of lines: %d" % numLines)

firstLine = lines.first()
print("First line: %s" % firstLine)

witchLines = lines.filter(lambda line: "Witch" in line)
print("Witch lines: %s" % witchLines)

witchLines.saveAsTextFile("witches")

sc.stop()

