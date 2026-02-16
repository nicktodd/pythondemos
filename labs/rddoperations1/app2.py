from pyspark import SparkContext
sc = SparkContext()
sc.setLogLevel("WARN")

teams = sc.textFile("teams.txt")
stadiums = sc.textFile("stadiums.txt")

# In each of the following statements, replace "None" with a suitable call to a PySpark API function...

# Zip teams with stadiums.
teamsAndStadiums = None
print("Teams and stadiums: %s" % teamsAndStadiums)

# Cartesian product of all teams.
cartesian = None
print("Cartesian product of all teams: %s" % cartesian)

# Fixtures.
fixtures = None
print("Fixtures: %s" % fixtures)

