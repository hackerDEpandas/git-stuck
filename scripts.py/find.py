import nflgame as nf
import pandas as pd
import numpy as np

class passing(object):
	def __init__(self, player, name, team):
		self.data = player
		self.name = name
		self.team = team
########################################################################
	def passing_tds(self):
	
		self.mecca = str(self.data.passing().filter(passing_tds_gt = 0).name(self.name))
		if self.mecca == self.name:
			for p in self.data.passing().filter(passing_tds_gt = 0).sort('passing_tds'):
				if str(p) == self.mecca and str(p.team) == self.team:
					self.holder = (str(p),str(p.team), int(p.passing_tds))
		else:
			return 0
		return self.holder[2]
########################################################################
	def passing_yds(self):
	
		self.mecca = str(self.data.passing().filter(passing_yds_gt = 0).name(self.name))
		if self.mecca == self.name:
			for p in self.data.passing().filter(passing_yds_gt = 0).sort('passing_yds'):
				if str(p) == self.mecca and str(p.team) == self.team:
					self.holder = (str(p), str(p.team), int(p.passing_yds))
		else:
			return 0
		return self.holder[2]
########################################################################
	def passing_int(self):
	
		self.mecca = str(self.data.passing().filter(passing_ints_gt = 0).name(self.name))
		if self.mecca == self.name:
			for p in self.data.passing().filter(passing_ints_gt = 0).sort('passing_ints'):
				if str(p) == self.mecca and str(p.team) == self.team:
					self.holder = (str(p), str(p.team), int(p.passing_ints))
		else:
			return 0
		return self.holder[2]
########################################################################
	def fumbles_lost(self):
		self.mecca = str(self.data.passing().filter(fumbles_lost_gt = 0).name(self.name))

		if self.mecca == self.name:
			for p in self.data.passing().filter(fumbles_lost_gt = 0).sort('fumbles_lost'):
				if str(p) == self.mecca and str(p.team) == self.team:
					self.holder = (str(p), str(p.team), int(p.fumbles_lost))
		else:
			return 0
		return self.holder[2]
########################################################################
	def rushing_tds(self):
		self.mecca = str(self.data.passing().filter(rushing_tds_gt = 0).name(self.name))
		if self.mecca == self.name:
			for p in self.data.passing().filter(rushing_tds_gt = 0).sort('rushing_yds'):
				if str(p) == self.mecca and str(p.team) == self.team:
					self.holder = (str(p), str(p.team), int(p.rushing_tds))
		else:
			return 0
		return self.holder[2]
########################################################################
	def rushing_yds(self):
		self.mecca = str(self.data.passing().filter(rushing_yds_gt = 0).name(self.name))
		if self.mecca == self.name:
			for p in self.data.passing().filter(rushing_yds_gt = 0).sort('rushing_tds'):
				if str(p) == self.mecca and str(p.team) == self.team:
					self.holder = (str(p), str(p.team), int(p.rushing_yds))
		else:
			return 0
		return self.holder[2]
########################################################################	

########################################################################
class rushing(object):
	def __init__(self, player, name, team):
		self.data = player
		self.name = name
		self.team = team
#########################################################################
	def receiving_tds(self):
	
		self.mecca = str(self.data.receiving().filter(receiving_rec_gt = 0).name(self.name))
		if self.mecca == self.name:
			for p in self.data.receiving().filter(receiving_rec_gt = 0).sort('receiving_rec'):
				if str(p) == self.mecca and str(p.team) == self.team:
					self.holder = (str(p), str(p.team), int(p.receiving_tds))
		else:
			return 0
		return self.holder[2]
#########################################################################
	def receiving_yds(self):
		self.mecca = str(self.data.receiving().filter(receiving_rec_gt = 0).name(self.name))
		if self.mecca == self.name:
			for p in self.data.receiving().filter(receiving_rec_gt = 0).sort('receiving_rec'):
				if str(p) == self.mecca and str(p.team) == self.team:
					self.holder = (str(p), str(p.team), int(p.receiving_yds))
		else:
			return 0
		return self.holder[2]
#########################################################################
	def receiving_rec(self):
		self.mecca = str(self.data.receiving().filter(receiving_rec_gt = 0).name(self.name))
		if self.mecca == self.name:
			for p in self.data.receiving().filter(receiving_rec_gt = 0).sort('receiving_rec'):
				if str(p) == self.mecca and str(p.team) == self.team:
					self.holder = (str(p), str(p.team), int(p.receiving_rec))
		else:
			return 0
		return self.holder[2]
#########################################################################
	def rushing_tds(self):
		self.mecca = str(self.data.rushing().filter(rushing_tds_gt = 0).name(self.name))
		if self.mecca == self.name:
			for p in self.data.rushing().filter(rushing_tds_gt = 0).sort('rushing_yds'):
				if str(p) == self.mecca and str(p.team) == self.team:
					self.holder = (str(p), str(p.team), int(p.rushing_tds))
		else:
			return 0
		return self.holder[2]
#########################################################################
	def rushing_yds(self):
		self.mecca = str(self.data.rushing().filter(rushing_yds_gt = 0).name(self.name))
		if self.mecca == self.name:
			for p in self.data.rushing().filter(rushing_yds_gt = 0).sort('rushing_tds'):
				if str(p) == self.mecca and str(p.team) == self.team:
					self.holder = (str(p), str(p.team), int(p.rushing_yds))
		else:
			return 0
		return self.holder[2]
#########################################################################
	def fumbles_lost(self):
		self.mecca = str(self.data.rushing().filter(fumbles_lost_gt = 0).name(self.name))
		if self.mecca == self.name:
			for p in self.data.rushing().filter(fumbles_lost_gt = 0).sort('fumbles_lost'):
				if str(p) == self.mecca and str(p.team) == self.team:
					self.holder = (str(p), str(p.team), int(p.fumbles_lost))
		else:
			return 0
		return self.holder[2]
		
#########################################################################
	def fumbles_lost_rec(self):
		self.mecca = str(self.data.receiving().filter(fumbles_lost_gt = 0).name(self.name))
		if self.mecca == self.name:
			for p in self.data.receiving().filter(fumbles_lost_gt = 0).sort('fumbles_lost'):
				if str(p) == self.mecca and str(p.team) == self.team:
					self.holder = (str(p), str(p.team), int(p.fumbles_lost))
		else:
			return 0

		return self.holder[2]
		
#########################################################################

#########################################################################
class player_gen(object):
	def __init__(self, player):
		self.data = player
		self.qb = []
		self.rb = []
		self.wr = []
########################################################################
	def running_backs(self):
	
		for p in self.data.rushing().sort('rushing_yds').limit(100):
			if str(p.guess_position) == 'RB':
				self.rb.append((str(p), str(p.team), str(p.guess_position)))
		return self.rb
########################################################################
	def wide_receivers(self):
	
		for p in self.data.receiving().sort('receiving_rec').limit(100):
			if str(p.guess_position) == 'WR' or str(p.guess_position) == 'TE':
				self.wr.append((str(p), str(p.team), str(p.guess_position)))
		return self.wr
#######################################################################
	def quarter_backs(self):

		for p in self.data.passing().sort('passing_tds').limit(32):
			self.qb.append((str(p), str(p.team), str(p.guess_position)))
		return self.qb
########################################################################
games = nf.games(2015, week = [4,5,6,7])
players = nf.combine_game_stats(games)


instance_player_gen = player_gen(players)
qb = instance_player_gen.quarter_backs()
rb = instance_player_gen.running_backs()
wr = instance_player_gen.wide_receivers()
final_qb = []
final_rb = []
final_wr = []

for x in rb:
	instance_rushing = rushing(players, x[0], x[1])
	final_rb.append({'A_Name':x[0], 'B_Team':x[1],'C_Pos.':x[2], 'D_Rush_yds':instance_rushing.rushing_yds(), 'E_Rush_tds':instance_rushing.rushing_tds(), 'F_Fumb_lost':instance_rushing.fumbles_lost(),'G_Rec':instance_rushing.receiving_rec(), 'H_Rec_yds':instance_rushing.receiving_yds(), 'I_Rec_tds':instance_rushing.receiving_tds(),'J_FanDuel_pts':round((instance_rushing.rushing_yds()*.1)+(instance_rushing.rushing_tds()*6.0)+(instance_rushing.receiving_rec()*.5)+(instance_rushing.receiving_yds()*.1)+(instance_rushing.receiving_tds()*6.0)-(instance_rushing.fumbles_lost()*2.0), 2)})

for x in qb:
	instance_passing = passing(players, x[0], x[1])
	final_qb.append({'A_Name':x[0], 'B_Team':x[1],'C_Pos.':x[2],'D_Pass_yds':instance_passing.passing_yds(),'E_Passing_tds':instance_passing.passing_tds(), 'F_Rush_yds':instance_passing.rushing_yds(), 'G_Rush_tds':instance_passing.rushing_tds(), 'H_Fumb_lost':instance_passing.fumbles_lost(),'I_Int':instance_passing.passing_int(),'J_FanDuel_pts':round((instance_passing.passing_yds()*.04)+(instance_passing.passing_tds()*4.0)+(instance_passing.rushing_yds()*.1)+(instance_passing.rushing_tds()*6.0)-(instance_passing.passing_int()*1.0)-(instance_passing.fumbles_lost()*2.0), 2)})

for x in wr:
	instance_receiving = rushing(players, x[0], x[1])
	final_wr.append({'A_Name':x[0], 'B_Team':x[1],'C_Pos.':x[2], 'D_Rec':instance_receiving.receiving_rec(),'E_Rec_yds':instance_receiving.receiving_yds(),'F_Rec_tds':instance_receiving.receiving_tds(),'G_Rush_yds':instance_receiving.rushing_yds(),'H_Rush_tds':instance_receiving.rushing_tds(),'I_Fumb_lost':instance_receiving.fumbles_lost_rec(),'J_FanDuel_pts':round((instance_receiving.receiving_rec()*.5)+(instance_receiving.receiving_yds()*.1)+(instance_receiving.receiving_tds()*6.0)+(instance_receiving.rushing_yds()*.1)+(instance_receiving.rushing_tds()*6.0)-(instance_receiving.fumbles_lost_rec()*2.0), 2)})
	
df_rb = pd.DataFrame(final_rb)
df_qb = pd.DataFrame(final_qb)
df_wr = pd.DataFrame(final_wr)

df_rb = df_rb.sort(columns = 'J_FanDuel_pts', axis = 0, ascending = False)
df_qb = df_qb.sort(columns = 'J_FanDuel_pts', axis = 0, ascending = False)
df_wr = df_wr.sort(columns = 'J_FanDuel_pts', axis = 0, ascending = False)
print df_rb
#np.savetxt('wide_receivers.txt', df_wr.values, fmt='%r')
#np.savetxt('running_backs.txt', df_rb.values, fmt='%r')
#np.savetxt('quarter_backs.txt', df_qb.values, fmt='%r')
