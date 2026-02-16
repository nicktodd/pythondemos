from pyspark import SparkContext

sc = SparkContext()

kvRdd = sc.parallelize( [ ["UK","London"], ["FR","Paris"], ["UK","Leeds"], ["SA","Joburg"] ] )

countByKeyResult = kvRdd.countByKey()

print("countByKeyResult: %s" % countByKeyResult)


