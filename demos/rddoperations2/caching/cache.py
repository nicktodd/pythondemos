from pyspark import SparkContext

sc = SparkContext("local[*]", "Cache Demo")

logs = sc.textFile("log_files")   
# cache() stores the RDD in memory after it is first computed
# Both errorLogs and warningLogs derive from logs, so without caching
# Spark would re-read the files from disk twice (once per action)
# With cache(), the logs RDD is read once and reused from memory
logs.cache()

# Create two filtered views of the cached logs RDD
errorLogs   = logs.filter(lambda line: "ERROR" in line)
warningLogs = logs.filter(lambda line: "WARNING" in line)

# Both count() calls reuse the cached logs data, avoiding redundant disk reads
errorCount   = errorLogs.count()
warningCount = warningLogs.count()

print("errorCount: %d, warningCount: %d" % (errorCount, warningCount))

sc.stop()
