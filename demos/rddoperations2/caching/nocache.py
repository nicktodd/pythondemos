from pyspark import SparkContext

sc = SparkContext("local[*]", "No Cache Demo")

logs = sc.textFile("log_files")   # This will be evaluated twice.

errorLogs   = logs.filter(lambda line: "ERROR" in line)
warningLogs = logs.filter(lambda line: "WARNING" in line)

errorCount   = errorLogs.count()
warningCount = warningLogs.count()

print("errorCount: %d, warningCount: %d" % (errorCount, warningCount))

sc.stop()