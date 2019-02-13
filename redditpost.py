import csv
from csv2md import csv2md
from forecast import forecast

out = "Current Elo ratings (includes preseason games):\n\n"
with open("aaf_elo.csv") as f:
	out += csv2md(list(csv.reader(f)),sort=lambda row: (0-float(row[1])))
	out+="\n\n"
out+="## Predictions\n"
with open("matchups.csv") as f:
	for row in csv.reader(f):
		winner, confidence = forecast(row[0],row[1])
		if winner==False:
			out+="Outcome unknown for {} vs. {}  \n".format(row[0],row[1])
		else:
			out+="{} **def.** {}  \n".format(winner,list(filter(lambda t: t!=winner,row))[0])
out=out.strip()+"\n"
with open("post.txt","w") as f:
	f.write(out)
