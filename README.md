# git-stuck
A tool to help make more informed NFL fantasy picks.

The following tool was made possible by the [nflgame API](http://pdoc.burntsushi.net/nflgame) given by the github user [BurntSushi](https://github.com/BurntSushi). 

*filter.py* collects relevant player data (relevant as in, data points that give you points on fanduel) and exports it to a text file. Any text file, as shown in *filter.py-data*, has a number of tuples per file. Each space seperated value is of the following form...
```
'Player Name' 'Player Team' 'Player Pos.' Player FanDuel Pts
```
...where the Player Name/Team/Pos. are strings and Player Fanduel Pts is a float.
There is one for every player in their respective position, i.e, quarterbacks, wide receivers, running backs, and tight ends for each week so far of the 2015 NFL regular season. Again *filter.py-data* has everything pretty straight forward, but let me know of any comments/advice/concerns. 
