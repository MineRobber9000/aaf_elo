import forecast

team = input("Team?: ")
opponent = input("Opponent?: ")

winner,confidence = forecast.forecast(team,opponent)

if not winner:
	print("I expect a tie!")
elif winner==team:
	print("The {} are gonna blow the {}'s socks off!".format(team,opponent))
else:
	print("The {} are gonna blow the {}'s socks off!".format(opponent,team))

print("Confidence:        {:.2%}".format(confidence))
