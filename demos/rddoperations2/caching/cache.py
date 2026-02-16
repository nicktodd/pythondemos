from pyspark import SparkContext

sc = SparkContext()

logs = sc.textFile("log_files")   
logs.cache()

errorLogs   = logs.filter(lambda line: "ERROR" in line)
warningLogs = logs.filter(lambda line: "WARNING" in line)

errorCount   = errorLogs.count()
warningCount = warningLogs.count()

print("errorCount: %d, warningCount: %d" % (errorCount, warningCount))
