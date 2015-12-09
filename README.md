# git-stuck
A tool to help make more informed NFL fantasy picks.

The following tool was made possible by the [nflgame API](http://pdoc.burntsushi.net/nflgame) given by the github user [BurntSushi](https://github.com/BurntSushi). 

*use_these.py* collects relevant player data (relevant as in, data points that give you points on fanduel) and exports them to a text file. Text files in the folders *quarter_backs*, *runing_backs*, and *wide_receivers_tight_ends*, have a number of tuples per file. Each space seperated tuple is of the following form...
```
'Player Name' 'Player Team' 'Player Pos.' 'Player FanDuel Pts.'
```
...where the Player Name/Team/Pos are strings and Player Fanduel Pts is a float.
There is one for every player in their respective position, i.e, quarterbacks, wide receivers, running backs, and tight ends for each week so far of the 2015 NFL regular season. 

*new_filter_tool.py* gives you the best players as far as matchups go for the current NFL week. Scroll down to **new_filter_tool.py** to get more information on how I'm finding the best matchups. Similar to *quarter_backs*, *runing_backs*, and *wide_receivers_tight_ends* in *data.txt*, the text files in *picks_(current NFL week)* return tuples. For *running_back_picks_(current NFL week)*, *tight_end_picks_(current NFL week)*, and *wide_receiver_picks_(current NFL week)* the tuples are of the following form..
```
'Player Name' 'Player Team' 'Player Pos.' 'Player Rec' 'Player RecYds' 'Player RecTds' 'Player RuYds' 'Player RuTds' 'Player FumLost' 'Player FanDuel Pts'
```
...where Player Name/Team/Pos are strings, Player Rec/RecYds/RecTds/RuYds/RuTds/FumLost are integers, and player FanDuel Pts is a float. For *quarter_back_picks_(current NFL week)* the tuples are of the following form...
```
'Player Name' 'Player Team' 'Player Pos.' 'Player PassYds' 'Player PassTds' 'Player RuYds' 'Player RuTds' 'Player PassInts' 'Player FumLost' 'Player FanDuel Pts'
```
...where Player Name/Team/Pos are strings, Player PassYds/PassTds/RuYds/RuTds/PassInts/FumLost are integers, and player FanDuel Pts is a float. Again *data.txt* has everything pretty straight forward, but let me know of any comments/advice/concerns. 

## use_these.py
If you're planning on running the scripts in *use_these.py* yourself, then you'll need the following:
* [nflgame module](https://github.com/BurntSushi/nflgame)
* [pandas](http://pandas.pydata.org/getpandas.html)
* [numpy](http://docs.scipy.org/doc/numpy-1.10.1/user/install.html)

Once you have all those packages, you're ready to run *passing.py*, *receiving.py*, and *rushing.py*. I've also uploaded the data as text files in the folder *data.txt* under *quarter_backs*, *runing_backs*, and *wide_receivers_tight_ends*, so if you're not a programmer you can easily look at the data.  

## new_filter_tool.py
The *new_filter_tool.py* is used based off the positive matchups given by the good people over at [FFToday](http://fftoday.com/stats/fantasystats.php?o=3&PosID=99&Data=Last5&Show1=10&Show2=17&LeagueID=1). If you're planning on running the scripts in *new_filter_tool.py* yourself, then you'll need the following:
* [nflgame module](https://github.com/BurntSushi/nflgame)
* [pandas](http://pandas.pydata.org/getpandas.html)
* [numpy](http://docs.scipy.org/doc/numpy-1.10.1/user/install.html)

Once you have all those packages, you're ready to run *filter_pass.py*, *filter_rush.py*, *filter_wide.py*, and *filter_tight.py*. I've also uploaded the data as text files in the folder *data.txt* under *picks_(current NFL week)*, so if you're not a programmer you can easily look at the data. 
