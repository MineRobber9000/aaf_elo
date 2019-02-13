import csv, forecast

records = {k: [0,0,0] for k in forecast.league.team.keys()}

with open("season.csv") as f:
	games = list(csv.reader(f))
for game in games:
	winner, confidence = forecast.forecast(game[0],game[1])
	if winner==False:
		print("{} and {} tie".format(*game))
		records[game[0]][2]+=1
		records[game[1]][2]+=1
		forecast.league.match(forecast.league.team[game[0]],forecast.league.team[game[1]],0.5)
	elif winner==game[0]:
		print("{} def. {}".format(*game))
		records[game[0]][0]+=1
		records[game[1]][1]+=1
		forecast.league.match(forecast.league.team[game[0]],forecast.league.team[game[1]],1)
	elif winner==game[1]:
		print("{1} def. {0}".format(*game))
		records[game[0]][1]+=1
		records[game[1]][0]+=1
		forecast.league.match(forecast.league.team[game[0]],forecast.league.team[game[1]],0)
print("---")
for team in forecast.league.team:
	print("{}: {!s}-{!s}-{!s} (ELO: {!s})".format(*([team]+records[team]+[forecast.league.team[team].score])))
