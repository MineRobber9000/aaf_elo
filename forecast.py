import csv, aaf

league = aaf.League([])

with open("aaf_elo.csv") as f:
	r = csv.reader(f)
	next(r) # skip header
	for row in r:
		league.team[row[0]]=aaf.Team(row[0],float(row[1]))

def forecast(team,opponent):
	team = league.team[team]
	opponent = league.team[opponent]
	ts = team.expected(opponent)
	os = opponent.expected(team)
	if ts==os:
		return False, 0
	elif ts>os:
		return team.name, ((max(ts,os)-min(ts,os))/2)
	else:
		return opponent.name, ((max(ts,os)-min(ts,os))/2)

#print("Team expected:     {!s}".format(ts))
#print("Opponent expected: {!s}".format(os))
#print("Confidence:        {:.2%}".format((max(ts,os)-min(ts,os))/2))
