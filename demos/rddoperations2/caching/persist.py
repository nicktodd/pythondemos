from pyspark import SparkContext
from pyspark import StorageLevel

sc = SparkContext("local[*]", "Persist Demo")

logs = sc.textFile("log_files")   
logs.persist(StorageLevel.DISK_ONLY)

errorLogs   = logs.filter(lambda line: "ERROR" in line)
warningLogs = logs.filter(lambda line: "WARNING" in line)

errorCount   = errorLogs.count()
warningCount = warningLogs.count()

print("errorCount: %d, warningCount: %d" % (errorCount, warningCount))

sc.stop()
