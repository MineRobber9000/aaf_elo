import csv, aaf

league = aaf.League("Legends Apollos Iron Express Stallions Hotshots Commanders Fleet".split())
with open("aaf_games.csv") as f:
	games = list(csv.reader(f))
for game in games:
	if game[2]=="0.5":
		print("{} and {} tie".format(*game))
	else:
		print("{} def. {}".format(*([game[0],game[1]] if game[2]=="1" else [game[1],game[0]])))
	league.match(league.team[game[0]],league.team[game[1]],float(game[2]))
for team in league.team:
	print(team,league.team[team].score)
rows = [[team,league.team[team].score] for team in league.team.keys()]
with open("aaf_elo.csv","w") as f:
	w = csv.writer(f)
	w.writerow(["Team","Score"])
	w.writerows(rows)
