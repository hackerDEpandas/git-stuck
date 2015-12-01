import nflgame as nf
import pandas as pd
import numpy as np

class passing(object):
	def __init__(self, player, name, team):
		self.data = player
		self.name = name
		self.team = team
		self.holder = 0
########################################################################
	def passing_tds_pts(self):
	
		self.mecca = str(self.data.passing().filter(passing_tds_gte = 0).name(self.name))
		if self.mecca == self.name:
			for p in self.data.passing().filter(passing_tds_gt = 0).sort('passing_tds'):
				if str(p) == self.mecca and str(p.team) == self.team:
					self.holder = int(p.passing_tds)*4.0
		else:
			return 0
		return self.holder
########################################################################
	def passing_yds_pts(self):
	
		self.mecca = str(self.data.passing().filter(passing_yds_gt = 0).name(self.name))
		if self.mecca == self.name:
			for p in self.data.passing().filter(passing_yds_gt = 0).sort('passing_yds'):
				if str(p) == self.mecca and str(p.team) == self.team:
					self.holder = int(p.passing_yds)*0.04
		else:
			return 0
		return self.holder
########################################################################
	def passing_int_pts(self):
	
		self.mecca = str(self.data.passing().filter(passing_ints_gt = 0).name(self.name))
		if self.mecca == self.name:
			for p in self.data.passing().filter(passing_ints_gt = 0).sort('passing_ints'):
				if str(p) == self.mecca and str(p.team) == self.team:
					self.holder = int(p.passing_ints)*(-1.0)
		else:
			return 0
		return self.holder
########################################################################
	def fumbles_lost_pts(self):
		self.mecca = str(self.data.passing().filter(fumbles_lost_gt = 0).name(self.name))

		if self.mecca == self.name:
			for p in self.data.passing().filter(fumbles_lost_gt = 0).sort('fumbles_lost'):
				if str(p) == self.mecca and str(p.team) == self.team:
					self.holder = int(p.fumbles_lost)*(-2.0)
		else:
			return 0
		return self.holder
########################################################################
	def rushing_tds_pts(self):
		self.mecca = str(self.data.passing().filter(rushing_tds_gte = 0).name(self.name))
		if self.mecca == self.name:
			for p in self.data.passing().filter(rushing_tds_gt = 0).sort('rushing_yds'):
				if str(p) == self.mecca and str(p.team) == self.team:
					self.holder = int(p.rushing_tds)*6.0
		else:
			return 0
		return self.holder
########################################################################
	def rushing_yds_pts(self):
		self.mecca = str(self.data.passing().filter(rushing_yds_gt = 0).name(self.name))
		if self.mecca == self.name:
			for p in self.data.passing().filter(rushing_yds_gt = 0).sort('rushing_tds'):
				if str(p) == self.mecca and str(p.team) == self.team:
					self.holder = int(p.rushing_yds)*0.1
		else:
			return 0
		return self.holder
########################################################################	

########################################################################
class rushing(object):
	def __init__(self, player, name, team):
		self.data = player
		self.name = name
		self.team = team
		self.holder = 0
#########################################################################
	def receiving_tds_pts(self):
	
		self.mecca = str(self.data.receiving().filter(receiving_rec_gte = 0).name(self.name))
		if self.mecca == self.name:
			for p in self.data.receiving().filter(receiving_rec_gte = 0).sort('receiving_rec'):
				if str(p) == self.mecca and str(p.team) == self.team:
					self.holder = int(p.receiving_tds)*6.0
		else:
			return 0
		return self.holder
#########################################################################
	def receiving_yds_pts(self):
		self.mecca = str(self.data.receiving().filter(receiving_rec_gte = 0).name(self.name))
		if self.mecca == self.name:
			for p in self.data.receiving().filter(receiving_rec_gte = 0).sort('receiving_rec'):
				if str(p) == self.mecca and str(p.team) == self.team:
					self.holder = int(p.receiving_yds)*0.1
		else:
			return 0
		return self.holder
#########################################################################
	def receiving_rec_pts(self):
		self.mecca = str(self.data.receiving().filter(receiving_rec_gte = 0).name(self.name))
		if self.mecca == self.name:
			for p in self.data.receiving().filter(receiving_rec_gte = 0).sort('receiving_rec'):
				if str(p) == self.mecca and str(p.team) == self.team:
					self.holder = int(p.receiving_rec)*0.5
		else:
			return 0
		return self.holder
#########################################################################
	def rushing_tds_pts(self):
		self.mecca = str(self.data.rushing().filter(rushing_tds_gte = 0).name(self.name))
		if self.mecca == self.name:
			for p in self.data.rushing().filter(rushing_tds_gt = 0).sort('rushing_yds'):
				if str(p) == self.mecca and str(p.team) == self.team:
					self.holder = int(p.rushing_tds)*6.0
		else:
			return 0
		return self.holder
#########################################################################
	def rushing_yds_pts(self):
		self.mecca = str(self.data.rushing().filter(rushing_yds_gt = 0).name(self.name))
		if self.mecca == self.name:
			for p in self.data.rushing().filter(rushing_yds_gt = 0).sort('rushing_tds'):
				if str(p) == self.mecca and str(p.team) == self.team:
					self.holder = int(p.rushing_yds)*0.1
		else:
			return 0
		return self.holder
#########################################################################
	def fumbles_lost_pts(self):
		self.mecca = str(self.data.rushing().filter(fumbles_lost_gte = 0).name(self.name))
		if self.mecca == self.name:
			for p in self.data.rushing().filter(fumbles_lost_gt = 0).sort('fumbles_lost'):
				if str(p) == self.mecca and str(p.team) == self.team:
					self.holder = int(p.fumbles_lost)*(-2.0)
		else:
			return 0
		return self.holder
		
#########################################################################
	def fumbles_lost_rec_pts(self):
		self.mecca = str(self.data.receiving().filter(fumbles_lost_gte = 0).name(self.name))
		if self.mecca == self.name:
			for p in self.data.receiving().filter(fumbles_lost_gt = 0).sort('fumbles_lost'):
				if str(p) == self.mecca and str(p.team) == self.team:
					self.holder = int(p.fumbles_lost)*(-2.0)
		else:
			return 0

		return self.holder
		
#########################################################################

#########################################################################
class fanduel_pts(object):
	def __init__(self, player, name, team):

		self.instance_passing = passing(player, name, team)
		self.instance_rushing = rushing(player, name, team)
#########################################################################
	def passer_pts(self):
		self.total_pts = sum([self.instance_passing.passing_yds_pts(), self.instance_passing.passing_tds_pts(), self.instance_passing.passing_int_pts(), self.instance_passing.fumbles_lost_pts(), self.instance_passing.rushing_yds_pts(), self.instance_passing.rushing_tds_pts()])
		return round(self.total_pts,2)
#########################################################################
	def runner_pts(self):
		self.total_pts = sum([self.instance_rushing.fumbles_lost_pts(), self.instance_rushing.rushing_yds_pts(), self.instance_rushing.rushing_tds_pts(), self.instance_rushing.receiving_rec_pts(), self.instance_rushing.receiving_yds_pts(), self.instance_rushing.receiving_tds_pts()])
		return round(self.total_pts,2)
#########################################################################
	def receiver_pts(self):
		self.total_pts = sum([self.instance_rushing.receiving_rec_pts(), self.instance_rushing.receiving_yds_pts(), self.instance_rushing.receiving_tds_pts(), self.instance_rushing.rushing_yds_pts(), self.instance_rushing.rushing_tds_pts(), self.instance_rushing.fumbles_lost_rec_pts()])
		return round(self.total_pts,2)
#########################################################################

#########################################################################
class player_gen(object):
	def __init__(self, player):
		self.data = player
		self.qb = []
		self.rb = []
		self.wr = []
		self.instance_fanduel_pts = None
		self.pts = 0
########################################################################
	def running_backs(self):
	
		for p in self.data.rushing().filter(rushing_att_gt = 0).limit(150):
			self.instance_fanduel_pts = fanduel_pts(self.data, str(p), str(p.team))
			self.pts = self.instance_fanduel_pts.runner_pts()
			if str(p.guess_position) == 'RB':
				self.rb.append((str(p), str(p.team), str(p.guess_position), self.pts))
		return self.rb
########################################################################
	def wide_receivers(self):
	
		for p in self.data.receiving().filter(receiving_rec_gte = 0):
			self.instance_fanduel_pts = fanduel_pts(self.data, str(p), str(p.team))
			self.pts = self.instance_fanduel_pts.receiver_pts()
			if str(p.guess_position) == 'WR' or str(p.guess_position) == 'TE':
				self.wr.append((str(p), str(p.team), str(p.guess_position), self.pts))
		return self.wr
#######################################################################
	def quarter_backs(self):

		for p in self.data.passing().filter(passing_yds_gt = 0).limit(40):
			self.instance_fanduel_pts = fanduel_pts(self.data, str(p), str(p.team))
			self.pts = self.instance_fanduel_pts.passer_pts()

			self.qb.append((str(p), str(p.team), str(p.guess_position), self.pts))
		return self.qb
########################################################################

#########################################################################
class player_df(object):
	def __init__(self, player):
		self.instance_player_gen = player_gen(player)
		self.qb = self.instance_player_gen.quarter_backs()
		self.wr = self.instance_player_gen.wide_receivers()
		self.rb = self.instance_player_gen.running_backs()
		self.final_wr = []
		self.final_rb = []
		self.final_qb = []
#########################################################################
	def wr_df(self):
		for i in self.wr:
			self.final_wr.append({'A_Name':i[0], 'B_Team':i[1], 'C_Pos':i[2], 'PTS':i[3]})
		return pd.DataFrame(self.final_wr)
#########################################################################
	def rb_df(self):
		for i in self.rb:
			self.final_rb.append({'A_Name':i[0], 'B_Team':i[1], 'C_Pos':i[2], 'PTS':i[3]})
		return pd.DataFrame(self.final_rb)
#########################################################################
	def qb_df(self):
		for i in self.qb:
			self.final_qb.append({'A_Name':i[0], 'B_Team':i[1], 'C_Pos':i[2], 'PTS':i[3]})
		return pd.DataFrame(self.final_qb)
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
