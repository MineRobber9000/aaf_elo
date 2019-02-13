import csv, aaf

league = aaf.League("Legends Apollos Iron Express Stallions Hotshots Commanders Fleet".split())
with open("aaf_games.csv") as f:
	games = list(csv.reader(f))
for game in games:
	league.match(league.team[game[0]],league.team[game[1]],1)
for team in league.team:
	print(team,league.team[team].score)
rows = [[team,league.team[team].score] for team in league.team.keys()]
with open("aaf_elo.csv","w") as f:
	w = csv.writer(f)
	w.writerow(["Team","Score"])
	w.writerows(rows)
