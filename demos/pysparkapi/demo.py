import shutil
import os
from pyspark import SparkContext

# Clean up any existing output directory from previous runs
if os.path.exists("lengths-output"):
    shutil.rmtree("lengths-output")  # Remove the directory and its contents

# Initialize Spark context for local execution with multiple cores
sc = SparkContext("local[*]", "Simple PySpark Demo")

# Read the input text file into an RDD (Resilient Distributed Dataset)
inputFile = sc.textFile("Macbeth.txt")

# Map each line to its length (number of characters)
lengths = inputFile.map(lambda line: len(line))

# Save the lengths RDD to text files in the output directory
# This creates a 'lengths-output' folder containing:
# - _SUCCESS: Marker file indicating successful job completion
# - part-00000, part-00001, etc.: Partitioned output files with line lengths (integers)
# - .crc files: Checksum files for data integrity
lengths.saveAsTextFile("lengths-output")

# Stop the Spark context to free resources
sc.stop()