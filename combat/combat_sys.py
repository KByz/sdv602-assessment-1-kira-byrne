"""
Define troll health & attack 
"""

import types
import cmd_parser.command_parser as cmd
import status.health as health


"""
Define combat system
"""
 #IF attack, troll health - player attack
#check if troll health = <0, if yes, set game location to "dead_troll", set game state back to explore.
    # set game state to explore, call cmd.move([cmd.move, 'Troll_Dead'])
     #if troll health is > 0, minus troll attack from player health
    #check if player health = 0, if yes, return game_over string.
#return player health and troll health to window

def combat(pPlace):
    global _player_health
    global _player_attack
    global _troll_health
    global _troll_attack

    result = "" #emptry string 
    pCommand = pPlace[1] #defines area of combat in game_place where combat commands are valid.
    print(pPlace, 'INSIDE COMBAT')
    if pCommand == 'attack':
        health._troll_health -= health._player_attack #reduce health from player and troll when attack is called
        health._player_health -= health._troll_attack
        if health._troll_health <= 0: #Check for troll's health, when less than or euqal to 0, move to next stage in game
            result = cmd.move([cmd.move, 'Troll_Dead']) #reuturn player to explore state and next story stage
        elif health._player_health <= 0:  #check for player health, if less than or equal to 0, return 'game over'
            result = 'You have been slain by the troll! Game Over!' + cmd.move([cmd.move, 'Game_Over'])
        else:
            result = 'You attacked the troll\n' + cmd.move([cmd.move, 'Troll_Fight']) #State attack story while troll and player are alive, remain at Troll_Fight
    elif pCommand == 'potion': #Increase player health by 400 when potion is called
        health. _player_health += 400
        result = 'You have restored your health!' + cmd.move([cmd.move, 'Troll_Fight']) #state health has been restored, return to combat
    else:
        result = 'You cannot do that here.' + cmd.move([cmd.move, 'Troll_Fight']) #Handle invalid or illegal input

    return result


