import nflgame as nf

games = nf.games(2015, week = [9,10,11,12])
players = nf.combine_game_stats(games)
name_arr = []
arr = []
tuples = []

##########################################################################
def runner_gen(team):
	for p in players.rushing().filter(rushing_att_gte = 0).sort('rushing_att'):
		if (str(p.guess_position) == 'RB' or str(p.guess_position) == 'HB') and str(p.team) == team:
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

teams = ['BAL', 'CAR', 'CHI', 'DEN', 'NE', 'NYJ']
for i in combine_data(teams):
	print i
