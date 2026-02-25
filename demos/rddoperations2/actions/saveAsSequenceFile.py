import shutil
import os
from pyspark import SparkContext

# Remove output directories if they already exist to avoid write conflicts
if os.path.exists("pairsAsSequence"):
    shutil.rmtree("pairsAsSequence")
if os.path.exists("pairsAsText"):
    shutil.rmtree("pairsAsText")

sc = SparkContext("local[*]", "SaveAsSequenceFile Action Demo")

# Key-value RDD with country codes and capital cities
pairRdd = sc.parallelize( [ ("UK", "London"), ("FR", "Paris"), ("SA", "Pretoria"), ("NO", "Oslo") ] )

# saveAsSequenceFile() saves the RDD as a Hadoop SequenceFile (binary key-value format)
pairRdd.saveAsSequenceFile("pairsAsSequence")
# saveAsTextFile() saves each element as a text string, one element per file part
pairRdd.saveAsTextFile("pairsAsText")

sc.stop()
