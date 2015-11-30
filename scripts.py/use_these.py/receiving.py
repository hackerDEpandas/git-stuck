import nflgame as nf
import pandas as pd
import numpy as np

class receiving(object):
	def __init__(self, player, name, team):
		self.data = player
		self.name = name
		self.team = team
		self.holder = 0
#########################################################################
	def receiving_pts(self):
		self.mecca = str(self.data.receiving().filter(receiving_rec_gte = 0).name(self.name))
		if self.mecca == self.name:
			for p in self.data.receiving().filter(receiving_rec_gte = 0).sort('receiving_rec'):
				if str(p) == self.mecca and str(p.team) == self.team:
					self.holder = round(sum([int(p.receiving_rec)*0.5, int(p.receiving_yds)*0.1, int(p.receiving_tds)*6.0, int(p.rushing_yds)*0.1, int(p.rushing_tds)*6.0, int(p.fumbles_lost)*-2.0]), 2)
		else:
			return 0
		return self.holder
#########################################################################

#########################################################################
class player_gen(object):
	def __init__(self, player):
		self.data = player
		self.wr = []
		self.instance_fanduel_pts = None
		self.pts = 0
########################################################################
	def wide_receivers(self):
	
		for p in self.data.receiving().filter(receiving_rec_gte = 0):
			self.instance_fanduel_pts = receiving(self.data, str(p), str(p.team))
			self.pts = self.instance_fanduel_pts.receiving_pts()
			if str(p.guess_position) == 'WR' or str(p.guess_position) == 'TE':
				self.wr.append((str(p), str(p.team), str(p.guess_position), self.pts))
		return self.wr
#######################################################################

#########################################################################
class player_df(object):
	def __init__(self, player):
		self.instance_player_gen = player_gen(player)
		self.wr = self.instance_player_gen.wide_receivers()
		self.final_wr = []
#########################################################################
	def wr_df(self):
		for i in self.wr:
			self.final_wr.append({'A_Name':i[0], 'B_Team':i[1], 'C_Pos':i[2], 'PTS':i[3]})
		return pd.DataFrame(self.final_wr)
#########################################################################
d = {}
games = []
players = []
arr = []
count = 0

for i in range(1,12):
	games.append(nf.games(2015, week = i))
	d['week'+str(i)] = nf.combine_game_stats(games[count])
	count += 1
for i in range(1,12):
	for_now = d['week'+str(i)]
	instance_player_df = player_df(for_now)
	arr.append(instance_player_df.wr_df())
for i in range(1,12):
	np.savetxt('wide_receivers_tight_ends_week'+ str(i) + '.txt', arr[i-1], fmt='%r')
