from pyspark import SparkContext
from pyspark import StorageLevel

sc = SparkContext("local[*]", "Persist Demo")

logs = sc.textFile("log_files")   
# persist() is like cache() but lets you explicitly specify the StorageLevel
# DISK_ONLY stores the RDD serialised on disk rather than in memory
# Other options include: MEMORY_ONLY, MEMORY_AND_DISK, MEMORY_ONLY_SER, OFF_HEAP
# Use persist() when you need fine-grained control over how data is stored
logs.persist(StorageLevel.DISK_ONLY)

# Both filtered RDDs derive from the persisted logs RDD
errorLogs   = logs.filter(lambda line: "ERROR" in line)
warningLogs = logs.filter(lambda line: "WARNING" in line)

# Both count() calls reuse the persisted logs data from disk
errorCount   = errorLogs.count()
warningCount = warningLogs.count()

print("errorCount: %d, warningCount: %d" % (errorCount, warningCount))

sc.stop()
