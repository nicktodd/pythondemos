from pyspark import SparkContext

sc = SparkContext()

pairRdd = sc.parallelize( [ ("UK", "London"), ("FR", "Paris"), ("SA", "Pretoria"), ("NO", "Oslo") ] )

pairRdd.saveAsSequenceFile("pairsAsSequence")
pairRdd.saveAsTextFile("pairsAsText")
