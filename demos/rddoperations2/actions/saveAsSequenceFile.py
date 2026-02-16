import shutil
import os
from pyspark import SparkContext

if os.path.exists("pairsAsSequence"):
    shutil.rmtree("pairsAsSequence")
if os.path.exists("pairsAsText"):
    shutil.rmtree("pairsAsText")

sc = SparkContext("local[*]", "SaveAsSequenceFile Action Demo")

pairRdd = sc.parallelize( [ ("UK", "London"), ("FR", "Paris"), ("SA", "Pretoria"), ("NO", "Oslo") ] )

pairRdd.saveAsSequenceFile("pairsAsSequence")
pairRdd.saveAsTextFile("pairsAsText")

sc.stop()
