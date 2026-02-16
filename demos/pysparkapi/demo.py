import shutil
import os
from pyspark import SparkContext

if os.path.exists("lengths-output"):
    shutil.rmtree("lengths-output")  # Clean up from previous runs

sc = SparkContext("local[*]", "Simple PySpark Demo")
inputFile = sc.textFile("Macbeth.txt")
lengths = inputFile.map(lambda line: len(line))
lengths.saveAsTextFile("lengths-output")
sc.stop()