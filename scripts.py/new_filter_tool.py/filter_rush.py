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
running_backs = []

##########################################################################
def runner_gen(team):
	for p in players.rushing().filter(rushing_att_gte = 0).sort('rushing_att'):
		if (str(p.guess_position) == 'RB' or str(p.guess_position) == '') and str(p.team) == team:
			name_arr.append(str(p.name))
	return name_arr
##########################################################################
def rushing_stats(player, team):
	for i in player:
		mecca = str(players.rushing().filter(rushing_att_gte = 0).name(i))

		if mecca == i:
			for p in players.rushing().filter(rushing_att_gte = 0).sort('rushing_att'):
				if str(p) == mecca and str(p.team) == team:

					holder = (str(p.name), str(p.team), str(p.guess_position), int(p.receiving_rec), int(p.receiving_yds), int(p.receiving_tds), int(p.rushing_yds), int(p.rushing_tds), int(p.fumbles_lost),)
					pts = round(sum((int(p.receiving_rec)*0.5, int(p.receiving_yds)*0.1, int(p.receiving_tds)*6.0, int(p.rushing_yds)*0.1, int(p.rushing_tds)*6.0, int(p.fumbles_lost)*-2.0)), 2)
					final = holder + (pts,)
					tuples.append(final)
		else:
			return 0
	return tuples
##########################################################################
def combine_data(teams):
	for i in teams:
		team = i
		name = runner_gen(team)
		var = rushing_stats(name, team)
	for j in var:
		arr.append(j)
	return arr
##########################################################################
teams = ['DET', 'GB', 'NYG', 'NYJ', 'BUF', 'HOU', 'MIA', 'BAL', 'CLE', 'CIN', 'TEN', 'JAC', 'CHI', 'SF', 'MIN', 'SEA', 'NO', 'CAR', 'TB', 'ATL', 'STL', 'ARI', 'OAK', 'KC', 'SD', 'DEN', 'NE', 'PHI', 'PIT', 'IND', 'WAS', 'DAL']
#['CAR', 'ARI', 'CIN', 'DET', 'HOU', 'JAC', 'MIA', 'MIN', 'SD', 'TB', 'TEN', 'WAS']

for i in combine_data(teams):
	running_backs.append({'A_Name':i[0], 'B_Team':i[1], 'C_Pos':i[2], 'D_Rec':i[3], 'E_Rec_Yds':i[4], 'F_Rec_Tds':i[5], 'G_Rush_Yds':i[6], 'H_Rush_Tds':i[7], 'I_Fum_Lost':i[8], 'J_FD_PTS':i[9]})

picks = pd.DataFrame(running_backs)
np.savetxt('running_backs_5_week_trend.txt', picks.sort(columns = 'J_FD_PTS', ascending = False), fmt='%r')

print datetime.now() - start_time
