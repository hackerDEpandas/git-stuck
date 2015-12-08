from datetime import datetime
start_time = datetime.now()
import nflgame as nf

games = nf.games(2015, week = [10,11,12,13])
players = nf.combine_game_stats(games)
name_arr = []
arr = []
tuples = []

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

teams = ['BAL', 'CAR', 'CHI', 'DEN', 'NE', 'NYJ', 'PIT']
for i in combine_data(teams):
	print i
print datetime.now() - start_time
