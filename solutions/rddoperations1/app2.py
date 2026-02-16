from pyspark import SparkContext
sc = SparkContext()
sc.setLogLevel("WARN")

teams = sc.textFile("teams.txt")
stadiums = sc.textFile("stadiums.txt")

# Zip teams with stadiums.
teamsAndStadiums = teams.zip(stadiums).collect()
print("Teams and stadiums: %s" % teamsAndStadiums)

# Cartesian product of all teams.
cartesian = teams.cartesian(teams).collect()
print("Cartesian product of all teams: %s" % cartesian)

# Fixtures.
fixtures = teams.cartesian(teams).filter(lambda twoTeams: twoTeams[0] != twoTeams[1]).collect()
print("Fixtures: %s" % fixtures)

