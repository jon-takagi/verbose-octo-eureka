Execute instructions
#################
there are about 6 million files that will do thing in noninterpretive mode in varying states of completeness.
running ai_test_main.py demonstrates Stupid_AI playing against a single player sitting in front of the local machine.
Networking mostly works, and can be demonstrated by playing networked_player_test_main.py, but will take some experimenting to ensure that the remote players are on the correct ports (expanded on in "networking")
As of 11:19, I am halfway through expanding load_game to fully inflate a client so that the network doesn't rely on streaming (more on that later). As of right now, it does not correctly run. The intended output is detailed in the section "load_game"
The other ones (loop_test.py, logic_test.py, color_test.py, tile_test.py, etc) are included to reveal my experimentation process (it's 11:19 and i'm not going to take the time to take them out of this .zip)
Note that the curses library was not ported to windows, so it will not work there.
Sounds are implemented using the afplay CLI that is included with Mac OS; I have only tested it using 10.12.6 however it should work with any system that can use npm.
Use the command `npm install --save afplay` to install afplay. If still no sound, go use a mac in the IRC. (use brew to get python3 on them probably.)


How to play
###########
locations specify a column as a letter in the range [a-zA-V] and a row as a number in [1-31] - Note that a1 and A1 are different
'help' shows available commands
move and attack take a subject and a target. The syntax is subj verb target, i.e. `a5 atk d8`
`info d6` shows information about the mech at d6. Players can only get info about their own mech. This command also shows the movement radius of the mech - tiles highlighted in green are viable move locations. However, in certain cases other Mech or cover will be highlighted green despite not being valid movement locations. The mech cannot move here, and attempting to do so will not waste a turn.
The highlighting issue could be fixed by adding a condition based on the is_walkable property of world.at(tile). See comments in World.py, line 101
the command `pass` ends your turn and the game prompts the next player for input.
All mechs have an attack range of 8 tiles, however, this is not visible. If a mech is not in range, there is no penalty for attempting to attack it. See comments in World.py line 79 for details on how this could be implemented

Game Mechanics
##############
Gadgets
--------
A gadget represents something carried by a mech, like a jetpack, shield, or gun.
The three types of gadgets working are movement, represented by Green dice; defense, represented by Blue dice; and attack, represented by Red dice.
The "Radar" in the bottom right of the screen shows each mech's loadout using these representations - RRGG means a mech carries two attack gadets and two movement gadgets.
A mech that appears as RRbb carries two attack and two defense gadgets, but both of the defense gadgets are destroyed.
Each mech carries 4 gadgets. If all 4 gadgets are destroyed, the mech is also destroyed.
As a mech takes damage, systems are destroyed at random. Mechs get no benefit from destroyed systems.
Carrying two movement systems ("GG") allows a mech to move over cover but not end its turn in cover.

Scores
--------
Each mech has a set of scores, randomly determined each turn based on what systems it carries.

Attacks
--------
When a mech is ordered to attack an enemy, first a number of "hits" is calculated.
The number of hits is the attacker's attack score minus the defender's defense score.
Then, each hit is checked to see if it causes damage. Each hit has a random score in [1-6] (a d6)
IF the target is NOT in cover, a score of 5 or 6 causes a point of damage and a gadget on the defending mech is destroyed.
IF the target IS in cover, a score of 4 or 5 strikes the cover, and lowers its height by one. ONLY a score of 6 will cause damage to the target.
Being in cover halves the chance of taking damage.
Cover is depicted as a numeral on a blue background by default. The numeral represents the current height of the cover.
Cover is only useful if it is >3 units high - if it is below this, it is too small to effectively hide behind, and you gain no benefit from being near it.
Cover is considered "nearby" if it is in any of the 4 units directly adjacent to the mech - there is no benefit to having cover diagonal, and line of sight is not considered.

Stations
----------
Stations are unmoving objects that are "captured" if the only mechs directly adjacent to them all belong to the same team.
If no mechs are adjacent, they retain their prior allegiance.
They do not act as cover.
Currently, nothing tracks them, however, a game mode could be written such that the game ends when all the stations belong to one team rather than the game ending when all enemy mech are destroyed.
