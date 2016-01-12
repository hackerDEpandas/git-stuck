from datetime import datetime
start_time = datetime.now()
import nflgame as nf
import pandas as pd
import numpy as np

games = nf.games(2015, week = [13,14,15,16,17])
players = nf.combine_game_stats(games)
name_arr = []
arr = []
tuples = []
quarter_backs = []

###########################################################################
def passer_gen(team):
	for p in players.passing().filter(passing_yds_gt = 0).sort('passing_yds'):
		if str(p.guess_position) == 'QB' and str(p.team) == team:
			name_arr.append(str(p.name))
	return name_arr
##########################################################################
def passing_stats(player, team):
	for i in player:
		mecca = str(players.passing().filter(passing_yds_gt = 0).name(i))
		if mecca == i:
			for p in players.passing().filter(passing_yds_gt = 0).sort('passing_yds'):
				if str(p) == mecca and str(p.team) == team:
					holder = (str(p.name), str(p.team), str(p.guess_position), int(p.passing_yds), int(p.passing_tds), int(p.rushing_yds), int(p.rushing_tds), int(p.passing_ints), int(p.fumbles_lost),)
					pts = round(sum((int(p.passing_yds)*0.04, int(p.passing_tds)*4.0, int(p.rushing_yds)*0.1, int(p.rushing_tds)*6.0, int(p.passing_ints)*-1.0, int(p.fumbles_lost)*-2.0)), 2)
					final = holder + (pts,)
					tuples.append(final)
		else:
			return 0
	return tuples
##########################################################################
def combine_data(teams):
	for i in teams:
		name = passer_gen(i)
		var = passing_stats(name, i)
	for j in var:
		arr.append(j)
	return arr
##########################################################################
teams = ['DET', 'GB', 'NYG', 'NYJ', 'BUF', 'HOU', 'MIA', 'BAL', 'CLE', 'CIN', 'TEN', 'JAC', 'CHI', 'SF', 'MIN', 'SEA', 'NO', 'CAR', 'TB', 'ATL', 'STL', 'ARI', 'OAK', 'KC', 'SD', 'DEN', 'NE', 'PHI', 'PIT', 'IND', 'WAS', 'DAL']
#['DET', 'CHI', 'SEA', 'CAR', 'ATL', 'ARI', 'SD', 'DEN', 'NE', 'TB']

for i in combine_data(teams):
	quarter_backs.append({'A_Name':i[0], 'B_Team':i[1], 'C_Pos':i[2], 'D_Pass_Yds':i[3], 'E_Pass_Tds':i[4], 'F_Rush_Yds':i[5], 'G_Rush_Tds':i[6], 'H_Pass_Ints':i[7], 'I_Fum_Lost':i[8], 'J_FD_PTS':i[9]})

picks = pd.DataFrame(quarter_backs)
np.savetxt('quarter_backs_5_week_trend.txt', picks.sort(columns = 'J_FD_PTS', ascending = False), fmt='%r')

print datetime.now() - start_time
