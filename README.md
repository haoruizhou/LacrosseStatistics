# LacrosseStatistics
## General Commands
#### Initialization (i)
Declare the information about both of the teams

Six questions will be asked

- Self Team Name, Coach's name, Past Record (Format: W-L-T)

- Opponent Team Name, Coach's name, Past Record (Format: W-L-T)


#### Quit (q)
Input 'q' to end the program


##Game Commands
### Neutral Command
#### Quarters (+/-)
Input '+' to start a quarter

Input '-' to end a quarter
### Side Specific Commands
#####For input related to the user's team, start the input line with '' (blank).
#####For input related to the other team, start the input line with '#'.__

####Shot (a)
Definition: Shot, but did not score

Self Input 'axx', xx is the player's number

Opponent Input '#axx', xx is the player's number

Note: The number must be between 00 to 99


    'a00': The player 00 on your team made a shot
    '#a12': The opponent team's player 12 made a shot
    
 ####Penalty (p)
 Self Input ’pxxTYPEtypeTime‘, xx is the player's number
 
 TYPE: (p)ersonal fouls or (t)echnical fouls
 
 type: (sl)ashing, (tr)ipping, (cc)cross checking, (uc)unsportsmanlike conduct, (ur)unnecessary roughness, (ib)illegal body checking; 
 (ho)ding, (in)terference, (os)off sides, (pu)shing, (sc)reening, (st)alling, (wo)warding off
 
   