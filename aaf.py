from elo import elo, expected

DEFAULT_SCORE = 1500

class Team:
	def __init__(self,name,score=DEFAULT_SCORE):
		self.name = name
		self.score = score
	def expected(self,opponent):
		return expected(self.score,opponent.score)
	def post_game(self,opponentscore,score):
		self.score = round(elo(self.score,self.expected(Team("DUMMY_TEAM",opponentscore)),score),3)

def reverse_wlt(wlt):
	if wlt==0.5: return 0.5 # reverse of a tie is a tie
	if wlt==0: return 1 # reverse of a loss is a win
	if wlt==1: return 0 # reverse of a win is a loss

class League:
	def __init__(self,teams=[]):
		for k in range(len(teams)):
			if type(teams[k])!=Team:
				teams[k]=Team(teams[k])
		self.team = {}
		for team in teams:
			self.team[team.name]=team
	def match(self,team,opponent,wlt=0.5):
		ts = team.score*1
		#print("Before:")
		#print(team.name,team.score)
		#print(opponent.name,opponent.score)
		team.post_game(opponent.score,wlt)
		opponent.post_game(ts,reverse_wlt(wlt))
		#print("After:")
		#print(team.name,team.score)
		#print(opponent.name,opponent.score)
