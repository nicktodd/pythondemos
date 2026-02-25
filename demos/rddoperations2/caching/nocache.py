from pyspark import SparkContext

sc = SparkContext("local[*]", "No Cache Demo")

# Without caching, Spark will re-read and reprocess the log files from disk
# for every action that depends on the logs RDD
# This means the files are read twice - once for errorCount and once for warningCount
logs = sc.textFile("log_files")   # This will be evaluated twice.

errorLogs   = logs.filter(lambda line: "ERROR" in line)
warningLogs = logs.filter(lambda line: "WARNING" in line)

errorCount   = errorLogs.count()
warningCount = warningLogs.count()

print("errorCount: %d, warningCount: %d" % (errorCount, warningCount))

sc.stop()